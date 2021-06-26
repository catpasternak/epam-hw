from homework01.task02 import check_fib


def test_true_fib_seq():
    """Testing the original Fibonacci sequence"""
    assert check_fib([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])


def test_fib_alike_seq():
    """Testing sequence that satisfies n=(n-1)+(n-2) but is not Fibanacci"""
    assert not check_fib([4, 6, 10, 16, 26, 42, 68])


def test_wrong_seq():
    """Testing non Fibonacci sequence"""
    assert not check_fib([3, 5, 6, 7, 8, 9, 12])


def test_too_short_seq():
    """Testing sequence that is too short to be evaluated"""
    assert not check_fib([0, 1])
