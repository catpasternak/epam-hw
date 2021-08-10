"""
Write down the function, which reads input line-by-line, and find maximum
and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_min_and_max(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        min_value = max_value = int(fi.readline())
        for line in fi:
            if int(line) > max_value:
                max_value = int(line)
            if int(line) < min_value:
                min_value = int(line)
    return min_value, max_value
