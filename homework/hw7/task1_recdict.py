"""Task 1.

Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Dict, List

# Example tree:
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


def find_occurrences(tree: dict, element: Any) -> int:
    """To exclude when tree == element."""
    return 1 if tree == element else find_occurrences_rec(tree, element)


def find_occurrences_rec(tree: dict, element: Any) -> int:
    """Recursive function which find number of occurrences of element in tree."""
    found = 0

    found += go_deeper(tree, element)

    if isinstance(tree, dict):
        found += go_deeper(tree.values(), element)

    return found


def count_increment(checked: Any, element: Any) -> int:
    """Increments counter if checked item is equal to element."""
    return 1 if checked == element else 0


def check_nested_dict(value: Dict, element: Any) -> int:
    """Recursive call for nested dict."""
    return find_occurrences_rec(value, element) if isinstance(value, dict) else 0


def check_nested_list(checked: List, element: Any) -> int:
    """Recursive call for nested list."""
    return go_deeper(checked, element) if isinstance(checked, list) else 0


def go_deeper(checked: Any, element: Any) -> int:
    """Recursive loop that checks for nested lists/dicts and also counts."""
    found = 0
    for item in checked:
        found += check_nested_list(item, element)
        found += check_nested_dict(item, element)
        found += count_increment(item, element)
    return found


if __name__ == "__main__":
    print(find_occurrences_rec(example_tree, "RED"))

    exam = {a: b for a, b in zip(range(3), range(3))}

    print(find_occurrences_rec(exam, exam))
    z = {**exam, "a": exam}
    z = {**exam, "a": z}
    print(z)
    print(exam)
    print((find_occurrences_rec(z, exam)))
