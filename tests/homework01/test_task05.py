from homework01.task05 import find_max_subarray_sum


def test_max_sum_equal_k():
    """Testing that array from example gives 16"""
    assert find_max_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_max_sum_less_k():
    """Testing that array with max sum produced by subarray shorter than k
    gives correct result"""
    assert find_max_subarray_sum([1, 2, 3, -10, -20, 20], 3) == 20
