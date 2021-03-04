"""Task 5.

Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """Maximum sum.

    Finds  a sub-array with length less or equal to "k", with maximal sum.

    :param nums:  given array
    :param k:  maximum number of elements in sub-array
    :return: maximal sum
    """
    max_sum = max(nums, key=lambda x: x < 0)
    for i in range(len(nums)):
        current = 0
        for j in range(k):
            current += nums[i + j]
            if current > max_sum:
                max_sum = current
            if j + k == len(nums):
                break
    return max_sum
