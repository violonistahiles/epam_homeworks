import time
from urllib.error import URLError
from urllib.request import urlopen

import aiohttp


class URLReader:
    """Perform operations with network requests"""
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.attempts = 3

    def read_url(self, url: str) -> bytes:
        for i in range(self.attempts):
            try:
                url_response = urlopen(url).read()
                return url_response
            except URLError:
                time.sleep(1)

        raise ValueError(f'Unreachable {url}')

    @staticmethod
    def decode_url(url_response: bytes, encoding: str = 'utf-8') -> str:
        return url_response.decode(encoding)

    def get_page_sinc(self, url: str, encoding: str = 'utf-8') -> str:
        url_data = self.read_url(url)
        url_str = self.decode_url(url_data, encoding)
        return url_str

    async def get_page(self, url, encoding: str = 'utf-8'):

        for i in range(self.attempts):
            async with self.session.get(url) as response:
                if response.status != 200:
                    time.sleep(1)
                    continue
                url_str = await response.text(encoding=encoding)
                return url_str

        raise ValueError(f'Unreachable {url}')
