from homework03.task02 import time_of_boosted_calc_50


def test_execution_time_less_than_20_seconds():
    """Testing that function using multiprocessing returns output in less than 20 sec"""
    assert time_of_boosted_calc_50() <= 20
