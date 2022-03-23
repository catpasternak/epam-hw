import os

import pytest

from homework08.task02 import TableData


def _path_to(filename):
    return os.path.join(os.path.dirname(__file__), filename)


@pytest.fixture
def presidents():
    """Creates :class:'TableData' object.
    :return: :class:'TableData' instance
    """
    presidents = TableData(_path_to("example.sqlite"), "presidents")
    return presidents


def test_collections_methods(presidents):
    """Tests that class methods __len__, __getattr__, __getitem__ return values from source table.
    :param presidents: table 'presidents' from example database
    """
    assert len(presidents) == 3
    assert presidents["Yeltsin"] == [("Yeltsin", 999, "Russia")]
    assert "Yeltsin" in presidents


def test_iteration(presidents):
    """Tests that __iter__ method returns rows from table.
    :param presidents: table 'presidents' from example database
    """
    assert [pr["name"] for pr in presidents] == ["Yeltsin", "Trump", "Big Man Tyrone"]
