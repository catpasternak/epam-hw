import os
from tempfile import NamedTemporaryFile

from homework09.task03 import universal_file_counter

dir_path = os.path.dirname(__file__)


class TempFiles:
    """Context manager that creates temporary files with content.
    :param num_of_files: Number of files to create
    :type num_of_files: int
    :param contents: List of content for each file, must match number of files
    :type contents: List[bytes]
    :param extensions: List of extensions to assign to files. Must include "."!!!
    :type extensions: List[str]
    """

    def __init__(self, num_of_files=1, contents=[], extensions=[]):
        """Constructor method."""
        self.num_of_files = num_of_files
        self.contents = contents
        self.extensions = extensions

    def __enter__(self):
        """Enter method. Creates temporary files with given contents and extensions."""
        self.paths = []
        for num in range(self.num_of_files):
            temp = NamedTemporaryFile(
                suffix=self.extensions[num], dir=dir_path, delete=False
            )
            self.paths.append(temp.name)
            temp.write(self.contents[num])
            temp.seek(0)

    def __exit__(self, exc_type, exc_value, traceback):
        """Exit method. Removes temporary files."""
        for path in self.paths:
            if os.path.exists(path):
                os.unlink(path)


test_contents = [b"1\n2\n3\n", b"4\n5\n", b"6 7 8 9 10\n", b"7\n", b"8\n"]
test_extensions = [".txt", ".txt", ".txt", ".py", ".py"]
number_of_files = len(test_extensions)


def test_counter_with_tokenizer_to_None():
    """Tests that function counts lines in all files with given extension in given directory."""
    with TempFiles(number_of_files, test_contents, test_extensions):
        assert universal_file_counter(dir_path, ".txt") == 6


def test_counter_with_tokenizer_to_strsplit():
    """Tests that function counts tokens in all files with given extension in given directory."""
    with TempFiles(number_of_files, test_contents, test_extensions):
        assert universal_file_counter(dir_path, ".txt", str.split) == 10
