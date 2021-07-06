"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n):
    """Returns list of integers from 1 to given number with multiples of 3, 5 and both (3 and 5)
    replaced respectively by 'fizz', 'buzz' and 'fizzbuzz'
    >>> fizzbuzz(15)
    [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz']
    """

    def modify(num):
        new_num = ""
        if num % 3 == 0:
            new_num += "fizz"
        if num % 5 == 0:
            new_num += "buzz"
        if num % 3 != 0 and num % 5 != 0:
            new_num = num
        return new_num

    return [modify(num) for num in range(1, n + 1)]


def fizzbuzz2(n: int) -> List[str]:
    """Returns list of integers from 1 to given number with multiples of 3, 5 and both (3 and 5)
    replaced respectively by 'fizz', 'buzz' and 'fizzbuzz'
    According to timeit module - less effective algorythm...
    >>> fizzbuzz(15)
    [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz']
    """
    dic = {
        (lambda x: x % 3 != 0 and x % 5 != 0): (lambda x: x),
        (lambda x: x % 3 == 0 and x % 5 != 0): (lambda x: "fizz"),
        (lambda x: x % 3 != 0 and x % 5 == 0): (lambda x: "buzz"),
        (lambda x: x % 3 == 0 and x % 5 == 0): (lambda x: "fizzbuzz"),
    }
    return [dic[key](x) for x in range(1, n + 1) for key in dic if key(x)]
