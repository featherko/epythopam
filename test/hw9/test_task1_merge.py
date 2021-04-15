import os

import pytest

from homework.hw9.task1_merge import merge_sorted_files


@pytest.fixture()
def files(text1: str, text2: str):
    file1 = "file_1.txt"
    file2 = "file_2.txt"
    with open(file1, "w") as f1:
        f1.write(text1)
    with open(file2, "w") as f2:
        f2.write(text2)
    yield file1, file2
    os.remove(file1)
    os.remove(file2)


@pytest.mark.parametrize(
    ("text1", "text2"),
    [
        ("1\n3\n5", "2\n4\n6"),
    ],
)
def test_merge_sorted_files(files):
    for i, j in zip(range(1, 7), merge_sorted_files(files)):
        assert i == j


@pytest.fixture()
def files2(text1: str, text2: str, text3: str):
    file1 = "file_1_2.txt"
    file2 = "file_2_2.txt"
    file3 = "file_3_2.txt"
    with open(file1, "w") as f1:
        f1.write(text1)
    with open(file2, "w") as f2:
        f2.write(text2)
    with open(file3, "w") as f3:
        f3.write(text3)
    yield file1, file2, file3
    os.remove(file1)
    os.remove(file2)
    os.remove(file3)


@pytest.mark.parametrize(
    ("text1", "text2", "text3"),
    [
        ("1\n4\n7", "3\n5\n8", "2\n6"),
    ],
)
def test_merge_3_sorted_files(files2):
    for i, j in zip(range(1, 9), merge_sorted_files(files2)):
        assert i == j
