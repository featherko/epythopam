"""Task 2.

Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func
print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий
До применения вашего декоратор будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция
Ожидаемый результат:

>>> print(custom_sum.__doc__)
This function can sum any objects which have __add___.

>>> print(custom_sum.__name__)
custom_sum

print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""

import functools
from typing import Any, Callable


def my_update(wrapper: Callable, wrapped: Callable) -> Callable:
    """Update.

    Body of my_wrap decorator.
    """
    assigned = ("__name__", "__doc__")
    for atr in assigned:
        value = getattr(wrapped, atr)
        setattr(wrapper, atr, value)
    wrapper.__original_func = wrapped
    return wrapper


def my_wrap(func: Callable) -> Callable:
    """Wrap.

    Returns __name__, __doc__, __original_func of wrapped funcion
    """
    return functools.partial(my_update, wrapped=func)


def print_result(func: Callable) -> Callable:
    """Decr.

    Decorator, that prints result of wrapped function.
    """

    @my_wrap(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Function-wrapper which print result of an original function."""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args: Any) -> Any:
    """This function can sum any objects which have __add___."""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    without_print = custom_sum.__original_func
    print(custom_sum.__original_func)
    # the result returns without printing
    without_print(1, 2, 3, 4)
