"""Task 2."""

import functools
import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value: int) -> int:
    """Slow calc.

    Some weird voodoo magic calculations
    """
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def slowpoke_calc() -> int:
    """Slowpoke."""
    with Pool(60) as p:
        return functools.reduce(
            lambda x, y: x + y, list(p.map(slow_calculate, range(501)))
        )


if __name__ == "__main__":
    slowpoke_calc()
