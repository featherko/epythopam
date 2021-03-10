"""Task 5.

Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""

from typing import Any, List, Sequence


def custom_range(
    iterable: Sequence, start: Any, stop: Any = None, step: int = 1
) -> List[Any]:
    """Customrange.

    Function that behaves as range function with given iterable of unique values.

    :param iterable: Given iterable
    :param start: Optional. An integer number specifying at which position to start. Default is 0
    :param stop: Required. An integer number specifying at which position to stop(not included)
    :param step: Optional. An integer number specifying the incrementation. Default is 1
    :return: returns a sequence
    """
    if stop is None:
        start, stop = iterable[0], start
    if step < 0:
        start, stop = stop, start
    return [
        iterable[i] for i in range(iterable.index(start), iterable.index(stop), step)
    ]
