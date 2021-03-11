from homework.hw2.task4 import cache

counter = 0


def test_cache_decorator():
    @cache
    def f(a, b):
        global counter
        counter += 1
        return a + b

    assert f(1, 2) == 3
    assert counter == 1
    assert f(1, 2) == 3
    assert counter == 1
