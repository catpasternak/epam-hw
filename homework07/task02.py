"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
from itertools import zip_longest


def generate_from_str(string):
    """Generates characters from given string in reversed order in such a manner,
    that '#' symboles are not printed and delete letters before them.
    :param string: input string containing letter and '#' symbols
    :type string: str
    """
    pawn_flag = 0
    for char in reversed(string):
        if char == "#":
            pawn_flag += 1
        else:
            if pawn_flag:
                pawn_flag -= 1
            else:
                yield char


def backspace_compare(first: str, second: str) -> bool:
    """Compares 2 strings containing backspaces and returns if their printed versions are the same.
    Symbol '#' is hadled as backspace key when printing.
    :param first: first string to compare
    :type first: str
    :param second: second string to compare
    :type second: str
    :return: `True` if strings are equal when printed, `False` otherwise
    :rtype: bool
    """
    for first, second in zip_longest(
        generate_from_str(first), generate_from_str(second)
    ):
        if first != second:
            return False
    return True
