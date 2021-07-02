from homework03.task03 import make_filter


def test_filter_object_created_with_function_delivers_correctly():
    """Testing that filter object with its method apply() returns only appropriate elements of given data"""
    sample_data = [
        {"name": "John", "age": 3, "color": "blue"},
        {"name": "Jane", "age": 5, "color": "red"},
    ]

    assert make_filter(name="Jane", age=5).apply(sample_data) == [
        {"name": "Jane", "age": 5, "color": "red"}
    ]


def test_filter_returns_empty_when_one_parameter_is_not_present_in_source_data():
    """Testing that filter object with its method apply() returns only appropriate elements of given data"""
    sample_data = [
        {"name": "John", "age": 3, "color": "blue"},
        {"name": "Jane", "age": 5, "color": "red"},
    ]

    assert make_filter(name="Jane", age=100).apply(sample_data) == []


def test_filter_returns_empty_when_key_is_not_present_in_source_data():
    """Testing that filter object with its method apply() returns only appropriate elements of given data"""
    sample_data = [
        {"name": "John", "age": 3, "color": "blue"},
        {"name": "Jane", "age": 5, "color": "red"},
    ]

    assert make_filter(gender="female").apply(sample_data) == []


def test_filter_returns_empty_when_keys_match_partially():
    """Testing that filter object with its method apply() returns None when keys don't match elements in full"""
    sample_data = [
        {"name": "John", "age": 3, "color": "blue"},
        {"name": "Jane", "age": 5, "color": "red"},
    ]

    assert make_filter(name="Jane", age=3).apply(sample_data) == []
