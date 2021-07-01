"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(iterable, *args):
    """Acts line range function on any given iterable"""
    if len(args) == 1:
        start = 0
        stop = iterable.index(args[0])
        step = 1
    if len(args) == 2:
        start = iterable.index(args[0])
        stop = iterable.index(args[1])
        step = 1
    if len(args) == 3:
        start = iterable.index(args[0])
        stop = iterable.index(args[1])
        step = args[2]
    new_seq = iterable[start:stop:step]
    if not isinstance(new_seq, list):
        new_list = [elem for elem in new_seq]
        return new_list
    return new_seq
