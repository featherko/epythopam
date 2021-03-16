"""Task 2.

Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests
* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
import requests


def counts(url: str) -> int:
    """Count i.

    Counts amount of i on given URL.

    :param url: Given Url
    :return: Amount of i.
    """
    try:
        r = requests.get(url)
        return r.text.count("i")
    except requests.exceptions.RequestException:
        raise ValueError(f"Unreachable {url}")
