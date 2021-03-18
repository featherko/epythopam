from typing import NoReturn, Optional

import pytest
import requests

from homework.hw4.task2_mock_input import counts


class MockResponse:
    @property
    def text(self):
        return "i i asdfasdfasdf i i"


@pytest.fixture()
def _mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


@pytest.mark.usefixtures("_mock_response")
def test_get_count_on_mock_positive():
    result = counts("asd")
    assert result == 4


@pytest.mark.xfail(raises=ValueError)
def test_network_exception_counts() -> Optional[NoReturn]:
    counts("asdf")
