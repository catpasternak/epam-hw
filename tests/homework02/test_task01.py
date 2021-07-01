import os

from homework02.task01 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


def _path_to(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def test_longest_diverse_words():
    """Testing that function returns 10 words with biggest amount of unique symbols in it"""
    assert get_longest_diverse_words(_path_to("sample01_task01.txt")) == [
        "vorzutäuschen",
        "Fruchtbarkeit",
        "herabgesunken",
        "ungeschwächt",
        "Bürokraten",
        "Rotwelsch",
        "Oberfläche",
        "brunnenführende",
        "Technikern",
        "Verstaubte",
    ]


def test_rarest_char():
    """Testing that least common char in given file is returned"""
    assert get_rarest_char(_path_to("sample01_task01.txt")) == "j"


def test_punctuation_chars_count():
    """Testing that function counts every punctuation char in file"""
    assert count_punctuation_chars(_path_to("sample01_task01.txt")) == 12


def test_non_ascii_chars_count():
    """Testing that function counts every non-ASCII char in given file"""
    assert count_non_ascii_chars(_path_to("sample01_task01.txt")) == 7


def test_most_common_non_ascii_char():
    """Testing that function returns most common non-ASCII char from file"""
    assert get_most_common_non_ascii_char(_path_to("sample01_task01.txt")) == "ä"
