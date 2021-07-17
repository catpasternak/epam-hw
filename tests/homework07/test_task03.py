import pytest

from homework07.task03 import tic_tac_toe_checker

testdata = [
    ([["x", "o", "o"], ["-", "x", "o"], ["-", "x", "x"]], "x wins!"),
    ([["x", "o", "-"], ["-", "o", "x"], ["x", "o", "-"]], "o wins!"),
    ([["x", "o", "x"], ["o", "o", "x"], ["x", "x", "o"]], "draw!"),
    ([["-", "-", "-"], ["o", "x", "-"], ["-", "-", "-"]], "unfinished!"),
]


@pytest.mark.parametrize("test_input, expected", testdata)
def test_game_checker(test_input, expected):
    """Testing that function returns winner or reflects current situation correctly"""
    assert tic_tac_toe_checker(test_input) == expected
