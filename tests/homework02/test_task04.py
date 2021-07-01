from homework02.task04 import cache


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 1, 2

val_1 = cache_func(*some)
val_2 = cache_func(*some)
val_3 = cache_func(*some)


def test_func_results_come_from_cache_on_2nd_call():
    """Testing that function output was picked from cache on 2nd function call with same arguments"""
    assert val_2 is val_1


def test_func_results_come_from_cache_on_3rd_iteration():
    """Testing that function output was picked from cache on 3rd function call with same arguments"""
    assert val_3 is val_1
