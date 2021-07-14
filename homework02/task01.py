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
from collections import defaultdict
from typing import List


def tokenize(input_file):
    """Yields whole words and single punctuation chars"""
    token_buffer = ""
    dash_flag = 0
    while char := input_file.read(1):
        category = unicodedata.category(char)
        if category in ("Ll", "Lo", "Lt", "Lu"):
            dash_flag = 0
            token_buffer += char
        elif category in ("Pc", "Pe", "Pf", "Pi", "Po", "Ps"):
            dash_flag = 0
            if token_buffer:
                yield (token_buffer, "word")
                token_buffer = ""
                yield (char, "punc")
        elif category == "Pd":
            if token_buffer:
                if not dash_flag:
                    dash_flag = 1
                else:
                    dash_flag = 0
                    yield (token_buffer, "word")
                    token_buffer = ""
            yield (char, "punc")
        elif category in ("Cc", "Zl", "Zp", "Zs"):
            if not dash_flag:
                yield (token_buffer, "word")
                token_buffer = ""
        else:
            dash_flag = 0
            if token_buffer:
                yield (token_buffer, "word")
                token_buffer = ""


def all_results(file_path, encoding="utf-8"):

    input_file = open(file_path, encoding=encoding)

    punc_counter = 0
    top_10 = ["" for _ in range(10)]
    chars_freq = defaultdict(int)
    non_ascii_count = 0
    non_ascii_freq = defaultdict(int)

    for token in tokenize(input_file):
        if token[1] == "punc":
            punc_counter += 1
            chars_freq[token[0]] += 1
            if ord(token[0]) > 127:
                non_ascii_count += 1
                non_ascii_freq[token[0]] += 1
        else:
            top_10.append(token[0])
            top_10 = sorted(top_10, key=lambda x: len(set(x.lower())), reverse=True)[
                :10
            ]
            for char in token[0]:
                chars_freq[char.lower()] += 1
                if ord(char) > 127:
                    non_ascii_count += 1
                    non_ascii_freq[char] += 1

    input_file.close()

    chars_sorted = sorted(list(chars_freq.keys()), key=lambda x: chars_freq.get(x))
    rarest_char = chars_sorted[0]
    sorted_chars = sorted(
        list(non_ascii_freq.keys()), key=lambda x: non_ascii_freq.get(x)
    )
    common_non_ascii = sorted_chars[-1]
    return top_10, rarest_char, punc_counter, non_ascii_count, common_non_ascii


"""
Below is previous version of solution without tokenization:
"""


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
