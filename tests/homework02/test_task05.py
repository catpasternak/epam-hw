import string

from homework02.task05 import custom_range


def test_func_acts_like_range_given_one_parameter():
    assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]


def test_func_acts_like_range_given_two_parameters():
    assert custom_range(string.ascii_lowercase, "g", "i") == ["g", "h"]


def test_func_acts_like_range_given_three_parameters():
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]
