"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
import unicodedata
from typing import List


def get_longest_diverse_words(file_path: str, encoding="utf-8") -> List[str]:
    def remove_punc(source_word):
        """Removes punctuation chars from string"""
        word = source_word
        for char in word:
            if unicodedata.category(char)[0] != "L":
                word = word.replace(char, "")
        return word

    with open(file_path, encoding=encoding) as fi:
        words = [remove_punc(word) for line in fi for word in line.split()]
    sorted_words = sorted(words, key=lambda word: len(set(word)), reverse=True)
    return sorted_words[:10]


def get_rarest_char(file_path: str, encoding="utf-8") -> str:
    with open(file_path, encoding=encoding) as fi:
        lower_chars = [char.lower() for line in fi for char in line]
    chars_freq = {char: lower_chars.count(char) for char in set(lower_chars)}
    chars_sorted = sorted(list(chars_freq.keys()), key=lambda x: chars_freq.get(x))
    rarest = chars_sorted[0]
    return rarest


def count_punctuation_chars(file_path: str, encoding="utf-8") -> int:
    punc = string.punctuation
    with open(file_path, encoding=encoding) as fi:
        punc_chars = [char for line in fi for char in line if char in punc]
    return len(punc_chars)


def count_non_ascii_chars(file_path: str, encoding="utf-8") -> int:
    with open(file_path, encoding=encoding) as fi:
        non_ascii_chars = [char for line in fi for char in line if ord(char) > 127]
    return len(non_ascii_chars)


def get_most_common_non_ascii_char(file_path: str, encoding="utf-8") -> str:
    with open(file_path, encoding=encoding) as fi:
        non_ascii_chars = [char for line in fi for char in line if ord(char) > 127]
    non_ascii_freq = {
        char: non_ascii_chars.count(char) for char in set(non_ascii_chars)
    }
    sorted_chars = sorted(
        list(non_ascii_freq.keys()), key=lambda x: non_ascii_freq.get(x), reverse=True
    )
    return sorted_chars[0]
