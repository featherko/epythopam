"""Task 3.

Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
"""
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """Count something in the file.

     function that takes directory path, a file extension and an optional tokenizer.
    It will count lines in all files with that extension if there are no tokenizer.
    If a the tokenizer is not none, it will count tokens.


    :param dir_path: Path to the directory with files
    :param file_extension: extension of files to be counted
    :param tokenizer: tokenizer to be used, if needed
    :return: total count
    """
    count = 0
    for file in dir_path.glob("*." + file_extension):
        with open(file) as f:
            if tokenizer:
                for line in f:
                    count += len(tokenizer(line))
            else:
                count += sum(1 for _ in f)
    return count
