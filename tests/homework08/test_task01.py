from unittest.mock import patch

import pytest

from homework08.task01 import KeyValueStorage


class FakeReader:
    """Class to mock :class:'FileReader.
    :param content: data that mocks data from file
    :type content: list[str]
    """

    def __init__(self, content):
        """Constructor method."""
        self.content = content

    def read_lines(self):
        """Simply returns content attribute
        :return: data to mock file content
        :rtype: list[str]
        """
        return self.content


@pytest.fixture
def test_content():
    return [
        "name=kek\n",
        "last_name=top\n",
        "power=9001\n",
        "song=shadilay\n",
        "__doc__=not_this_doc\n",
    ]


def test_class_attributes(test_content):
    """Tests that keys and value accessible both as attributes and collection items
    :param test_content: data to mock file content
    """
    with patch("homework08.task01.FileReader") as mock_obj:
        mock_obj.return_value = FakeReader(content=test_content)
        storage = KeyValueStorage("somefile")
        assert storage.name == "kek"
        assert storage.power == 9001
        assert storage["song"] == "shadilay"


def test_built_in_attributes(test_content):
    """Tests that built-in attributes are not overwritten.
    :param test_content: data to mock file content
    """
    with patch("homework08.task01.FileReader") as mock_obj:
        mock_obj.return_value = FakeReader(content=test_content)
        storage = KeyValueStorage("somefile")
        assert not storage.__doc__ == "not_this_doc"


def test_error_raised_with_impossible_keys():
    """Tests that error is raised in case of key that is not valid identifier in Python
    :raises ValueError: when key is not valid identifier
    """
    with patch("homework08.task01.FileReader") as mock:
        mock.return_value = FakeReader(content=["1=value"])
        with pytest.raises(ValueError):
            storage = KeyValueStorage("somefile")
