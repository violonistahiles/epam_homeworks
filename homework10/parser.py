import os
import re
from typing import Dict, List

import toml
from bs4 import BeautifulSoup

from homework10.connection import URLReader


class CompaniesParser:
    def __init__(self, site: str):
        """
        Create parser for getting information about S&P 500 stocks
        from the site 'https://markets.businessinsider.com'

        :param site: Link to the initial site page
        :type site: str
        """
        self.site = site

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

    @staticmethod
    def parse_pages_number(page: str) -> List:
        """
        Parsing links for pages with companies lists
        Element to find example:
        '<a href="?p=4">4</a>', where ?p=4 is link
        for 4-th page with companies list

        :param page: String representation of html page
        :type page: str
        """
        soup = BeautifulSoup(page, 'html.parser')

        pages_list = set()
        for element in soup.find_all("a", href=re.compile(r"^\?p")):
            href_name = element.get('href')
            pages_list.add(href_name)
        # Subtract page number 1 from pages to visit list
        pages_list = pages_list - set('?p=1')

        return list(pages_list)

    def _parse_company(self, element: BeautifulSoup) -> Dict:
        """
        Parse information about single company from table

        :param element: HTML information of company element
        :type element: BeautifulSoup
        """
        href_name = element.get('href')
        company_link = self.site + href_name

        company_name = element.get('title')
        company_code = self._parse_company_code(href_name)
        company_dict = {company_code.upper(): {'name': company_name,
                                               'link': company_link}}

        return company_dict

    def parse_companies(self, page: str) -> Dict:
        """
        Parsing company information from companies list
        Element to find example:
        <a href="/stocks/aos-stock" title="A.O. Smith">A.O. Smith</a>

        :param page: String representation of html page
        :type page: str
        """
        soup = BeautifulSoup(page, 'html.parser')
        table = soup.find("tbody", class_='table__tbody')

        companies_dict = {}
        for element in table.find_all("a",
                                      href=re.compile(r"^/stocks.*stock$")):

            company_dict = self._parse_company(element)
            companies_dict.update(company_dict)

        return companies_dict


class CompanyParser:

    @staticmethod
    def _parse_current_value(soup):
        element = soup.find('span', class_='price-section__current-value')
        price = element.contents[0]

        return price

    @staticmethod
    def _parse_company_code(soup):
        element = soup.find('span', class_='price-section__category')
        company_code = element.find('span').contents[0]
        company_code = company_code.split()[1]

        return company_code

    def scalp_company(self, page):
        soup = BeautifulSoup(page, 'html.parser')
        price = self._parse_current_value(soup)
        company_code = self._parse_company_code(soup)
        return [company_code, price]


if __name__ == '__main__':

    current_path = os.path.abspath(os.getcwd())
    current_path = os.path.join(current_path, 'homework10')
    commands_file = os.path.join(current_path, 'links.toml')
    with open(commands_file, 'r') as fi:
        commands = toml.load(fi)

    client = URLReader()
    parser = CompaniesParser(commands['INITIAL_LINK'])
    url_data = client.read_url(commands['FIRST_PAGE_LINK'])
    url_str = client.decode_url(url_data)
    pages_list = parser.parse_pages_number(url_str)
    print(pages_list)

    companies_dict = parser.parse_companies(url_str)
    for company in companies_dict.keys():
        print(companies_dict[company])
