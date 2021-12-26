import os
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from queue import Queue

import toml

from homework10.connection import URLReader
from homework10.parser import CompanyParser, TableParser


class Scalper:
    def __init__(self, info):

        self.info = info
        self.client = URLReader()
        self.companies_parser = TableParser(info['INITIAL_LINK'])
        self.company_parser = CompanyParser(self.client)
        self.companies_links = Queue(500)
        self.pages_links = None
        self.companies = []
        self._scalp_usd_course()
        self.attempts = 5

    def _scalp_usd_course(self):
        link = self.info['BANK_LINK']
        date = datetime.today()
        link = link.format(f'{date.day}/{date.month}/{date.year}')

        page = self.client.get_page(link, encoding='ISO-8859-2')
        root = ET.fromstring(page)
        dollar_course_str = root.findall(".//*[@ID='R01235']/Value")[0].text
        self.dollar_course = float(dollar_course_str.replace(',', '.'))

    def _scalp_first_page(self):
        first_page = self.client.get_page(self.info['FIRST_PAGE_LINK'])

        pages = self.companies_parser.parse_pages_number(first_page)
        pages_links = [self.info['FIRST_PAGE_LINK'] + page for page in pages]
        self.pages_links = Queue(len(pages_links))
        for page_link in pages_links:
            self.pages_links.put(page_link)

        companies_links = self.companies_parser.parse_companies(first_page)
        for company_link in companies_links:
            self.companies_links.put(company_link)

    def _scalp_page(self):
        page_url = self.pages_links.get()
        page = self.client.get_page(page_url)
        companies_links = self.companies_parser.parse_companies(page)

        for company_link in companies_links:
            self.companies_links.put(company_link)

    def _scalp_company_page(self):
        page_url = self.companies_links.get()
        page = self.client.get_page(page_url)
        data = self.company_parser.parse_company(page, self.info['DATA_LINK'])
        self.companies.append(data)
        print(data)

    def scalp(self):
        self._scalp_first_page()
        time.sleep(1)

        while not self.pages_links.empty() or not self.companies_links.empty():
            if not self.pages_links.empty():
                self._scalp_page()
                time.sleep(1)
            if not self.companies_links.empty():
                self._scalp_company_page()
                time.sleep(1)

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
