"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    """Decorator that looks up function args in cache to return previuos result if exists."""
    memory = []

    def inner(*args, **kwargs):
        arguments = args, kwargs.items()
        for call in memory:
            if call[0] == arguments:
                return call[1]
        func_outcome = func(*args, **kwargs)
        call = arguments, func_outcome
        memory.append(call)
        return func_outcome

    return inner
