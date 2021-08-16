from homework02.task02 import major_and_minor_elem


def test_most_frequent_and_rarest_elements_in_list():
    """Testing that function returns most common and least common elements from given list"""
    assert major_and_minor_elem([1, 2, 3, 4, 2, 2, 4, 1, 2]) == (2, 3)
