"""
"We have a file that works as key-value storage, each line is represented as key and value separated by = symbol, example:

name=kek
last_name=top
song_name=shadilay
power=9001

Values can be strings or integer numbers. If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible as collection items and as attributes.
Example:
storage['name']  # will be string 'kek'
storage.song_name  # will be 'shadilay'
storage.power  # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute (for example when there's a line `1=something`) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""
from keyword import iskeyword


class FileReader:
    """Class that reads from file and returns its content as list of lines.

    :param file_path: Path to file
    :type file_path: str
    """

    def __init__(self, file_path):
        """Constructor method."""
        self.file_path = file_path

    def read_lines(self):
        """Returns content of a file as a list of lines.
        :return: lines from file
        :rtype: list of strings
        """
        with open(self.file_path) as file_input:
            return file_input.readlines()


class KeyValueStorage:
    """Wrapper class that takes a list of lines as input
    and uses each line content as a key-value pair separated by '='.
    Resulting dictionary is used to return attributes and collection items
    of the class.

    :param file_path: Path to file that containce source data for class.
    :type file_path: str
    """

    def __init__(self, file_path):
        """Constructor method. Uses :class:'FileReader' to read content from file
        into instance variable.
        """
        self.file_path = file_path
        self.data = FileReader(file_path).read_lines()
        self.dict = self.create_dict()

    def create_dict(self):
        """Creates instance dictionary from input file data.
        :raises ValueError: Raises error in case of invalid key.
        :return: dictionary containing key-value pairs from file.
        :rtype: dict
        """
        dic = {}
        for line in self.data:
            key, value = line.rstrip().split("=")
            if not key.isidentifier() or iskeyword(key):
                raise ValueError("Key is not a valid identifier!")
            if key in self.__dir__():
                continue
            if value.isdigit():
                value = int(value)
            dic[key] = value
        return dic

    def __getattr__(self, attr):
        """Getattr method.
        :return: value from self.dict
        :rtype: str, int
        """
        return self.dict[attr]

    def __getitem__(self, item):
        """Getitem method
        :return: value from self.dict
        :rtype: str, int
        """
        return self.dict[item]
