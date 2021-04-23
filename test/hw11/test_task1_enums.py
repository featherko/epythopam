from homework.hw11.task1_enums import SimplifiedEnum


class RandomEnums(metaclass=SimplifiedEnum):
    __keys = ("Raz", "Potato", "PewPew")


def test_enums():
    assert RandomEnums.Raz == "Raz"
    assert RandomEnums.Potato == "Potato"
    assert RandomEnums.PewPew == "PewPew"
