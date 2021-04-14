import os
from pathlib import Path

import pytest

from homework.hw9.task3_tokotoko import universal_file_counter


@pytest.fixture()
def start_dir():
    for i in range(1, 3):
        filename = "./test/test_" + str(i) + ".txt"
        with open(filename, "w") as f:
            f.write((((str(i) + " ") * i) + "\n") * i)
    yield Path("./test")
    for i in range(1, 3):
        os.remove("./test/test_" + str(i) + ".txt")


def test_universal_file_counter(start_dir):
    assert universal_file_counter(start_dir, "txt") == 3
    assert universal_file_counter(start_dir, "txt", str.split) == 5
