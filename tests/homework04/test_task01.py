import os

import pytest

from homework04.task01 import read_magic_number


@pytest.fixture
def create_file_1(tmpdir):
    f = tmpdir.join("myfile.txt")
    f.write("2.5")
    yield f
    os.remove(f)


def test_read_magic_number_for_positive_case(create_file_1):
    """Testing that if file contains number on 1st line and it is in interval - function returns True"""
    f1 = create_file_1
    assert read_magic_number(f1)


@pytest.fixture
def create_file_2(tmpdir):
    f = tmpdir.join("myfile.txt")
    f.write("5")
    yield f
    os.remove(f)


def test_read_magic_number_for_negative_case(create_file_2):
    """Testing that if file contains number on 1st line and it is not in interval - function returns False"""
    f2 = create_file_2
    assert not read_magic_number(f2)


@pytest.fixture
def create_file_3(tmpdir):
    f = tmpdir.join("myfile.txt")
    f.write("Hollywood")
    yield f
    os.remove(f)


def test_valueerror_exception_case(create_file_3):
    """Testing that if file contains other type than int or float - function raises ValueError"""
    f3 = create_file_3
    with pytest.raises(ValueError):
        read_magic_number(f3)


def test_filenotfounderror_exception_case():
    """Testing that when file doesn't exists - ValueError raised"""
    with pytest.raises(ValueError):
        read_magic_number(os.path.join(os.path.dirname(__file__), "missing.txt"))
