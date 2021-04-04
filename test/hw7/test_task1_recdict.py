import json
import os
from typing import NoReturn, Optional

import pytest

from homework.hw7.task1_recdict import find_occurrences


def example_tree_build():
    with open(os.path.join(os.getcwd(), "test", "hw7", "tree.json")) as f:
        return json.load(f)


exam = {1: 1, 2: 2, 3: 3}


@pytest.mark.parametrize(
    ("tree", "element", "expected_result"),
    [
        (
            example_tree_build(),
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
