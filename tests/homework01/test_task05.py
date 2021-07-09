import pytest

from homework01.task05 import find_max_subarray_sum

testdata = [([1, 3, -1, -3, 5, 3, 6, 7], 3, 16), ([1, 2, 3, -10, -20, 20], 3, 20)]


@pytest.mark.parametrize(
    "array, k, expected", testdata, ids=["len(maxsum)=k", "len(maxsum)<k"]
)
def test_max_sum_counted(array, k, expected):
    """Testing that max subarray is count including case with subarr length less than given"""
    assert find_max_subarray_sum(array, k) == expected
