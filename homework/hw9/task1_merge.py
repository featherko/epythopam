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
from pathlib import Path
from typing import Iterator, List, Optional, Union


def open_file(file_name: Union[Path, str]) -> Iterator:
    """Read from file, iterator.

    :param file_name: Path or str to file.
    :return: int value
    """
    with open(file_name) as f:
        for line in f:
            yield int(line)


def get_next(itr: Iterator) -> Optional[int]:
    """Get next value from iterator."""
    try:
        val = next(itr)
    except StopIteration:
        val = None
    return val  # noqa: R504


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """Merge sorted files.

    Merges any amount of sorted files.

    :param file_list: List with path/str to sorted files
    """
    files_open = [open_file(file) for file in file_list]
    nums = {file_open: next(file_open) for file_open in files_open}
    while True:
        key, minor = min(nums.items(), key=lambda x: x[1])
        yield minor
        a = get_next(key)
        if a:
            nums[key] = a
        else:
            del nums[key]
