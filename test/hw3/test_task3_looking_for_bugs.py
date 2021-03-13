from typing import Dict, Iterable, List, NoReturn, Optional

import pytest

from homework.hw3.task3_looking_for_bugs import Filter, make_filter


@pytest.mark.parametrize(
    ("keywords", "expected_result", "sample_data"),
    [
        (
            {"name": "polly"},
            [{"is_dead": True, "name": "polly"}],
            [
                {"is_dead": True, "name": "polly"},
                {"name": "Bill", "last_name": "Gilbert"},
            ],
        ),
    ],
)
def test_make_filter(
    expected_result: List, keywords: Dict, sample_data: List
) -> Optional[NoReturn]:
    actual_result = make_filter(**keywords).apply(sample_data)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("functions", "expected_result", "apply_range"),
    [
        (
            [lambda a: a % 2 == 0, lambda a: isinstance(a, int)],
            [-4, -2, 0, 2, 4],
            range(-5, 5),
        ),
    ],
)
def test_filter_apply(
    functions: List, expected_result: List, apply_range: Iterable
) -> Optional[NoReturn]:
    actual_result = Filter(functions).apply(apply_range)

    assert expected_result == actual_result
