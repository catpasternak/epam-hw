import os
import tempfile
from collections.abc import Generator

from homework09.task01 import merge_sorted_files


def create_temp_files(with_content=[]):
    """Parametrized decorator that creates several temporary files with given content.
    :param with_content: list of byte strings (contain only digits), 1 string for 1 line in file
    :type with_content: List[bytes]
    :return: decorated function that takes temporary files as extra arguments
    :rtype: Callable
    """

    def decorate(func):
        def wrapper(*args, **kwargs):
            files = []
            for i in range(len(with_content)):
                fd, path = tempfile.mkstemp()
                os.write(fd, with_content[i])
                os.close(fd)
                files.append(path)
            try:
                return func(files, *args, **kwargs)
            finally:
                for path in files:
                    if os.path.exists(path):
                        os.unlink(path)

        return wrapper

    return decorate


test_content = [b"1\n4\n7\n8\n", b"2\n3\n", b"5\n6\n9\n", b"10\n", b""]


@create_temp_files(with_content=test_content)
def test_files_merging(temp_files):
    """Test that integerst from files merge in ascending order and function is generator"""
    function_output = merge_sorted_files(temp_files)
    assert list(function_output) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert isinstance(function_output, Generator)
