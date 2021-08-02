import pytest

from homework07.task01 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "key2": ["RED", ["RED", "BLUE"]],
        "complex_key": {
            "key1": "value1",
            "key2": ["RED", "BLUE"],
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": ["RED", {"nested_key": "RED"}],
}

testdata = [("RED", 8), ("key2", 2), (["RED", "BLUE"], 3), ({"nested_key": "RED"}, 2)]


@pytest.mark.parametrize("elem, expected", testdata)
def test_element_occurrences_counter(elem, expected):
    """Tests that function returns correct number of occurences for different types of elements"""
    assert find_occurrences(example_tree, elem) == expected
