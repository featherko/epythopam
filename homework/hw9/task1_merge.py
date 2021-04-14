"""Task 1.

Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
"""
from itertools import zip_longest
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """Merge sorted files.

    Merges any amount of sorted files.

    :param file_list: List with path/str to sorted files
    """
    files = [open(path) for path in file_list]
    for tup in zip_longest(*files):
        for val in tup:
            if val:
                yield int(val)
    for f in files:
        f.close()
