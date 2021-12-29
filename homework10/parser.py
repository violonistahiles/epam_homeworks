import datetime
import re
from typing import Callable, Dict, List

from bs4 import BeautifulSoup


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
    """
    Create parser for getting information about S&P 500 stocks
    from the site 'https://markets.businessinsider.com'
    """

    @staticmethod
    def parse_pages_number(page: str) -> List:
        """
        Parsing links for pages with _companies tables
        Element to find example:
        '<a href="?p=4">4</a>', where ?p=4 is link
        for 4-th page with _companies list

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

        return pages_list

    @staticmethod
    def parse_companies(page: str, site: str) -> List:
        """
        Parsing company link from company html element
        Element to find example:
        <a href="/stocks/aos-stock" title="A.O. Smith">A.O. Smith</a>

        :param page: String representation of html page
        :type page: str
        :param site: Link to the initial site page
        :type site: str
        """
        soup = BeautifulSoup(page, 'html.parser')
        # Find table with _companies
        table = soup.find("tbody", class_='table__tbody')

        # Process table line by line
        companies_links = []
        for element in table.find_all("a",
                                      href=re.compile(r"^/stocks.*stock$")):

            company_link = element.get('href')
            companies_links.append(site + company_link)

        return companies_links


class CompanyParser:
    def __init__(self):
        """
        Create class for parsing information from company page on site
        'https://markets.businessinsider.com'
        """
        self._soup = None

    @staticmethod
    def _set_up_data_link(data_link: str, tkdata: str) -> str:
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
        current = datetime.datetime.today()
        current_date = f'{current.year}{current.month}{current.day}'
        # Not consider leap year
        year_back = current - datetime.timedelta(days=365)
        year_back_date = f'{year_back.year}{year_back.month}{year_back.day}'

        data_link = data_link.format(tkdata, year_back_date, current_date)
        return data_link

    def _parse_company_db_address(self) -> str:
        """
        Read from HTML code company address for getting time series statistics

        :return: Company specific address for url request
        :rtype: str
        """
        pattern_to_find = '"TKData" : "'
        element = self._soup.find('script',
                                  string=re.compile('.*ChartViewmodel.*'))
        if not element:
            raise ElementNotFoundError
        func_str = element.contents[0]

        tkdata_start = func_str.find(pattern_to_find)
        tkdata_end = func_str[tkdata_start+len(pattern_to_find):].find('"')
        tkdata_start = tkdata_start + len(pattern_to_find)
        tkdata_end = tkdata_start + tkdata_end
        tkdata = func_str[tkdata_start:tkdata_end]
        return tkdata

    def _parse_parent(self, string: str) -> str:
        """
        Function to get data from parent HTML element

        :param string: Text value of HTML element
        :type string: str
        :return: Text value of the parent HTML element
        :rtype: str
        """
        element = self._soup.find('div', string=string)
        if not element:
            raise ElementNotFoundError
        parent_element = element.parent
        result = parent_element.contents[0]
        result = result.strip('\r\n\t')
        return result

    @parsing_decorator
    def _parse_name(self) -> str:
        """
        Parse company name from HTML

        :return: Company name
        :rtype: str
        """
        element = self._soup.find('span', class_='price-section__label')
        if not element:
            raise ElementNotFoundError
        name = element.contents[0]
        name = name.strip('\r\n\t')
        return name

    @parsing_decorator
    def _parse_current_value(self) -> float:
        """
        Parse current company share

        :return: Company share price in USD
        :rtype: float
        """
        element = self._soup.find('span',
                                  class_='price-section__current-value')
        if not element:
            raise ElementNotFoundError
        price = element.contents[0]
        price = price.replace(',', '')
        return float(price)

    @parsing_decorator
    def _parse_company_code(self) -> str:
        """
        Parse company abbreviation on the web site

        :return: Company abbreviation on the web site
        :rtype: str
        """
        element = self._soup.find('span', class_='price-section__category')
        if not element:
            raise ElementNotFoundError
        company_code = element.find('span').contents[0]
        company_code = company_code.split()[1]
        return company_code

    @parsing_decorator
    def _parse_company_pe(self) -> float:
        """
        Parse company P/E ratio

        :return: Company P/E ratio
        :rtype: float
        """
        company_pe = self._parse_parent('P/E Ratio')
        company_pe = company_pe.replace(',', '')
        return float(company_pe)

    @parsing_decorator
    def _get_link_to_statistics(self, data_link: str) -> str:
        """
        Prepare URL link for year statistic request

        :param data_link: Pattern for URL link
        :type data_link: str
        :return: URL link with data associated to current company
        :rtype: str
        """
        tkdata = self._parse_company_db_address()
        url_link = self._set_up_data_link(data_link, tkdata)
        return url_link

    @parsing_decorator
    def _parse_company_profit(self) -> float:
        """
        Parse and calculate potential profit of buying company shares
        from 52 weeks low to 52 weeks high period

        :return: Profit related to start price in percentages
        :rtype: float
        """
        low_price = self._parse_parent('52 Week Low')
        high_price = self._parse_parent('52 Week High')
        low_price = float(low_price.replace(',', ''))
        high_price = float(high_price.replace(',', ''))
        related_profit = (high_price - low_price) * 100 / low_price
        return related_profit

    @staticmethod
    def parse_company_year_growth(data: str) -> float:
        """
        Parse company year growth from statistics data

        :param data: String with raw data containing days statistics
        :type data: str
        :return: Growth related to the price from 365 days back
        :rtype: float
        """
        start_l = data.find('{')
        end_l = data.find('}')
        start_r = data.rfind('{')
        end_r = data.rfind('}')

        data_st = data[start_l:end_l]
        data_end = data[start_r:end_r]

        start_value = float(data_st[data_st.find(':')+1: data_st.find(',')])
        end_value = float(data_end[data_end.find(':')+1: data_end.find(',')])
        year_growth = (end_value - start_value) * 100 / start_value
        return year_growth

    def parse_company(self, page: str, data_link: str) -> Dict:
        """
        Collect all necessary data about company from HTML page

        :param page: HTML page
        :param page: str
        :param data_link: URL link pattern for collecting year statistic
        :type data_link: str
        :return: Collected data
        :rtype: dict
        """
        self._soup = BeautifulSoup(page, 'html.parser')
        name = self._parse_name()
        price = self._parse_current_value()
        code = self._parse_company_code()
        pe = self._parse_company_pe()
        profit = self._parse_company_profit()
        growth_link = self._get_link_to_statistics(data_link)

        company_dict = {'name': name,
                        'code': code,
                        'price': price,
                        'P/E': pe,
                        'link': growth_link,
                        'profit': profit}

        return company_dict
