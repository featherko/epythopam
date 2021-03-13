"""Task 1."""

from typing import Callable


def cache(times: int) -> Callable:
    """Cache.

    Caches result of function.

    :param times: times of recall before clearing cache
    :return: cached result of function
    """
    cached = {}

    def wrapper(random_func: Callable) -> int:
        def inner(*args: int) -> int:
            if args not in cached:
                cached[args] = [random_func(*args), 1]
            else:
                cached[args][1] += 1
                if cached[args][1] == times:
                    temp = cached[args][0]
                    del cached[args]
                    return temp
            return cached[args][0]

        return inner

    return wrapper


@cache(times=3)
def f(a: int, b: int) -> int:
    """F."""
    return a + b
