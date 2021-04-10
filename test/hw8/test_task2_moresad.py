import pytest

from homework.hw8.task2_moresad import TableData


@pytest.fixture()
def presidents():
    filename = "example.sqlite"
    with TableData(database_name=filename, table_name="presidents") as f:
        yield f


def test_len(presidents):
    assert len(presidents) == 3


def test_get_item(presidents):
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_contains(presidents):
    assert "Yeltsin" in presidents
    assert ("Washington" in presidents) is False


def test_iter(presidents):
    names = [president["name"] for president in presidents]
    assert names == ["Yeltsin", "Trump", "Big Man Tyrone"]
