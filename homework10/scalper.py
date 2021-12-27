import asyncio
import os
from datetime import datetime
from xml.etree import ElementTree

import toml

from homework10.connection import URLReader
from homework10.parser import CompanyParser, TableParser


class Scalper:
    def __init__(self, info):

        self.info = info
        self.client = URLReader()
        self.companies_parser = TableParser(info['INITIAL_LINK'])
        self.company_parser = CompanyParser(self.client)
        self.companies_links = []
        self.pages_links = []
        self.companies = []

    async def scalp_usd_course(self):
        link = self.info['BANK_LINK']
        date = datetime.today()
        link = link.format(f'{date.day}/{date.month}/{date.year}')

        page = await self.client.get_page(link, encoding='ISO-8859-2')
        root = ElementTree.fromstring(page)
        dollar_course_str = root.findall(".//*[@ID='R01235']/Value")[0].text
        dollar_course = float(dollar_course_str.replace(',', '.'))

        return dollar_course

    async def _scalp_first_page(self):
        first_page = await self.client.get_page(self.info['FIRST_PAGE_LINK'])

        pages_number = self.companies_parser.parse_pages_number(first_page)
        self.pages_links = [self.info['FIRST_PAGE_LINK'] + page for page
                            in pages_number]

        new_companies_links = self.companies_parser.parse_companies(first_page)
        self.companies_links.extend(new_companies_links)

    async def _scalp_page(self, link):
        page = await self.client.get_page(link)
        new_companies_links = self.companies_parser.parse_companies(page)
        self.companies_links.extend(new_companies_links)

    async def _scalp_company_page(self, link):
        page = await self.client.get_page(link)
        data = self.company_parser.parse_company(page, self.info['DATA_LINK'])
        self.companies.append(data)
        print(data)

    async def scalp(self):
        await self._scalp_first_page()

        tasks = [asyncio.create_task(self._scalp_page(url)) for url
                 in self.pages_links]
        await asyncio.gather(*tasks)

        tasks = [asyncio.create_task(self._scalp_company_page(url)) for url
                 in self.companies_links]
        await asyncio.gather(*tasks)

        return self.companies


if __name__ == '__main__':

    current_path = os.path.abspath(os.getcwd())
    # current_path = os.path.join(current_path, 'homework10')
    info_file = os.path.join(current_path, 'links.toml')
    with open(info_file, 'r') as fi:
        info = toml.load(fi)

    scalper = Scalper(info)
    print(scalper.dollar_course)
    scalper.scalp()
