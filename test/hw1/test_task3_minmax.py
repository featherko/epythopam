"""Test for task 3."""
import os
from typing import NoReturn, Optional, Tuple

import pytest

from homework.hw1.task3_minmax import find_maximum_and_minimum


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (os.path.join(os.getcwd(), "test", "hw1", "test.txt"), (1, 7)),
        (os.path.join(os.getcwd(), "test", "hw1", "test2.txt"), (-7, 128)),
        (os.path.join(os.getcwd(), "test", "hw1", "text3.txt"), (-123, 51234)),
    ],
)
def test_find_maximum_and_minimum(
    value: str, expected_result: Tuple[int, int]
) -> Optional[NoReturn]:
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result


os.path.join(os.getcwd(), "test.txt")
