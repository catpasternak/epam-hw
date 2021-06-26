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
    if len(nums) == 0:
        return "List is empty."
    if k <= 0:
        return "Second argument must be positive integer."
    if k > len(nums):
        k = len(nums)
    max_so_far = sum(nums[:k])
    while k > 0:
        for i in range(1, len(nums) - k + 1):
            subarr_sum = sum(nums[i : (i + k)])
            if subarr_sum > max_so_far:
                max_so_far = subarr_sum
        k -= 1
    return max_so_far
