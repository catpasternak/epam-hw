"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    """Metaclass that passes values from class variable `__keys` as class attributes
    with respective names.
    :param cls: metaclass
    :param clsname: future class name
    :param bases: future class parent
    :param dct: future class attributes
    """

    def __new__(cls, clsname, bases, dct):
        """Constructor method."""
        if f"_{clsname}__keys" in dct:
            for item in dct[f"_{clsname}__keys"]:
                dct[item] = item
            return super().__new__(cls, clsname, bases, dct)
