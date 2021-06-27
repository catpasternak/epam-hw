from homework01.task04 import check_sum_of_four


def test_lists_with_present_sums():
    """Testing lists with 4 zero sums"""
    a = [1, 1]
    b = [1, 1]
    c = [1, 0]
    d = [0, -2]
    assert check_sum_of_four(a, b, c, d) == 4


def test_lists_without_sums():
    """Testing lists without zero sums"""
    a = [1, 1]
    b = [1, 1]
    c = [1, 0]
    d = [0, 2]
    assert check_sum_of_four(a, b, c, d) == 0
