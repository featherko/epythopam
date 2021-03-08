"""Test for task 4."""

from typing import List, NoReturn, Optional

import pytest

from homework.hw1.task4_sum41 import check_sum_of_four


@pytest.mark.parametrize(
    ("a", "b", "c", "d", "expected_result"),
    [([0, 0], [0], [0], [0], 2), ([1, 2], [-2, -1], [-1, 2], [0, 2], 2)],
)
def test_check_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
) -> Optional[NoReturn]:
    actual_result = check_sum_of_four(a, b, c, d)

    assert actual_result == expected_result
