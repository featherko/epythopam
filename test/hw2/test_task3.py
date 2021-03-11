from typing import Any, List, NoReturn, Optional

import pytest

from homework.hw2.task3 import combinations


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ([[1, 2], [3, 4]], [[1, 3], [1, 4], [2, 3], [2, 4]]),
        ([[1], [2, 3]], [[1, 2], [1, 3]]),
    ],
)
def test_combinations(
    value: List[Any], expected_result: List[List]
) -> Optional[NoReturn]:
    actual_result = combinations(*value)

    assert actual_result == expected_result
