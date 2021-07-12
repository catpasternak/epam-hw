import pytest

from homework06.task01 import instances_counter


@instances_counter
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, dist_x, dist_y):
        return ((self.x - dist_x) ** 2 + (self.y - dist_y) ** 2) ** 0.5


def test_decorator_without_instances():
    """Testing that decorator sets counter to zero when no instances exist"""
    assert Point.get_created_instances() == 0


def test_decorator_with_instances():
    """Testing that decorator counts class instances"""
    inst_1, inst_2, inst_3 = Point(1, 1), Point(1, 2), Point(1, 3)
    assert Point.get_created_instances() == 3


def test_decorator_after_reset():
    """Testing that counter is set to zero with reset method and returns last count before that"""
    assert Point.reset_instances_counter() == 3
    assert Point.get_created_instances() == 0


def test_decorator_doesnt_change_class_attr_and_methods():
    """Testing that decorated class attrbutes and methods are not changed by decorator"""
    point = Point(3, 4)
    assert point.x == 3
    assert point.y == 4
    assert point.distance(0, 0) == pytest.approx(5.0)
