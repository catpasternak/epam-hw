"""In previous homework task 4, you wrote a cache function that remembers other function output value. Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass

Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ') # careful with input() in python2, use raw_input()
   
   f()
? 1
'1'
   f()     # will remember previous value
'1'
   f()     #  but use it up to two times only
'1'
   f()
? 2
'2'"""


def cache(times=3):
    """Saves function result with unique arguments to cache and keeps it there for given number of calls"""

    def decorator(func):
        memorized = {}

        def wrapper(*args, **kwargs):
            arguments = tuple(args) + tuple(kwargs.items())
            if arguments not in memorized:
                memorized[arguments] = [func(*args, **kwargs), times]
                return memorized[arguments][0]
            else:
                output = memorized[arguments][0]
                memorized[arguments][1] -= 1
                if memorized[arguments][1] == 0:
                    del memorized[arguments]
                return output

        return wrapper

    return decorator
