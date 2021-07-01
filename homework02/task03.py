"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
import itertools
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """Returns all combinations of elements from given lists"""
    comb_tuples = list(itertools.product(*args))
    comb_lists = [[elem for elem in tupl] for tupl in comb_tuples]
    return comb_lists
