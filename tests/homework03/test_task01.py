from homework03.task01 import cache


def test_cache_with_parameter_is_working():
    """Testing that parametrized decorator keeps in cache given number of results"""
    times_called = 0

    @cache(times=1)
    def f():
        nonlocal times_called
        times_called += 1
        return 1

    assert f() == 1
    assert times_called == 1

    assert f() == 1
    assert times_called == 1

    assert f() == 1
    assert times_called == 2
