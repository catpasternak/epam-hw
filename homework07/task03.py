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
from collections import defaultdict
from itertools import chain
from typing import List


def get_win_combs(board):
    """Returns all winning combinations for on board with size n*n cells.
    - Flattens board;
    - Collects combinations in rows;
    - Collects combinations in columns;
    - Collects combinations in diagonals.
    :param board: square board with cells filled with 'x', 'o', or '-'
    :type board: List[list]
    :return: List of winning combinations in form of indexes of cells, flattened board
    :rtype: List[list], tuple
    """
    n = len(board[0])
    flat = tuple(chain.from_iterable(board))
    win_combs = []
    for row_start in range(0, len(flat), n):
        for comb_start in range(row_start, row_start + n - 3):
            comb = []
            for index in range(comb_start, comb_start + 4):
                comb.append(index)
            win_combs.append(comb)
    for column_start in range(n):
        for comb_start in range(column_start, column_start + len(flat) + 1 - n * 4, n):
            comb = []
            for index in range(comb_start, comb_start + n * 4, n):
                comb.append(index)
            win_combs.append(comb)
    for row_start in range(0, len(flat) - n * 3, n):
        for diag_start in range(row_start, row_start + n - 3, 1):
            comb = []
            for index in range(diag_start, diag_start + (n + 1) * 4, n + 1):
                comb.append(index)
            win_combs.append(comb)
    for row_start in range(3, len(flat) - n * 3, n):
        for diag_start in range(row_start, row_start + n - 3):
            comb = []
            for index in range(diag_start, diag_start + (n - 1) * 4, n - 1):
                comb.append(index)
            win_combs.append(comb)
    return win_combs, flat


def check_winner_on_nxn(board):
    """Finds winner or returns current situation on board.
    - Gets all possible winning combinations
    - Collects combinations for each party
    - Removes combinations that have intersections
    - Counts scores and returns winner
    :param board: square playing field for tic-tac-toe game
    :type board: List[list]
    :return: phrase about who won
    :rtype: str
    """
    win_combs, flat_board = get_win_combs(board)
    combs = defaultdict(list)
    for comb in win_combs:
        symbol = flat_board[comb[0]]
        if symbol in ("x", "o"):
            if len(set(flat_board[i] for i in comb)) == 1:
                combs[symbol].append(comb)
    for key in combs.keys():
        unique_cells = combs.get(key)[0]
        for comb in combs.get(key)[1:]:
            for cell in comb:
                if cell in unique_cells:
                    combs.get(key).remove(comb)
                    break
            else:
                unique_cells.extend(comb)
    x_result = len(combs.get("x"))
    o_result = len(combs.get("o"))
    if x_result > o_result:
        return "x wins!"
    if x_result < o_result:
        return "o wins!"
    return "draw!"


"""
Below is solution to 3x3 board game.
"""


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
