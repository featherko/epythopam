# flake8: noqa

import asyncio
import json
from heapq import nlargest
from typing import List, Dict

import aiohttp

from bs4 import BeautifulSoup


async def get_page(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()


async def exchange() -> float:
    url_cbr = "http://www.cbr.ru/scripts/XML_daily.asp"
    page = await get_page(url_cbr)
    page = BeautifulSoup(page, "lxml")
    exchange_r = page.find(id="R01235").find_next("value").get_text()
    return float(exchange_r.replace(",", "."))


async def page_cnt() -> int:
    url = "https://markets.businessinsider.com/index/components/s&p_500"
    page = await get_page(url)
    page = BeautifulSoup(page, "lxml")
    pages = page.find("div", class_="finando_paging").find_all("a")
    return len(pages)


async def get_page_comps(page: int):
    url_p = "https://markets.businessinsider.com/index/components/s&p_500?p={}"
    comps = []
    page = BeautifulSoup(await get_page(url_p.format(page)), "lxml")
    table = page.find(class_="table table-small")
    for row in table.find_all("tr")[1:]:
        comps.append(
            dict(
                name=row.find("a")["title"],
                href=row.find("a")["href"],
                growth=row.find_all("td")[9].text.split()[1],
            )
        )
    return comps


async def get_all_comps():
    pages = await page_cnt()
    tasks = [get_page_comps(i) for i in range(1, pages + 1)]
    print(tasks)
    return await asyncio.gather(*tasks)


async def comp_info(comp, exchange_rage: float) -> Dict:
    c_url = "https://markets.businessinsider.com" + comp["href"]
    page = BeautifulSoup(await get_page(c_url), "lxml")
    table = page.find("span", class_="price-section__category")
    code = table.find("span").text[2:]
    table = page.find("span", class_="price-section__current-value")
    price = float(table.text.replace(",", "")) * exchange_rage
    snapshots = page.find_all("div", class_="snapshot__highlow")
    if len(snapshots) < 2:
        low = high = 1
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
        "P/E": pe,
        "price": round(price, 2),
        "profit": round((high - low) / low, 2),
    }


async def get_all_info():
    comps = await get_all_comps()
    exchange_r = await exchange()
    tasks = []
    for page in comps:
        for comp in page:
            tasks.append(comp_info(comp, exchange_r))
    return await asyncio.gather(*tasks)


def save_to_json(filename: str, value_name: str, data: List[Dict]) -> None:
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
    """Start point."""
    companies_info = asyncio.run(get_all_info())
    save_to_json(
        "top_growth",
        "growth",
        nlargest(10, companies_info, key=lambda x: x["growth"]),
    )
    save_to_json(
        "top_PE",
        "P/E",
        nlargest(10, companies_info, key=lambda x: x["P/E"]),
    )
    save_to_json(
        "top_price",
        "price",
        nlargest(10, companies_info, key=lambda x: x["price"]),
    )
    save_to_json(
        "top_potential_profit",
        "profit",
        nlargest(10, companies_info, key=lambda x: x["profit"]),
    )


json_go()
