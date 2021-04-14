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


@pytest.mark.parametrize(
    ("text1", "text2"),
    [
        ("1\n2\n3", "11\n22\n33"),
    ],
)
def test_merge_sorted_files_2(files):
    assert [1, 11, 2, 22, 3, 33] == list(merge_sorted_files(files))
