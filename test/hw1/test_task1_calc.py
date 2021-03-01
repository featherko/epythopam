"""Test for task 1."""

from typing import NoReturn, Optional

import pytest

from homework.hw1.task1_calc import check_power_of_two


@pytest.mark.parametrize(
    ("value", "expected_result"), [(65536, True), (12, False), (-12, False), (0, False)]
)
def test_check_power_of_two(value: int, expected_result: bool) -> Optional[NoReturn]:
    actual_result = check_power_of_two(value)

    assert actual_result == expected_result
