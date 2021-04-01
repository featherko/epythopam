from typing import NoReturn, Optional

import pytest

from homework.hw7.task1_recdict import find_occurrences


example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}
exam = {1: 1, 2: 2, 3: 3}


@pytest.mark.parametrize(
    ("tree", "element", "expected_result"),
    [
        (
            example_tree,
            "RED",
            6,
        ),
        (exam, 1, 2),
        ({**exam, "a": exam}, exam, 1),
        (exam, exam, 1),
    ],
)
def test_find_occurrences(tree, element, expected_result) -> Optional[NoReturn]:
    actual_result = find_occurrences(tree, element)
    assert actual_result == expected_result
