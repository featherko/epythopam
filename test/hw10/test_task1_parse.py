import asynctest
import pytest

import homework
from homework.hw10.task1_parse import comp_info, get_page, get_page_comps


@pytest.mark.asyncio
async def test_get_company_info(monkeypatch):
    def fake_page(url):
        with open("test/m.html") as file:
            return file.read()

    fake_get_page = asynctest.CoroutineMock(get_page, side_effect=fake_page)
    monkeypatch.setattr(homework.hw10.task1_parse, "get_page", fake_get_page)
    res = {
        "name": "AO Smith",
        "href": "/stocks/aos-stock",
        "growth": 38.31,
        "code": "AOS",
        "P/E": 25.06,
        "price": 0,
        "profit": 0.85,
    }
    d = {"name": "AO Smith", "href": "/stocks/aos-stock", "growth": 38.31}
    actual_res = await comp_info(d, 0)
    assert res == actual_res


@pytest.mark.asyncio
async def test_get_companies_from_page(monkeypatch):
    def fake_page(url):
        with open("test/tab.html") as file:
            return file.read()

    fake_get_page = asynctest.CoroutineMock(get_page, side_effect=fake_page)
    monkeypatch.setattr(homework.hw10.task1_parse, "get_page", fake_get_page)

    actual_res = await get_page_comps(1)
    assert actual_res[0]["name"] == "3M"
    assert actual_res[1]["name"] == "AO Smith"
    assert actual_res[2]["name"] == "Abbott Laboratories"
