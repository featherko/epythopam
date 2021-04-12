import os

import pytest

from homework.hw8.task1_sadtimes import KeyValueStorage


@pytest.fixture()
def file_name(data: str):
    filename = "test_hard_plz_work.txt"
    with open(filename, "w") as f:
        f.write(data)
    yield filename
    os.remove(filename)


@pytest.mark.parametrize(
    "data",
    [
        "1=run",
        "!=1",
        "Hello!=123",
        "def=def",
    ],
)
def test_value_error(file_name):
    with pytest.raises(ValueError, match="Invalid key!"):
        KeyValueStorage(file_name)


@pytest.mark.parametrize(
    ("data", "correct_storage"),
    [
        (
            "name=kek last_name=top power=9001 song=shadilay",
            {"name": "kek", "last_name": "top", "power": 9001, "song": "shadilay"},
        ),
        ("name=kek", {"name": "kek"}),
    ],
)
def test_key_value_storage(file_name, correct_storage):
    storage = KeyValueStorage(file_name)
    assert storage["name"] == storage.name == correct_storage["name"]
    assert storage.stor == correct_storage
