import pytest

from homework07.task02 import backspace_compare

testdata = [(("ab#c", "ad#c"), True), (("a##c", "#a#c"), True), (("a#c", "b"), False)]


@pytest.mark.parametrize("strings, expected", testdata)
def test_string_compare_function(strings, expected):
    """Testing backspaces are correctly handled"""
    assert backspace_compare(*strings) == expected
