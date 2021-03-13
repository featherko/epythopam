from homework.hw3.task1_times_cache import cache

counter = 0


def test_cache_decorator():
    @cache(times=2)
    def f(a, b):
        global counter
        counter += 1
        return a + b

    assert f(1, 2) == 3
    assert counter == 1
    assert f(1, 2) == 3
    assert counter == 1
    assert f(1, 2) == 3

    assert counter == 2
