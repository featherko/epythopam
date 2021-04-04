from typing import NoReturn, Optional

import pytest

from homework.hw7.task2_backspace import backspace_compare, random_fun


@pytest.mark.parametrize(
    ("string1", "string2", "expected_result"),
    [
        (
            "ab#c",
            "ad#c",
            True,
        ),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
        ("", "", True),
    ],
)
def test_calc_backspace(string1, string2, expected_result) -> Optional[NoReturn]:
    actual_result = backspace_compare(string1, string2)
    assert expected_result == actual_result


@pytest.mark.parametrize(
    ("string1", "string2", "expected_result"),
    [
        (
            "ab#c",
            "ad#c",
            True,
        ),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
        ("", "", True),
    ],
)
def test_random_fun(string1, string2, expected_result) -> Optional[NoReturn]:
    actual_result = random_fun(string1, string2)
    assert expected_result == actual_result
