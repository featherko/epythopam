"""Task 1 text."""


def check_power_of_two(a: int) -> bool:
    """Power of two.

    Tests given number if it's power of two

    :param a:  given number
    :return: Returns True if given number is power of two
    """
    if a <= 0:
        return False
    else:
        return not (bool(a & (a - 1)))
