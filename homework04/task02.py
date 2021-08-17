"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection
You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests
>> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
from urllib.request import urlopen


class UrlResponse:
    """Service class that extracts data fron url.
    :param url: url where we get source data from
    :type url: str
    """

    def __init__(self, url):
        self.url = url

    def get_data(self):
        try:
            response = urlopen(self.url)
        except Exception:
            raise ValueError("Unreachable {url}")
        return response.read().decode()


def count_dots_on_i(url: str) -> int:
    """Processing data according to business logic"""
    data = UrlResponse(url)
    content = data.get_data()
    return content.count("i")
