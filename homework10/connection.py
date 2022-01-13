import time

import aiohttp


class URLReader:
    """Perform operations with network requests"""
    def __init__(self):
        """
        Create service class for URL requests
        """
        self.session = aiohttp.ClientSession()
        self._attempts = 3  # Number of attempts to repeat request

    async def get_page(self, url: str, encoding: str = 'utf-8') -> str:
        """
        Create GET request to the URL

        :param url: URL
        :type url: str
        :param encoding: Codec to encode received data
        :type encoding: str
        :return: HTML in string format from requested URL
        :rtype: str
        """
        sleep_dilation_sec = 1
        for i in range(self._attempts):
            async with self.session.get(url) as response:
                if response.status != 200:
                    time.sleep(sleep_dilation_sec)
                    continue
                url_str = await response.text(encoding=encoding)
                return url_str

        raise ValueError(f'Unreachable {url}')
