import string

import pytest

from homework02.task05 import custom_range

testdata = [
    ((string.ascii_lowercase, "g"), ["a", "b", "c", "d", "e", "f"]),
    ((string.ascii_lowercase, "g", "i"), ["g", "h"]),
    ((string.ascii_lowercase, "p", "i", -2), ["p", "n", "l", "j"]),
]


@pytest.mark.parametrize("arguments, expected", testdata)
def test_custom_range(arguments, expected):
    """Tests that custom_range returns correct sequence with different number of args."""
    assert custom_range(*arguments) == expected


def test_error_raised_with_wrong_number_of_args():
    """Tests that TypeError is raised when number of args is less than 1 or more than 4."""
    with pytest.raises(TypeError):
        custom_range(string.ascii_lowercase, "o", "p", "q", "r")
