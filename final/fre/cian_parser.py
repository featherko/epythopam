"""Parser for data."""
import json
import re
from time import sleep

import requests
from fake_useragent import UserAgent
from final.fre.pony_db import Flat, db_bind
from pony.orm import *
from requests_html import Element, HTML
from tenacity import retry, stop_after_attempt, wait_exponential


class CianParser:
    """Class to parse through cian.ru."""

    def __init__(self, domain: str, districts: str):
        self.domain = domain
        self.url = f"https://{domain}.cian.ru/cat.php"
        self.districts = districts
        self.s = requests.Session()
        self.s.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,ru;q=0.8,ka;q=0.7",
            "User-Agent": UserAgent().firefox,
            "Referer": "https://www.cian.ru/",
            "Cookie": "",
        }
        try:
            with open("cian.json", "r") as f:
                self.parsed = json.load(f)
        except FileNotFoundError:
            self.parsed = {}

    def save_parsed(self, district: str, page: int) -> None:
        """Save parsed.

        Saves parsed page count of given district

        :param district: district in question
        :param page: page
        """
        self.parsed[district] = page
        with open("cian.json", "w") as f:
            json.dump(self.parsed, f)

    def run(self) -> None:
        """To start parsing."""
        for d in self.districts:
            self.parse_page(district=d, page=self.parsed.get(str(d), 1))

    def parse_page(self, district: str, page: int = 1) -> None:
        """To parse  through each page.

        Parsing through pages for given district. Calls itself if it's not last page. Starts with first place, unless
        another page given.

        :param district: Given district
        :param page: Page
        """
        print("Parse", self.domain, district, page)
        r = self.get(district=district, page=page)
        html = HTML(html=r.content)
        flats = html.xpath("//div[@data-name='LinkArea']")
        for flat in flats:
            self.parse_flat(flat)

        if r.status_code == 302 or not flats:
            print(r.status_code, "Failed page")
            sleep(10)
            return self.parse_page(district=district, page=page)

        page += 1
        if html.xpath(
            f'//div[@data-name="Pagination"]//ul//li//a[text()="{page}"]'
        ):  # noqa: R503, calls itself
            self.save_parsed(district, page)
            return self.parse_page(district=district, page=page)

    @db_session
    def parse_flat(self, html: Element) -> None:  # noqa: CCR001
        """Get info about flat.

        Get all info about flat in given html element.

        :param html: Given element
        """
        try:
            flat_url = html.find("a", first=True).attrs.get("href")
            flat_id = int(re.search(r"flat/(\d+)", flat_url).group(1))
            location = html.xpath(".//a[@data-name='GeoLabel']/text()")
            if self.domain == "ekb":
                location = location[1:]
            city, district, *location = location
            location = " ".join(location)
            price = html.xpath(".//span[@data-mark='MainPrice']/text()", first=True)
            price = int(price.replace("₽", "").strip().replace(" ", ""))
            ppm = html.xpath(".//p[@data-mark='PriceInfo']/text()", first=True)
            ppm = int(ppm.replace("₽/м²", "").strip().replace(" ", ""))
            square = round(price / ppm, 2)
            if not Flat.exists(id=flat_id):
                Flat(
                    id=flat_id,
                    city=city,
                    district=district,
                    location=location,
                    price=price,
                    ppm=ppm,
                    square=square,
                )
                commit()
        except Exception as exc:
            print(exc)
            rollback()

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=16),
        reraise=True,
    )
    def get(self, district: str, page: int) -> requests.Response:
        """Get server response.

        Builds up needed url and gets response from server.
        ex: with district = 1, page 1
        url: https://www.cian.ru/cat.php?deal_type=sale&district[0]=1&engine_version=2&offer_type=flat&p=1

        :param district: given district
        :param page: given page
        :return: response from server
        """
        params = {
            "deal_type": "sale",
            "district[0]": district,
            "engine_version": 2,
            "offer_type": "flat",
            "p": page,
        }
        r = self.s.get(self.url, params=params, timeout=5, allow_redirects=False)
        r.raise_for_status()
        return r


if __name__ == "__main__":
    db_bind()
    domains = dict(  # noqa: C408
        spb=range(133, 151), ekb=range(286, 293), www=list(range(4, 12)) + [1, 151, 325]
    )
    for dom in domains:
        c = CianParser(domain=dom, districts=domains[dom])
        c.run()
