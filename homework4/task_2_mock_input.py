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


# >>> count_dots_on_i("https://example.com/")
# 59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
from urllib.error import URLError
from urllib.request import urlopen


class URLReader:
    """Perform operations with network requests"""
    @staticmethod
    def read_url(url: str) -> bytes:
        try:
            url_response = urlopen(url).read()
        except URLError:
            raise ValueError(f'Unreachable {url}')

        return url_response

    @staticmethod
    def decode_url(url_response: bytes, encoding: str = 'utf-8') -> str:
        return url_response.decode(encoding)


def count_dots_on_i(url: str) -> int:
    """Return number of "i" characters in html code of url"""
    client = URLReader()
    url_response = client.read_url(url)
    html_string = client.decode_url(url_response)

    return html_string.count('i')


if __name__ == '__main__':
    test_url = 'https://example.com/'
    i_count = count_dots_on_i(test_url)
    print(i_count)
