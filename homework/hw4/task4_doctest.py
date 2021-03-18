"""Task 4.

Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.
That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Fb.

    fizzbuss some numbers

    :param n: numbers to fizzbuzz
    :return: fizzbuzzed

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(1)
    ['1']
    """
    fb = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fb.append("fizz buzz")
        elif i % 3 == 0:
            fb.append("fizz")
        elif i % 5 == 0:
            fb.append("buzz")
        else:
            fb.append(f"{i}")
    return fb


""" - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open file, in wich tested function is located
 - Create docstring for tested function
 - At the end of docstring press Enter twice
 - Write down <function name>(arg), where function name - function to be tested
 and arg - argument that should be used for test
 - Press Enter
 - Write down supposed output of tested function
 - Press Enter
 - Check that selected docstring quotes are closed
 - Open terminal in IDE
 - Write pytest, press Enter
 """
