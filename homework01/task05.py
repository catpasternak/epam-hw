"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k",
with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_max_subarray_sum(nums: List[int], k: int) -> int:
    if k <= len(nums):
        max_length = k
    else:
        max_length = len(nums)
    max_so_far = sum(nums[:max_length])
    for subarr_length in range(max_length, 0, -1):
        for i in range(1, len(nums) - subarr_length + 1):
            subarr_sum = sum(nums[i : (i + subarr_length)])
            if subarr_sum > max_so_far:
                max_so_far = subarr_sum
    return max_so_far
