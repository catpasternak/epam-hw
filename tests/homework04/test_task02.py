from unittest.mock import MagicMock

import pytest

import homework04
from homework04.task02 import count_dots_on_i


@pytest.fixture()
def mock_url(monkeypatch):
    mock = MagicMock()
    mock.return_value.read.return_value = "<title>Hi!</title>".encode("utf-8")
    monkeypatch.setattr(homework04.task02, "urlopen", mock)


def test_i_count(mock_url):
    """Testing number of i is correct and test uses mocked url instead of real"""
    assert count_dots_on_i("http://sample.com") == 3
