import string
from typing import Any, List, NoReturn, Optional, Sequence

import pytest

from homework.hw2.task5 import custom_range


@pytest.mark.parametrize(
    ("value", "expected_result", "args"),
    [
        (string.ascii_lowercase, ["a", "b", "c", "d", "e", "f"], ["g"]),
        (
            string.ascii_lowercase,
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
            ["g", "p"],
        ),
        (string.ascii_lowercase, ["p", "n", "l", "j", "h"], ["g", "p", -2]),
    ],
)
def test_custom_range(
    value: Sequence, expected_result: List[Any], args
) -> Optional[NoReturn]:
    actual_result = custom_range(value, *args)

    assert actual_result == expected_result
