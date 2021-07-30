import sys
from contextlib import ContextDecorator
from unittest.mock import patch

from homework04.task02 import count_dots_on_i


class FakeResponse:
    """Mocking service class"""

    def __init__(self, *args):
        pass

    def get_data(self):
        return "iii"


def test_i_count():
    """Testing business logic, service class for retrieving data from url mocked"""
    with patch("homework04.task02.UrlResponse") as mock_request:
        mock_request.return_value = FakeResponse()
        assert count_dots_on_i("http://example.com") == 3


class MyPatch(ContextDecorator):
    """Acts as a decorator or context manager. Inside the body of the function
    or with statement, the target is patched with a new object. When the function/
    with statement exits - the patch is undone.
    :param path_to_obj: name of class that should be mocked
    :type path_to_obj: str
    :param mock_obj: mock object
    :type mock_obj: type
    """

    def __init__(self, path_to_obj, mock_obj):
        self.path_to_obj = path_to_obj
        self.mock_obj = mock_obj

    def __enter__(self):
        """Return value is bound to variable after 'as' in with statement."""
        modules = self.path_to_obj.split(".")
        self.current_module = sys.modules[modules[0]]
        for next_module in modules[1:-1]:
            self.current_module = getattr(self.current_module, next_module)
        self.obj_name = modules[-1]
        self.original_obj = getattr(self.current_module, self.obj_name)
        setattr(self.current_module, self.obj_name, self.mock_obj)
        return self.mock_obj

    def __exit__(self, *args, **kwargs):
        setattr(self.current_module, self.obj_name, self.original_obj)


def test_i_count_with_MyPatch_context_manager():
    with MyPatch("homework04.task02.UrlResponse", FakeResponse):
        assert count_dots_on_i("http://example.com") == 3


@MyPatch("homework04.task02.UrlResponse", FakeResponse)
def test_i_count_with_MyPatch_decorator():
    assert count_dots_on_i("http://example.com") == 3
