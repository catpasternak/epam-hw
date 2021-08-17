import pytest

from homework09.task02 import SuppressManager, suppressor

testdata = [(IndexError, IndexError), (Exception, KeyError)]


@pytest.mark.parametrize("exc_to_suppress, exc_to_raise", testdata)
def test_positive_with_suppressor_class(exc_to_suppress, exc_to_raise):
    """Tests that exception passed as parameter to context manager is suppressed if raised."""
    with SuppressManager(exc_to_suppress):
        raise exc_to_raise
    assert True


def test_negative_with_suppressor_class():
    """Tests that exception other than one passed as parameter - is not suppressed."""
    with pytest.raises(IndexError):
        with SuppressManager(TypeError):
            raise IndexError


@pytest.mark.parametrize("exc_to_suppress, exc_to_raise", testdata)
def test_positive_with_suppressor_generator(exc_to_suppress, exc_to_raise):
    """Tests that exception passed as parameter to context manager is suppressed if raised."""
    with suppressor(exc_to_suppress):
        raise exc_to_raise
    assert True


def test_negative_with_suppressor_generator():
    """Tests that exception other than one passed as parameter - is not suppressed."""
    with pytest.raises(IndexError):
        with suppressor(TypeError):
            raise IndexError


def text_expression_inside_with_statement_executed():
    """Test that expression in with statement gets executed when error is raised and suppressed."""
    with suppressor(IndexError):
        lst = [1, 2, 3]
        summa = sum(lst[i] for i in range(7))
    assert summa == 6
