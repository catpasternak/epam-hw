"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import unicodedata
from collections import defaultdict


def by_word(input_file):
    """Yields whole words from file"""
    token_buffer = ""
    dash_flag = 0
    while char := input_file.read(1):
        category = unicodedata.category(char)
        if category[0] == "L":
            dash_flag = 0
            token_buffer += char
        elif category[0] == "P" and category != "Pd":
            dash_flag = 0
            if token_buffer:
                yield token_buffer
                token_buffer = ""
        elif category == "Pd":
            if token_buffer:
                if not dash_flag:
                    dash_flag = 1
                else:
                    dash_flag = 0
                    yield token_buffer
                    token_buffer = ""
        elif category[0] in ("C", "Z"):
            if token_buffer and not dash_flag:
                yield token_buffer
                token_buffer = ""
        else:
            dash_flag = 0
            if token_buffer:
                yield token_buffer
                token_buffer = ""


def by_symbol(input_file):
    """Yields tuples containing symbol and its category: letter or punctuation."""
    while char := input_file.read(1):
        category = unicodedata.category(char)
        if category[0] == "L":
            yield char, "letter"
        if category[0] == "P":
            yield char, "punctuation"


def custom_open(file_path, encoding="utf-8", tokenize=by_word):
    """Yields from file by wors or by char accoding to chosen tokenize function."""
    with open(file_path, encoding=encoding) as input_file:
        yield from tokenize(input_file)


def get_longest_diverse_words(file_path, encoding="utf-8"):
    """Finds 10 words with maximum number of diverse characters."""
    top_10 = ["" for _ in range(10)]
    for elem in custom_open(file_path, encoding=encoding, tokenize=by_word):
        top_10.append(elem)
        top_10 = sorted(top_10, key=lambda x: len(set(x.lower())), reverse=True)[:10]
    return top_10


def get_rarest_char(file_path, encoding="utf-8"):
    """Finds least common character in file."""
    chars_freq = defaultdict(int)
    for elem in custom_open(file_path, encoding=encoding, tokenize=by_symbol):
        chars_freq[elem[0].lower()] += 1
    sorted_chars = sorted(chars_freq.keys(), key=lambda x: chars_freq.get(x))
    return sorted_chars[0]


def count_punctuation_chars(file_path, encoding="utf-8"):
    """Counts punctuation chars in file."""
    counter = 0
    for elem in custom_open(file_path, encoding=encoding, tokenize=by_symbol):
        if elem[1] == "punctuation":
            counter += 1
    return counter


def count_non_ascii_chars(file_path, encoding="utf-8"):
    """Counts non-ASCII characters from file."""
    counter = 0
    for elem in custom_open(file_path, encoding=encoding, tokenize=by_symbol):
        if not elem[0].isascii():
            counter += 1
    return counter


def get_most_common_non_ascii_char(file_path, encoding="utf-8"):
    """Finds most common non-ASCII character from file."""
    frequencies = defaultdict(int)
    for elem in custom_open(file_path, encoding=encoding, tokenize=by_symbol):
        if not elem[0].isascii():
            frequencies[elem[0].lower()] += 1
    sorted_freq = sorted(frequencies.keys(), key=lambda x: frequencies.get(x))
    return sorted_freq[-1]
