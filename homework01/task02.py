"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence.

We guarantee, that the given sequence contains >= 0 integers inside.
"""

import math
from typing import Sequence


def check_perfect_square(num):
    root = int(math.sqrt(num))
    return root ** 2 == num


def check_fib(data: Sequence[int]) -> bool:
    try:
        # using try due to the case of negative int or shorter list
        # using 3rd element in order to make sure it exists
        expr_1 = 5 * data[2] ** 2 + 4
        expr_2 = 5 * data[2] ** 2 - 4
        if check_perfect_square(expr_1) or check_perfect_square(expr_2):
            for i in range(2, len(data)):
                if data[i] != data[i - 2] + data[i - 1]:
                    return False
            return True
        return False
    except (ValueError, IndexError):
        return False
