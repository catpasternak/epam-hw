"""
Given a dictionary (tree), that contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from collections.abc import Collection, Mapping
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """Counts occurrences of given element in given dictionary.
    :param tree: dictionary where to search for element
    :type tree: dict
    :param element: element to search for
    :type element: Any
    :return: number of occurrences of element
    :rtype: int
    """
    counter = sum([tree == element])
    if isinstance(tree, Collection) and not isinstance(tree, (Mapping, str)):
        for node in tree:
            counter += find_occurrences(node, element)
    if isinstance(tree, Mapping):
        for key, value in tree.items():
            counter += sum([key == element])
            counter += find_occurrences(value, element)
    return counter
