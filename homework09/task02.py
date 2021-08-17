"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


class SuppressManager:
    """Context manager that suppresses given exceptions.
    :param exception: exception type to be suppressed
    :type exception: :class:`BaseException`
    """

    def __init__(self, exception):
        """Constructor method."""
        self.exception = exception

    def __enter__(self):
        """Enter method."""
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """Exit method. Returns `True` if raised exception (if any) matches given type."""
        if issubclass(exception_type, self.exception):
            return True


@contextmanager
def suppressor(exception):
    """Context manger generator that suppresses only given exception.
    :param exception: exception type to be suppressed
    :type exception: :class:`BaseException`
    """
    try:
        yield
    except exception:
        pass
