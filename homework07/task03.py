"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from itertools import chain
from typing import List


def check_line(line: List) -> bool:
    """Checks an array for having all elements to be identical, except for the case of '-'"""
    if len(set(line)) == 1 and line[0] != "-":
        return True
    return False


def tic_tac_toe_checker(board: List[List]) -> str:
    """Checks rows, columns and diagonals to find winner or return other result"""
    for row in board:
        if check_line(row):
            return f"{row[0]} wins!"
    for i in range(3):
        column = [row[i] for row in board]
        if check_line(column):
            return f"{column[0]} wins!"
    if check_line([board[i][i] for i in range(3)]):
        return f"{board[0][0]} wins!"
    elif check_line([board[i][2 - i] for i in range(3)]):
        return f"{board[0][2]} wins!"
    elif "-" in chain(*board):
        return "unfinished!"
    return "draw!"
