"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6
"""
import os
import re


def tokenize_by_lines(file_input):
    """Generator that yields lines from file."""
    while line := file_input.readline():
        yield line
        line = ""


def universal_file_counter(dir_path, file_extension, tokenizer=None):
    """Counts number of lines in files in given directory with given extension.
    If tokenizer parameter not None - will count tokens instead of lines.
    - Gets files with given extension;
    :param dir_path: Path to directory with files
    :type path: Path
    :param file_extension: Extension of files that function takes into accout
    :type file_extension: str
    :param tokenizer: Optional. Function that returns tokens from file content
    :type tokenizer: Optional[Callable]
    :return: number of lines or tokens in files with given extension
    :rtype: int
    """
    counter = 0
    re_extension = "." + file_extension + "$"
    filenames = (
        os.path.join(dir_path, fi)
        for fi in os.listdir(dir_path)
        if re.search(re_extension, fi)
    )
    for fi in filenames:
        with open(fi) as file_input:
            for line in tokenize_by_lines(file_input):
                if tokenizer:
                    for token in tokenizer(line):
                        counter += 1
                else:
                    counter += 1
    return counter
