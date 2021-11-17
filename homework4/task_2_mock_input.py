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


>>> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
from urllib.request import urlopen


def count_dots_on_i(url: str) -> int:
    """
    Return number of "i" characters in html code of url
    """
    try:
        url_response = urlopen(url).read()
    except Exception:
        raise ValueError(f'Unreachable {url}')

    html_string = url_response.decode('utf-8')
    return html_string.count('i')


if __name__ == '__main__':
    test_url = 'http://www.python.org'
    i_count = count_dots_on_i(test_url)
    print(i_count)
