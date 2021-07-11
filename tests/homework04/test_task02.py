from unittest.mock import patch

from homework04.task02 import count_dots_on_i


class FakeResponse:
    """Mocking service class"""

    def __init__(self, content):
        self.content = content

    def get_data(self):
        return self.content


def test_i_count():
    """Testing business logic, service class for retrieving data from url mocked"""
    with patch("homework04.task02.UrlResponse") as mock_request:
        mock_request.return_value = FakeResponse(content="<title>Hi!</title>")
        assert count_dots_on_i("http://example.com") == 3
