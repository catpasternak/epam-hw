"""
Given an array of size n, find the most common and the least common element.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Finds most common and least common elements in list"""
    frequencies = Counter(inp)
    sorted_freq = frequencies.most_common()
    return sorted_freq[0][0], sorted_freq[-1][0]
