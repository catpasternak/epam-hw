"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from itertools import chain, cycle
from typing import Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    fizz = cycle(chain((None for _ in range(2)), ("fizz",)))
    buzz = cycle(chain((None for _ in range(4)), ("buzz",)))
    fizzbuzz = cycle(chain((None for _ in range(14)), ("fizzbuzz",)))
    nums = (num for num in range(1, n + 1))

    def find_first_true(tup):
        yield next(elem for elem in tup if elem)

    yield (find_first_true(tup) for tup in zip(fizzbuzz, fizz, buzz, nums))
