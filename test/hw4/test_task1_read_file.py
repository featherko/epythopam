import os
from typing import NoReturn, Optional

import pytest

from homework.hw4.task1_read_file import read_magic_number


@pytest.mark.parametrize(
    ("name", "text", "expected_result"),
    [
        (
            "kun.txt",
            "2",
            True,
        ),
    ],
)
def test_magic_number_true(name, text, expected_result) -> Optional[NoReturn]:
    try:
        with open(name, "w") as f:
            f.write(text)
        assert expected_result == read_magic_number(f.name)
    except Exception as e:
        raise e
    finally:
        os.unlink(f.name)


@pytest.mark.parametrize(
    ("name", "text", "expected_result"),
    [
        (
            "kun.txt",
            "3",
            False,
        ),
    ],
)
def test_magic_number_false(name, text, expected_result) -> Optional[NoReturn]:
    try:
        with open(name, "w") as f:
            f.write(text)
        assert expected_result == read_magic_number(f.name)
    except Exception as e:
        raise e
    finally:
        os.unlink(f.name)


@pytest.mark.xfail(raises=ValueError)
def test_magic_exception_in_name() -> Optional[NoReturn]:
    read_magic_number(123)


@pytest.mark.xfail(raises=ValueError)
def test_magic_exception_in_text() -> Optional[NoReturn]:
    try:
        with open("kun.txt", "w") as f:
            f.write("asdfasdf")
            read_magic_number(f.name)
    except Exception as e:
        raise e
    finally:
        os.unlink(f.name)
