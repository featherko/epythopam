"""Task 1.

Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""

from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """Check fibonacci.

    Checks if given sequence is fibonacci sequence

    :param data:  given sequence
    :return:  Returns true if given sequence is fibonacci
    """
    if len(data) <= 2:
        return data == [0, 1]
    else:
        for i in range(2, len(data)):
            if not data[i] == data[i - 1] + data[i - 2]:
                return False
    return True
