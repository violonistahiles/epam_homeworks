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

    def get_page(self, url: str, encoding: str = 'utf-8') -> str:
        url_data = self.read_url(url)
        url_str = self.decode_url(url_data, encoding)
        return url_str
