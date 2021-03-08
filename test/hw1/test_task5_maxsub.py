"""Test for task 5."""

from typing import List, NoReturn, Optional

import pytest

from homework.hw1.task5_maxsub import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ("array", "k", "expected_result"),
    [([1, 2, 3, 4, 5], 1, 5), ([-1, -2, -3], 1, -1), ([-1, -2, 3], 1, 3)],
)
def test_check_power_of_two(
    array: List[int], k: int, expected_result: int
) -> Optional[NoReturn]:
    actual_result = find_maximal_subarray_sum(array, k)

    assert actual_result == expected_result
