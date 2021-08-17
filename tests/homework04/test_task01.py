import os
import tempfile

import pytest

from homework04.task01 import read_magic_number


def create_file(with_content):
    """Parametrized decorator that creates temporary file, writes content to it,
    passes created file to function and removes the file afterwards.
    """

    def decorate(func):
        def wrapper(*args, **kwargs):
            fd, path = tempfile.mkstemp()
            os.write(fd, with_content)
            os.close(fd)
            try:
                return func(path, *args, **kwargs)
            finally:
                if os.path.exists(path):
                    os.unlink(path)

        return wrapper

    return decorate


@create_file(with_content=b"2.5")
def test_read_magic_number_for_positive_case(temp_filename):
    """Testing that if file contains number on 1st line and it is in interval - function returns True"""
    assert read_magic_number(temp_filename)


@create_file(with_content=b"5")
def test_read_magic_number_for_negative_case(temp_filename):
    """Testing that if file contains number on 1st line and it is not in interval - function returns False"""
    assert not read_magic_number(temp_filename)


@create_file(with_content=b"Hollywood")
def test_valueerror_exception_case(temp_filename):
    """Testing that if file contains other type than int or float - function raises ValueError"""
    with pytest.raises(ValueError):
        read_magic_number(temp_filename)


def test_filenotfounderror_exception_case():
    """Testing that when file doesn't exists - ValueError raised"""
    with pytest.raises(ValueError):
        read_magic_number(os.path.join(os.path.dirname(__file__), "missing.txt"))
