from homework11.task01 import SimplifiedEnum


def test_class_attributes():
    """Tests that values from `__keys` class variable are accessible by respective attributes names."""

    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.ORANGE == "ORANGE"
