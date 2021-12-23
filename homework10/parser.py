import os
import re
from urllib.error import URLError
from urllib.request import urlopen

import toml
from bs4 import BeautifulSoup


def parse_page(url):
    """
    Parse web page by specified url

    :param url: url address
    :type url: str
    """
    pass


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


if __name__ == '__main__':

    current_path = os.path.abspath(os.getcwd())
    dir_path = os.path.join(current_path, 'homework10')
    commands_file = os.path.join(dir_path, 'links.toml')
    with open(commands_file, 'r') as fi:
        commands = toml.load(fi)

    client = URLReader()
    url_data = client.read_url(commands['PARSING_SITE'])
    url_str = client.decode_url(url_data)
    soup = BeautifulSoup(url_str, 'html.parser')

    pages_list = []
    for element in soup.find_all("a", href=re.compile(r"^\?p")):
        # print(element.contents)
        href_name = element.get('href')
        page_number = re.findall(r'\d+', href_name)[0]
        pages_list.append(int(page_number))

    print(max(pages_list))
