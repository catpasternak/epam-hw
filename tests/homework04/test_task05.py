from homework04.task04 import fizzbuzz


def test_fizzbuzz_returns_correct_sequence():
    """Testing that elements in generator are a fizzbuzz sequence"""
    assert list(fizzbuzz(15)) == [
        1,
        2,
        "fizz",
        4,
        "buzz",
        "fizz",
        7,
        8,
        "fizz",
        "buzz",
        11,
        "fizz",
        13,
        14,
        "fizzbuzz",
    ]
