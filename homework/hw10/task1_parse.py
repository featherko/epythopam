"""Task 1."""

import asyncio
import json
from heapq import nlargest
from typing import Dict, List, Tuple

import aiohttp
from bs4 import BeautifulSoup


async def get_page(url: str) -> str:
    """Async page request.

    Request to the page, and getting raw text from it.

    :param url: page url
    :return: raw text from this page.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()


async def exchange() -> float:
    """Exchange rate.

    Checks current exchange rate USD to RUB on cbr site.

    :return: Current exchange rate USD to RUB.
    """
    url_cbr = "http://www.cbr.ru/scripts/XML_daily.asp"
    page = await get_page(url_cbr)
    page = BeautifulSoup(page, "lxml")
    exchange_r = page.find(id="R01235").find_next("value").get_text()
    return float(exchange_r.replace(",", "."))


async def page_cnt() -> int:
    """Page count.

    Checks amount of pages with tables.

    :return: number of pages
    """
    url = "https://markets.businessinsider.com/index/components/s&p_500"
    page = await get_page(url)
    page = BeautifulSoup(page, "lxml")
    pages = page.find("div", class_="finando_paging").find_all("a")
    return len(pages)


async def get_page_comps(page: int) -> List[Dict]:
    """Table info about companies.

    Gets information about companies from table.

    :param page: number of the page we get info from.
    :return: List of dicts with info about companies
    """
    url_p = "https://markets.businessinsider.com/index/components/s&p_500?p={}"
    comps = []
    page = BeautifulSoup(await get_page(url_p.format(page)), "lxml")
    table = page.find(class_="table table-small")
    for row in table.find_all("tr")[1:]:
        comps.append(
            {
                "name": row.find("a")["title"],
                "href": row.find("a")["href"],
                "growth": row.find_all("td")[9].text.split()[1],
            }
        )
    return comps


async def get_all_comps() -> Tuple:
    """Info about companies.

    Gets information from all pages with tables through async methods.

    :return: List of dicts.
    """
    pages = await page_cnt()
    tasks = [get_page_comps(i) for i in range(1, pages + 1)]
    return await asyncio.gather(*tasks)


async def comp_info(comp: dict, exchange_rage: float) -> Dict:
    """Full information on company.

    Parse through company's page and return full requested info on this
    company

    :param comp: Raw data in dict form from get_page_comps
    :return: Full requested data in dict form
    """
    c_url = "https://markets.businessinsider.com" + comp["href"]
    page = BeautifulSoup(await get_page(c_url), "lxml")
    table = page.find("span", class_="price-section__category")
    code = table.find("span").text[2:]
    table = page.find("span", class_="price-section__current-value")
    price = float(table.text.replace(",", "")) * exchange_rage
    snapshots = page.find_all("div", class_="snapshot__highlow")
    if len(snapshots) < 2:
        text = snapshots[0].find("div", class_="snapshot__header").text
        if text != "52 Week Low":
            low, high = 1, 1
        else:
            low, high = (
                float(x.text.replace(",", "").split()[0])
                for x in snapshots[0].find_all("div", class_="snapshot__data-item")
            )
    else:
        low, high = (
            float(x.text.replace(",", "").split()[0])
            for x in snapshots[1].find_all("div", class_="snapshot__data-item")
        )
    try:
        pe = float(
            page.find("div", class_="snapshot")
            .find_all(class_="snapshot__data-item")[6]
            .text.split()[0]
        )
    except ValueError:
        pe = -1
    return {
        **comp,
        "code": code,
        "PE": pe,
        "price": round(price, 2),
        "profit": round((high - low) / low, 2),
    }


async def get_all_info() -> Tuple:
    """Information about all companies.

    Get's all full info about all companies, through async method.

    :return: Tuple of Dicts.
    """
    comps = await get_all_comps()
    exchange_r = await exchange()
    tasks = []
    for page in comps:
        for comp in page:
            tasks.append(comp_info(comp, exchange_r))
    return await asyncio.gather(*tasks)


def save_to_json(filename: str, value_name: str, data: List[Dict]) -> None:
    """Save data to json."""
    with open(filename + ".json", "w") as file:
        top_10 = [
            {
                "name": data[i]["name"],
                "code": data[i]["code"],
                value_name: data[i][value_name],
            }
            for i in range(10)
        ]
        json.dump(top_10, file, indent=4)


def json_go() -> None:
    """Make is json."""
    companies_info = asyncio.run(get_all_info())
    terms = ["growth", "PE", "price", "profit"]
    for term in terms:
        save_to_json(
            "top_growth",
            term,
            nlargest(10, companies_info, key=lambda x: x[term]),
        )
