"""In previous homework task 4, you wrote a cache function that remembers
other function output value. Modify it to be a parametrized decorator,
so that the following code:

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
from collections import namedtuple


def cache(times=3):
    """Adds parameter to decorated function.
    :param times: number of calls with same args that has to be retrieved from cache
    :type times: int
    """

    def decorate(func):
        """Decorator function."""
        memory = []
        Call = namedtuple("Call", "args output times")

        def wrapper(*args, **kwargs):
            """Saves function result with unique arguments to cache and keeps it there for given number of calls."""
            arguments = args, kwargs.items()
            for call in memory:
                if call.args == arguments:
                    output = call.output
                    call.times[0] -= 1
                    if call.times[0] == 0:
                        memory.remove(call)
                    return output
            call = Call(args=arguments, output=func(*args, **kwargs), times=[times])
            memory.append(call)
            return call.output

        return wrapper

    return decorate
