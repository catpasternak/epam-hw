import pytest

from homework01.task02 import check_fib, check_fib_2

testdata = [
    ([0, 1, 1, 2, 3, 5, 8, 13], True),
    ([3, 5, 8, 13], True),
    ([2, 4, 6, 10, 16, 26], False),
    ([3, 5, 6, 7, 8, 9], False),
]


@pytest.mark.parametrize(
    "sequence, expected", testdata, ids=["fib", "fib part", "fib-like", "non-fib"]
)
def test_sequence_fibonacci_check(sequence, expected):
    """Testing that sequences are correctly defined as Fibonacci of not"""
    assert check_fib(sequence) == expected
    assert check_fib_2(sequence) == expected


def test_error_raised_when_zero_sequence():
    with pytest.raises(ValueError):
        check_fib_2([])
