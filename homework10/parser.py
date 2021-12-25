import os
import re
from queue import Queue

import toml
from bs4 import BeautifulSoup
from connection import URLReader


class CompaniesParser:
    def __init__(self, site: str):
        """
        Create parser for information about S&P 500 stocks from the site
        'https://markets.businessinsider.com'

        :param site: Link to the initial site page
        :type site: str
        """
        self.site = site
        self.companies_links = Queue(500)
        self.companies = dict()
        self.pages_list = set()

    @staticmethod
    def _parse_company_code(company_href: str) -> str:
        """
        Get company code from company link
        Link example:
        '/stocks/aos-stock', where aos is company code

        :param company_href: Company link
        :type company_href: str
        :return: Code of the company
        :rtype: str
        """
        start_position = company_href.rfind('/') + 1
        end_position = company_href.rfind('-')
        company_code = company_href[start_position:end_position]
        return company_code

    def _parse_pages_number(self, url_str: str):
        """
        Parsing links for pages with companies lists
        Element to find example:
        '<a href="?p=4">4</a>', where ?p=4 is link
        for 4-th page with companies list

        :param url_str: String representation of html page
        :type url_str: str
        """
        soup = BeautifulSoup(url_str, 'html.parser')

        for element in soup.find_all("a", href=re.compile(r"^\?p")):
            href_name = element.get('href')
            self.pages_list.add(href_name)
        # Subtract page number 1 from pages to visit list
        self.pages_list = self.pages_list - set('?p=1')

    def _parse_company(self, element: BeautifulSoup):
        """
        Parse information about single company from table

        :param element: HTML information of company element
        :type element: BeautifulSoup
        """
        href_name = element.get('href')
        self.companies_links.put(self.site + href_name)

        company_name = element.get('title')
        company_code = self._parse_company_code(href_name)
        self.companies[company_name] = {'code': company_code}

    def _parse_companies(self, url_str: str):
        """
        Parsing company information from companies list
        Element to find example:
        <a href="/stocks/aos-stock" title="A.O. Smith">A.O. Smith</a>

        :param url_str: String representation of html page
        :type url_str: str
        """
        soup = BeautifulSoup(url_str, 'html.parser')
        table = soup.find("tbody", class_='table__tbody')

        for element in table.find_all("a",
                                      href=re.compile(r"^/stocks.*stock$")):

            self._parse_company(element)


if __name__ == '__main__':

    current_path = os.path.abspath(os.getcwd())
    current_path = os.path.join(current_path, 'homework10')
    commands_file = os.path.join(current_path, 'links.toml')
    with open(commands_file, 'r') as fi:
        commands = toml.load(fi)

    client = URLReader()
    parser = CompaniesParser(commands['INITIAL_LINK'])
    url_data = client.read_url(commands['PARSE_FIRST_PAGE'])
    url_str = client.decode_url(url_data)
    parser._parse_pages_number(url_str)
    print(parser.pages_list)

    parser._parse_companies(url_str)
    print(parser.companies_links)
    print(parser.companies)
    print(len(parser.companies))
