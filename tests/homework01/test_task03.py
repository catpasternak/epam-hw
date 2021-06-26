import os

from homework01.task03 import find_min_and_max


def test_file_1_to_10():
    """Testing that file with integers 1 to 10 gives (1, 10)"""
    assert find_min_and_max(
        os.path.join(os.path.dirname(__file__), "file01_task03.txt")
    ) == (1, 10)


def test_file_10_to_1():
    """Testing that file with reverse order gives (1, 10)"""
    assert find_min_and_max(
        os.path.join(os.path.dirname(__file__), "file02_task03.txt")
    ) == (1, 10)


def test_file_with_0_and_neg():
    """Testing that file with 0 and negative ints gives (-10, 10)"""
    assert find_min_and_max(
        os.path.join(os.path.dirname(__file__), "file03_task03.txt")
    ) == (-10, 10)
