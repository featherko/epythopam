"""Task 4.

Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
import itertools
from typing import List

"""def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    answer = 0
    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    if a[i] + b[j] + c[k] + d[l] == 0:
                        answer += 1
    return answer"""


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


"""def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    counter = 0
    sum1 = {}
    for i in a:
        for j in b:
            if i + j not in sum1:
                sum1[i + j] = 1
            else:
                sum1[i + j] += 1
    for i in c:
        for j in d:
            if -1 * (i + j) in sum1:
                counter += sum1[-1 * (i + j)]
    return counter"""
