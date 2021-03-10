"""Task 1."""


import string
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Longest diverse.

    Gets 10 longest  words consisting from largest amount of unique symbols from given file.

    :param file_path: Given file
    :return: List of words
    """
    with open(file_path, encoding="unicode-escape") as f:
        text = f.read()
    text = text.translate(str.maketrans(dict.fromkeys(string.punctuation)))
    words = list(set(text.replace("-\n", "").replace("\n", " ").split(" ")))
    return sorted(words, key=lambda x: len(set(x)))[-10:]


def get_rarest_char(file_path: str) -> str:
    """Rarest char.

    Finds rarest symbol for given document

    :param file_path:  Given document
    :return: Rarest symbol
    """
    with open(file_path, encoding="unicode-escape") as f:
        text = f.read()
    char_dict = {}
    for char in set(text):
        char_dict[char] = text.count(char)
    return sorted(char_dict.items(), key=lambda x: x[1])[0][0]


def count_punctuation_chars(file_path: str) -> int:
    """Count punctuation.

    Count every punctuation char in given document.

    :param file_path:  Given document
    :return: number of punctuation chars
    """
    with open(file_path, encoding="unicode-escape") as f:
        counter = 0
        for char in f.read():
            if char in string.punctuation:
                counter += 1
        return counter


def count_not_ascii_chars(file_path: str) -> int:
    """Count not ascii.

    Count every non ascii char in given document

    :param file_path: Given Document
    :return: number of not ascii chars
    """
    with open(file_path, encoding="unicode-escape") as f:
        text = f.read()
    chars = set(text) - set(
        string.punctuation + string.ascii_letters + string.digits + "\n "
    )
    return sum(text.count(x) for x in chars)


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Not ascii.

    Finds most common non ascii char for given document

    :param file_path: Given document
    :return: Most common not ascii char
    """
    with open(file_path, encoding="unicode-escape") as f:
        text = f.read()
    chars = set(text) - set(
        string.punctuation + string.ascii_letters + string.digits + "\n "
    )
    char_dict = {}
    for char in chars:
        char_dict[char] = text.count(char)
    return sorted(char_dict.items(), key=lambda x: x[1])[-1][0]
