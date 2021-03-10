"""Task 3.

Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
import itertools
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """Combs.

    Returns all possible lists of some items, where first element from the first list, the second is from the second
    and so on, from given Amount of lists.

    :param args: Given lists
    :return:  All possible combinations
    """
    return list(map(list, (itertools.product(*args))))
