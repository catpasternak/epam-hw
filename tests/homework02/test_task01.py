import os

from homework02 import task01


def _path_to(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def test_longest_diverse_words():
    """Testing that function returns 10 words with biggest amount of unique symbols in it"""
    assert task01.get_longest_diverse_words(
        _path_to("sample01_task01.txt"), encoding="unicode-escape"
    ) == [
        "vorzutäuschen",
        "Fruchtbarkeit",
        "herabgesunken",
        "ungeschwächt",
        "Bürokraten",
        "Rotwelsch",
        "Oberfläche",
        "brunnenführende",
        "Technikern",
        "versucht",
    ]


def test_rarest_char():
    """Testing that least common char in given file is returned"""
    assert (
        task01.get_rarest_char(
            _path_to("sample01_task01.txt"), encoding="unicode-escape"
        )
        == "j"
    )


def test_punctuation_chars_count():
    """Testing that function counts every punctuation char in file"""
    assert (
        task01.count_punctuation_chars(
            _path_to("sample01_task01.txt"), encoding="unicode-escape"
        )
        == 12
    )


def test_non_ascii_chars_count():
    """Testing that function counts every non-ASCII char in given file"""
    assert (
        task01.count_non_ascii_chars(
            _path_to("sample01_task01.txt"), encoding="unicode-escape"
        )
        == 7
    )


def test_most_common_non_ascii_char():
    """Testing that function returns most common non-ASCII char from file"""
    assert (
        task01.get_most_common_non_ascii_char(
            _path_to("sample01_task01.txt"), encoding="unicode-escape"
        )
        == "ä"
    )
