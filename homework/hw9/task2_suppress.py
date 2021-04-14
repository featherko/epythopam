"""Task 2.

Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
"""
from contextlib import contextmanager
from typing import Any


@contextmanager
def suppressor(exc: Exception) -> None:  # noqa: D103
    try:
        yield
    except exc:
        pass


with suppressor(IndexError):
    [][2]


class Suppressor:  # noqa: D101
    def __init__(self, *exceptions: Any):
        self._exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exctype, excinst, exctb):  # noqa: ANN001
        return exctype is not None and issubclass(exctype, self._exceptions)


with Suppressor(IndexError):
    [][2]
