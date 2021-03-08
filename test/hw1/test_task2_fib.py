"""Test for task 2."""


from typing import NoReturn, Optional, Sequence

import pytest

from homework.hw1.task2_fib import check_fibonacci


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ([0, 1, 1, 2], True),
        ([0, 1], True),
        ([], False),
        ([0, 1, 1, 2, 3, 5, 8], True),
    ],
)
def test_check_fibonacci(
    value: Sequence[int], expected_result: bool
) -> Optional[NoReturn]:
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
