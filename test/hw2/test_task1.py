import os
from typing import List, NoReturn, Optional

import pytest

from homework.hw2.task1 import count_not_ascii_chars, count_punctuation_chars
from homework.hw2.task1 import (
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


@pytest.mark.parametrize(
    ("file_path", "expected_result"),
    [
        (
            os.path.join(os.getcwd(), "test", "hw2", "testlongest.txt"),
            [
                "ab",
                "abc",
                "abcde",
                "abcdef",
                "abcdefg",
                "abcdefgh",
                "abcdefghi",
                "abcdefghij",
                "abcdefghijk",
                "abcdefghijkl",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(
    file_path: str, expected_result: List[str]
) -> Optional[NoReturn]:
    actual_result = get_longest_diverse_words(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("file_path", "expected_result"),
    [
        (os.path.join(os.getcwd(), "test", "hw2", "testrarest.txt"), "a"),
    ],
)
def test_get_rarest_char(file_path: str, expected_result: str) -> Optional[NoReturn]:
    actual_result = get_rarest_char(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("file_path", "expected_result"),
    [
        (os.path.join(os.getcwd(), "test", "hw2", "testpunctio.txt"), 7),
    ],
)
def test_count_punctuation_chars(
    file_path: str, expected_result: int
) -> Optional[NoReturn]:
    actual_result = count_punctuation_chars(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("file_path", "expected_result"),
    [
        (os.path.join(os.getcwd(), "test", "hw2", "testnotascii.txt"), 5),
    ],
)
def test_count_not_ascii_chars(
    file_path: str, expected_result: int
) -> Optional[NoReturn]:
    actual_result = count_not_ascii_chars(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("file_path", "expected_result"),
    [
        (os.path.join(os.getcwd(), "test", "hw2", "textcommon.txt"), "ü"),
    ],
)
def test_get_most_common_non_ascii_char(
    file_path: str, expected_result: str
) -> Optional[NoReturn]:
    actual_result = get_most_common_non_ascii_char(file_path)

    assert actual_result == expected_result
