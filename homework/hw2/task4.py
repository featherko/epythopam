"""Task 4.

Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2

"""

from typing import Callable


def cache(random_func: Callable) -> Callable:
    """Cache.

    Caches result of function.

    :param random_func: target function
    :return: cached result of function
    """
    cached = {}

    def inner(*args: int) -> int:
        if args not in cached:
            cached[args] = random_func(*args)
        return cached[args]

    return inner
