import os
import re
from datetime import datetime, timedelta
from typing import Callable, List

import toml
from bs4 import BeautifulSoup

from homework10.connection import URLReader


class ElementNotFoundError(Exception):
    """No such element on HTML"""


def parsing_decorator(func: Callable) -> Callable:
    """
    Decorator to handling exceptions during parsing an element through html

    :param func: Parsing function
    :type func: Callable
    :return: Decorated function
    :rtype: Callable
    """
    def wrapper(*args):
        try:
            result = func(*args)
        except ElementNotFoundError:
            result = None
        return result
    return wrapper


class TableParser:
    def __init__(self, site: str):
        """
        Create parser for getting information about S&P 500 stocks
        from the site 'https://markets.businessinsider.com'

        :param site: Link to the initial site page
        :type site: str
        """
        self.site = site

    @staticmethod
    def parse_pages_number(page: str) -> List:
        """
        Parsing links for pages with companies tables
        Element to find example:
        '<a href="?p=4">4</a>', where ?p=4 is link
        for 4-th page with companies list

        :param page: String representation of html page
        :type page: str
        """
        soup = BeautifulSoup(page, 'html.parser')

        pages_number = 0
        for element in soup.find_all("a", href=re.compile(r"^\?p")):
            href_name = element.get('href')
            page_number = int(re.findall(r'\d+', href_name)[0])
            if pages_number < page_number:
                pages_number = page_number
        # Take remaining pages
        pages_list = ['?p=' + str(digit) for digit in range(2, pages_number+1)]

        return list(pages_list)

    def parse_companies(self, page: str) -> List:
        """
        Parsing company link from company html element
        Element to find example:
        <a href="/stocks/aos-stock" title="A.O. Smith">A.O. Smith</a>

        :param page: String representation of html page
        :type page: str
        """
        soup = BeautifulSoup(page, 'html.parser')
        # Find table with companies
        table = soup.find("tbody", class_='table__tbody')

        # Process table line by line
        companies_links = []
        for element in table.find_all("a",
                                      href=re.compile(r"^/stocks.*stock$")):

            company_link = element.get('href')
            companies_links.append(self.site + company_link)

        return companies_links


class CompanyParser:
    def __init__(self, client: 'URLReader'):
        """
        Create class for parsing information from company page on site
        'https://markets.businessinsider.com'

        :param client: Client for processing web requests
        :type client: URLReader
        """
        self.soup = None
        self.client = client

    @staticmethod
    def _set_up_data_link(data_link, tkdata):
        """
        Function for filling url link with associated company data to get
        time series statistics

        :param data_link: URL link with missing parameters
        :type data_link: str
        :param tkdata: Company specific parameter for url request
        :type tkdata: str
        :return: Ready to use URL link
        :rtype: str
        """
        current = datetime.today()
        current_date = f'{current.year}{current.month}{current.day}'
        # Not consider leap year
        year_back = current - timedelta(days=365)
        year_back_date = f'{year_back.year}{year_back.month}{year_back.day}'

        data_link = data_link.format(tkdata, year_back_date, current_date)
        return data_link

    def _parse_company_db_address(self):
        """
        Read from HTML code company address for getting time series statistics

        :return: Company specific address for url request
        :rtype: str
        """
        pattern_to_find = '"TKData" : "'
        element = self.soup.find('div', class_='responsivePosition')
        if not element:
            raise ElementNotFoundError
        func_str = element.find('script').contents[0]

        tkdata_start = func_str.find(pattern_to_find)
        tkdata_end = func_str[tkdata_start+len(pattern_to_find):].find('"')
        tkdata_start = tkdata_start + len(pattern_to_find)
        tkdata_end = tkdata_start + tkdata_end
        tkdata = func_str[tkdata_start:tkdata_end]
        return tkdata

    def _parse_parent(self, string: str):
        """
        Function to get data from parent HTML element

        :param string: Text value of HTML element
        :type string: str
        :return: Text value of the parent HTML element
        :rtype: str
        """
        element = self.soup.find('div', string=string)
        if not element:
            raise ElementNotFoundError
        parent_element = element.parent
        result = parent_element.contents[0]
        result = result.strip('\r\n\t')
        return result

    @parsing_decorator
    def _parse_name(self):
        element = self.soup.find('span', class_='price-section__label')
        if not element:
            raise ElementNotFoundError
        name = element.contents[0]
        name = name.strip('\r\n\t')
        return name

    @parsing_decorator
    def _parse_current_value(self):
        element = self.soup.find('span', class_='price-section__current-value')
        if not element:
            raise ElementNotFoundError
        price = element.contents[0]
        price = price.replace(',', '')
        return float(price)

    @parsing_decorator
    def _parse_company_code(self):
        element = self.soup.find('span', class_='price-section__category')
        if not element:
            raise ElementNotFoundError
        company_code = element.find('span').contents[0]
        company_code = company_code.split()[1]
        return company_code

    @parsing_decorator
    def _parse_company_pe(self):
        company_pe = self._parse_parent('P/E Ratio')
        return float(company_pe)

    @parsing_decorator
    def _parse_company_year_growth(self, data_link):
        tkdata = self._parse_company_db_address()
        url_link = self._set_up_data_link(data_link, tkdata)
        data = self.client.get_page(url_link)

        data_list = eval(data)
        start_value = float(data_list[0]['Close'])
        end_value = float(data_list[-1]['Close'])
        year_growth = (end_value - start_value) * 100 / start_value
        return year_growth

    @parsing_decorator
    def _parse_company_profit(self):
        low_price = self._parse_parent('52 Week Low')
        high_price = self._parse_parent('52 Week High')
        low_price = float(low_price.replace(',', ''))
        high_price = float(high_price.replace(',', ''))
        related_profit = (high_price - low_price) * 100 / low_price
        return related_profit

    def parse_company(self, page, data_link):
        self.soup = BeautifulSoup(page, 'html.parser')
        name = self._parse_name()
        price = self._parse_current_value()
        code = self._parse_company_code()
        pe = self._parse_company_pe()
        growth = self._parse_company_year_growth(data_link)
        profit = self._parse_company_profit()

        company_dict = {'name': name,
                        'code': code,
                        'price': price,
                        'P/E': pe,
                        'growth': growth,
                        'profit': profit}

        return company_dict


if __name__ == '__main__':

    current_path = os.path.abspath(os.getcwd())
    current_path = os.path.join(current_path, 'homework10')
    commands_file = os.path.join(current_path, 'links.toml')
    with open(commands_file, 'r') as fi:
        commands = toml.load(fi)

    client = URLReader()
    parser = TableParser(commands['INITIAL_LINK'])
    url_data = client.read_url(commands['FIRST_PAGE_LINK'])
    url_str = client.decode_url(url_data)
    pages_list = parser.parse_pages_number(url_str)
    print(pages_list)

    companies_dict = parser.parse_companies(url_str)
    for company in companies_dict.keys():
        print(companies_dict[company])
