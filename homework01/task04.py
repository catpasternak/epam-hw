"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are
    such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    half_combies = {}
    for i in a:
        for j in b:
            if (i + j) not in half_combies:
                half_combies[i + j] = 1
            else:
                half_combies[i + j] += 1
    counter = 0
    for k in c:
        for m in d:
            if -(k + m) in half_combies:
                counter += half_combies[-(k + m)]
    return counter
