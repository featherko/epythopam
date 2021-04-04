"""Task 2.

Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
from typing import List


def calc_backspace(text: str) -> str:
    """Re-write text with backspace instead of #."""
    new_string = []
    for char in text:
        if char != "#":
            new_string.append(char)
        elif len(new_string) > 0:
            new_string.pop()
    return "".join(new_string)


def backspace_compare(first: str, second: str) -> bool:
    """Compare if two given strings are equal."""
    return calc_backspace(first) == calc_backspace(second)


"""some proof of concept"""


def random_fun(string: str, string2: str) -> bool:  # noqa: CCR001
    """Compare if two given strings are equal."""
    istr = []
    kstr = []
    iflag = 0
    kflag = 0
    for i, k in zip(string[::-1], string2[::-1]):
        iflag = flags_check(i, iflag, istr)
        kflag = flags_check(k, kflag, kstr)
        a = min(len(istr), len(kstr))
        if istr[:a] != kstr[:a]:
            return False
    return kstr == istr


def flags_check(char: str, flag: int, val_string: List) -> int:
    """Check flag count.

    Recalculates flag count or writes new element into list

    :param char: given character
    :param flag: flag value
    :param val_string: list of characters
    """
    if char != "#" and flag == 0:
        val_string.append(char)
    elif char != "#":
        flag -= 1
    else:
        flag += 1
    return flag
