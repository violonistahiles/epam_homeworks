import asyncio
from datetime import datetime
from typing import Dict, List
from xml.etree import ElementTree

from homework10.connection import URLReader
from homework10.parser import CompanyParser, TableParser
from homework10.utils import fill_date


class Scalper:
    def __init__(self, info: Dict):
        """
        Create class for collecting information from URL pages

        :param info: Dictionary with URL links to visit during data collection
        :type info: Dict
        """
        self._info = info
        self.client = URLReader()
        self._table_parser = TableParser()
        self._company_parser = CompanyParser()
        self._companies_links = []
        self._pages_links = []
        self._companies = {}

    async def scalp_usd_course(self):
        """
        Get up-to-date USD course from Russia center bank

        :return: Current USD course
        :rtype: float
        """

        link = self._info['BANK_LINK']
        date = datetime.today()
        month = fill_date(date.month)
        day = fill_date(date.day)
        link = link.format(f'{day}/{month}/{date.year}')

        page = await self.client.get_page(link, encoding='ISO-8859-2')
        root = ElementTree.fromstring(page)
        dollar_course_str = root.findall(".//*[@ID='R01235']/Value")[0].text
        usd_course = float(dollar_course_str.replace(',', '.'))

        return usd_course

    async def _scalp_first_page(self):
        """Get data from initial parsing page"""
        first_page = await self.client.get_page(self._info['FIRST_PAGE_LINK'])

        pages_number = self._table_parser.parse_pages_number(first_page)
        self._pages_links = [self._info['FIRST_PAGE_LINK'] + page for page
                             in pages_number]

        links = self._table_parser.parse_companies(first_page,
                                                   self._info['SITE_LINK'])
        self._companies_links.extend(links)

    async def _scalp_table(self, link: str):
        """
        Get list of companies links from summary table

        :param link: URL link to page with company summary
        :type link: str
        """
        page = await self.client.get_page(link)
        links = self._table_parser.parse_companies(page,
                                                   self._info['SITE_LINK'])
        self._companies_links.extend(links)

    async def _scalp_company_page(self, link: str):
        """
        Get information about company from its page

        :param link: URL to company page
        :type link: str
        """
        page = await self.client.get_page(link)
        data = self._company_parser.parse_company(page,
                                                  self._info['DATA_LINK'])
        self._companies.update({data['code']: data})

    async def _scalp_company_growth(self, data: Dict):
        """
        Get information about company year growth

        :param data: Dictionary with parsed company data
        :type data: Dict
        """
        if data['link']:
            page = await self.client.get_page(data['link'])
            growth = self._company_parser.parse_company_year_growth(page)
        else:
            growth = None
        self._companies[data['code']].update({'growth': growth})
        self._companies[data['code']].pop('link')

    async def scalp(self) -> List[Dict]:
        """
        Parse _companies data in async way

        :return: List of data containing companies information
        :rtype: List[Dict]
        """
        await self._scalp_first_page()

        # Parse links for companies pages
        tasks = [asyncio.create_task(self._scalp_table(url)) for url
                 in self._pages_links]
        await asyncio.gather(*tasks)

        # Parse companies data from its pages
        tasks = [asyncio.create_task(self._scalp_company_page(url)) for url
                 in self._companies_links]
        await asyncio.gather(*tasks)

        # Parse companies growth by link gotten from companies pages
        tasks = [asyncio.create_task(self._scalp_company_growth(data)) for data
                 in self._companies.values()]
        await asyncio.gather(*tasks)

        return list(self._companies.values())
