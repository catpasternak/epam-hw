import pytest

from homework07.task03 import check_winner_on_nxn, tic_tac_toe_checker

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


testdata_6x6 = [
    (
        [
            ["o", "o", "o", "o", "o", "o"],
            ["-", "-", "-", "-", "-", "-"],
            ["o", "x", "x", "x", "x", "x"],
            ["-", "o", "-", "-", "x", "-"],
            ["-", "-", "o", "x", "-", "-"],
            ["-", "-", "x", "o", "-", "-"],
        ],
        "draw!",
    ),
]


@pytest.mark.parametrize("test_input, expected", testdata_6x6)
def test_nxn_game_checker(test_input, expected):
    """Testing function for n*n field and 4-in-row winning combinations"""
    assert check_winner_on_nxn(test_input) == expected
