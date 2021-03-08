"""Task 4.

Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
import itertools
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Check sum 4.

    Checks how many tuples i, k, k, l there are such chat A[i], B[j], C[k], D[l] is zero

    :param a: First list (A)
    :param b: Second List (B)
    :param c: Third List (C)
    :param d: Forth List (D)
    :return: Number of such tuples
    """
    return sum(1 for x in itertools.product(a, b, c, d) if sum(x) == 0)
