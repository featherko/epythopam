"""Task 1.

Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""
from typing import Type, TypeVar

T = TypeVar("T")


def instances_counter(some_class: Type[T]) -> Type[T]:
    """Decr.

    Decorator that updates class with get_created_instances and
    reset_instances_counter methods.
    """
    """itero = [
        '__new__',
        "get_created_instances",
        "reset_instances_counter",
        "count",
    ]"""

    class Countcls:
        """Countcls.

        Subclass for decoration purposes.
        """

        count = 0

        def __new__(cls):
            cls.count += 1

            return super(Countcls, Countcls).__new__(cls)

        """def __init__(self):
            Countcls.count += 1"""

        @classmethod
        def get_created_instances(cls: Type[T]) -> int:
            return cls.count

        @classmethod
        def reset_instances_counter(cls: Type[T]) -> int:
            temp = cls.count
            cls.count = 0
            return temp

    """for meth in itero:
        value = getattr(Countcls, meth)
        setattr(some_class, meth, value)"""

    for meth in Countcls.__dict__:
        if meth not in some_class.__dict__:
            setattr(some_class, meth, Countcls.__dict__[meth])
    """some_class.__new__ = Countcls.__new__
    some_class.get_created_instances = Countcls.get_created_instances
    some_class.reset_instances_counter = Countcls.reset_instances_counter
    some_class.count = Countcls.count"""
    return some_class


@instances_counter
class User:
    """Fodder."""

    pass


if __name__ == "__main__":
    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(User.reset_instances_counter())  # 3
