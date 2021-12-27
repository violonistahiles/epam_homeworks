import time

import aiohttp


class URLReader:
    """Perform operations with network requests"""
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.attempts = 3

    async def get_page(self, url, encoding: str = 'utf-8'):

        for i in range(self.attempts):
            async with self.session.get(url) as response:
                if response.status != 200:
                    time.sleep(1)
                    continue
                url_str = await response.text(encoding=encoding)
                return url_str

        raise ValueError(f'Unreachable {url}')
