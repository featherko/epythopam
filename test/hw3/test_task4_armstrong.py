from typing import NoReturn, Optional

import pytest

from homework.hw3.task4_armstrong import is_armstrong


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (153, True),
        (10, False),
    ],
)
def test_is_armstrong(value: int, expected_result: bool) -> Optional[NoReturn]:
    actual_result = is_armstrong(value)

    assert actual_result == expected_result
