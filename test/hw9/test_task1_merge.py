import os

import pytest

from homework.hw9.task1_merge import merge_sorted_files


@pytest.fixture()
def files(text1: str, text2: str):
    args = [text1, text2]
    for i, text in enumerate(args):
        file = f"test{i}_{i}.txt"
        with open(file, "w") as f:
            f.write(text)
    yield "test0_0.txt", "test1_1.txt"
    for i in range(len(args)):
        os.remove(f"test{i}_{i}.txt")


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
def files2(text1, text2, text3):
    args = [text1, text2, text3]
    for i, text in enumerate(args):
        file = f"test{i}.txt"
        with open(file, "w") as f:
            f.write(text)
    yield "test0.txt", "test1.txt", "test2.txt"
    for i in range(len(args)):
        os.remove(f"test{i}.txt")


@pytest.mark.parametrize(
    ("text1", "text2", "text3"),
    [
        ("1\n4\n7", "3\n5\n8", "2\n6"),
    ],
)
def test_merge_3_sorted_files(files2):
    for i, j in zip(range(1, 9), merge_sorted_files(files2)):
        assert i == j
