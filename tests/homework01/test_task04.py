import pytest

from homework01.task04 import check_sum_of_four, check_sum_of_four_2

testdata = [
    (([1, 1], [1, 1], [1, 0], [0, -2]), 4),
    (([1, 1], [1, 1], [1, 0], [0, 2]), 0),
]


@pytest.mark.parametrize("lists, expected", testdata, ids=["4 sums", "no sums"])
def test_zero_sums_count(lists, expected):
    """Testing that function returns correct number of zero sums"""
    assert check_sum_of_four(*lists) == expected
    assert check_sum_of_four_2(*lists) == expected
