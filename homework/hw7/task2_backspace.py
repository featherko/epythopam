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


def calc_backspace(text: str) -> str:
    """Re-write text with backspace instead of #."""
    new_string = []
    for char in text:
        if char != "#":
            new_string.append(char)
        elif len(new_string) > 0:
            new_string.pop()
    return "".join(new_string)


"""Не знаю, какая лучше"""


def c(text: str) -> str:
    """Re-write text with backspace instead of #."""
    new_string = ""
    for char in text:
        if char != "#":
            new_string += char
        elif len(new_string) > 0:
            new_string = new_string[:-1]
    return new_string


def backspace_compare(first: str, second: str) -> bool:
    """Compare if two given strings are equal."""
    return c(first) == c(second)


"""some proof of concept"""


def random_fun(string: str, string2: str) -> bool:  # noqa: CCR001
    """Compare if two given strings are equal."""
    istr = ""
    kstr = ""
    iflag = 0
    kflag = 0
    for i, k in zip(string[::-1], string2[::-1]):
        if i != "#" and iflag == 0:
            istr += i
        elif iflag > 0 and i != "#":
            iflag -= 1
        else:
            iflag += 1

        if k != "#" and kflag == 0:
            kstr += k
        elif kflag > 0 and k != "#":
            kflag -= 1
        else:
            kflag += 1

        a = min(len(istr), len(kstr))
        if istr[:a] != kstr[:a]:
            return False
    return kstr == istr
