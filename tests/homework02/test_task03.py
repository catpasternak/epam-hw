from homework02.task03 import combinations


def test_all_possible_combinations_of_elements_among_given_lists():
    """Testing that function returns all possible combinations of elements in given lists
    so that only one element from each list should be present in any combination"""
    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]
