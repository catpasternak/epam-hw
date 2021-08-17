from homework03.task04 import is_armstrong


def test_actual_armstrong_number():
    """Testing Armstrong number is identified"""
    assert is_armstrong(153)


def test_non_armstrong_number():
    """Testing that non-Armstrong number is detected"""
    assert not is_armstrong(10)
