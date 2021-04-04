"""Test 1."""

from homework.hw6.task1_counter import instances_counter


def test_instance_counter():
    @instances_counter
    class User:
        pass

    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3
    assert User.reset_instances_counter() == 3
    assert User.get_created_instances() == 0
