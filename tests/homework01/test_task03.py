import os

import pytest

from homework01.task03 import find_min_and_max


def _path_to(filename):
    return os.path.join(os.path.dirname(__file__), filename)


testdata = [
    ("file01_task03.txt", (1, 10)),
    ("file02_task03.txt", (1, 10)),
    ("file03_task03.txt", (-10, 10)),
]


@pytest.mark.parametrize(
    "filename, expected", testdata, ids=["ints 1-10", "ints 10-1", "include 0 and neg"]
)
def test_min_and_max_returned_correctly(filename, expected):
    """Testing min and max in 3 cases"""
    assert find_min_and_max(_path_to(filename)) == expected
