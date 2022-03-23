from homework05.task02 import custom_sum


def test_attr_decorator():
    """Testing that attributes of original function are returned"""
    assert custom_sum.__doc__ == "This function can sum any objects which have __add__"
    assert custom_sum.__name__ == "custom_sum"
    assert custom_sum.__original_func.__eq__(custom_sum)
