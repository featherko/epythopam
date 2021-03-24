from homework.hw5.task2_decor import print_result


def test_my_wrap_decorator():
    @print_result
    def name(a: int, b: int) -> int:
        """Weird docstring."""
        return a + b

    assert str(name.__doc__) == "Weird docstring."
    assert str(name.__name__) == "name"
