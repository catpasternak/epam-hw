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


def convert_string(string: str) -> str:
    """Converts into pure string without backspace characters"""
    if "#" not in string:
        return string
    flag = 0
    new_string = ""
    for char in reversed(string):
        if char == "#":
            flag += 1
        elif not flag:
            new_string = char + new_string
        else:
            flag -= 1
    return new_string


def backspace_compare(first: str, second: str) -> bool:
    """Compares 2 strings containing backspaces and returns if their printed versions are the same"""
    return convert_string(first) == convert_string(second)
