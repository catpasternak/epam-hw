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


class CustomRange:
    """Functor class, when called returns sequence from start (inclusive) to stop (exclusive)
    by step. Acts like :class:'range', but takes any iterable of unique values, not only int.
    CustomRange()(iterable, stop) -> iterable[:stop]
    CustomRange()(iterable, start, stop) -> iterable[start:stop]
    CustomRange()(iterable, start, stop, step) -> iterable[start:stop:step]
    """

    def process_args(self, iterable, *args):
        """Returns start and step elements from given iterable as well as step for iteration.
        :param iterable: iterable of unique elements
        :param args: start(optional), stop and step(optional) variables to slice from iterable
        :return: start and stop elements from iterable, step for picking elements from iterable
        """
        if len(args) == 1:
            start, stop, step = 0, iterable.index(args[0]), 1
        if len(args) == 2:
            start, stop, step = iterable.index(args[0]), iterable.index(args[1]), 1
        if len(args) == 3:
            start, stop, step = (
                iterable.index(args[0]),
                iterable.index(args[1]),
                args[2],
            )
        if len(args) < 1 or len(args) > 3:
            raise TypeError("Function takes 2 to 4 arguments!")
        return start, stop, step

    def __call__(self, iterable, *args):
        """Call method, produces new sequence from given iterable.
        :param iterable: iterable of unique elements
        :param args: start(optional), stop and step(optional) variables to slice from iterable
        :return: sequence containing elements from given iterable
        :rtype: List[Any]
        """
        start, stop, step = self.process_args(iterable, *args)
        new_seq = iterable[start:stop:step]
        if not isinstance(new_seq, list):
            new_seq = [elem for elem in new_seq]
        return new_seq


custom_range = CustomRange()
