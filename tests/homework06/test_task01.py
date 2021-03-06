import pytest

from homework06.task01 import instances_counter


@instances_counter
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, dist_x, dist_y):
        return ((self.x - dist_x) ** 2 + (self.y - dist_y) ** 2) ** 0.5


def test_decorator_with_and_without_instances():
    """Testing that decorator sets counter to zero when no instances exist
    and counts class instances correctly.
    """
    assert Point.get_created_instances() == 0
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


def test_with_inheritance():
    """Tests that counter does not count child class instances and child class with different
    number of args works correctly.
    """
    Point.reset_instances_counter()

    class ChildPoint(Point):
        def __init__(self, x, y, z):
            self.x, self.y, self.z = x, y, z

    child_inst_1, child_inst_2 = ChildPoint(1, 1, 1), ChildPoint(2, 2, 2)
    assert Point.get_created_instances() == 0


def test_child_class_counter():
    """Tests that child class counter works correctly"""

    class ChildPoint2(Point):
        pass

    child_inst_1, child_inst_2 = ChildPoint2(1, 1), ChildPoint2(2, 2)
    assert ChildPoint2.get_created_instances() == 2
