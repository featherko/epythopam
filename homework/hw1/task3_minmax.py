"""Task 3.

Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""

from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Find max and min.

    Function that reads input line by line and then returns minimum and maximum values

    :param file_name: Input file
    :return: : Min, Max
    """
    """seq = []
    with open("input.txt") as fi:
        for line in fi:
            seq.append(line)
    return min(seq), max(seq)"""

    """
    #with open("input.txt") as fi:
        lines = fi.readlines()
        min_value = int(lines[0])
        max_value = int(lines[0])
        for line in lines:
            line = int(line)
            if line > max_value:
                max_value = line
            elif line < min_value:
                min_value = line
        return min_value, max_value
    """

    with open(file_name) as fi:
        lines = fi.readlines()
        lines = list(map(int, lines))
        lines.sort()
        return lines[0], lines[-1]
