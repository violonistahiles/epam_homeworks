import asyncio
import json
import os
from typing import Dict, List

import toml

from homework10.scalper import Scalper


class Worker:
    def __init__(self):
        """
        Create class for collecting and filtering data about companies
        """
        current_path = os.path.abspath(os.getcwd())
        # current_path = os.path.join(current_path, 'homework10')
        info_file = os.path.join(current_path, 'links.toml')
        with open(info_file, 'r') as fi:
            info = toml.load(fi)
        # Filenames to save data
        self.file_names = {'price': os.path.join(current_path, 'price.json'),
                           'pe': os.path.join(current_path, 'pe.json'),
                           'growth': os.path.join(current_path, 'growth.json'),
                           'profit': os.path.join(current_path, 'profit.json')}

        self._scalper = Scalper(info)
        self._number_of_elements = 10  # Limit of companies to write in file

    def _sort_elements(self,
                       key: str,
                       coef: float = 1.0,
                       reverse: bool = False) -> List[Dict]:
        """
        Sort parsed data by some key and take only defined number of elements

        :param key: Dictionary key to sort values
        :type key: str
        :param coef: Optional parameter to modify selected data
        :type coef: float
        :param reverse: Flag to select order of sorting
        :type reverse: bool
        :return: List of dictionary with company code, name and selected
                 parameter
        :rtype: List
        """
        elements = [item for item in self.companies_list if item[key]]
        elements = sorted(elements, key=lambda x: x[key], reverse=reverse)

        data = []
        for i in range(self._number_of_elements):
            tmp_dict = elements[i]
            new_dict = {'name': tmp_dict['name'],
                        'code': tmp_dict['code'],
                        key: tmp_dict[key]*coef}
            data.append(new_dict)

        return data

    async def _get_companies_info(self):
        """Collect companies data from web"""
        number_of_threads = 15
        sem = asyncio.Semaphore(number_of_threads)
        async with sem:
            self.usd_course = await self._scalper.scalp_usd_course()
            self.companies_list = await self._scalper.scalp()
        await self._scalper.client.session.close()

    def _get_most_expensive(self):
        """Save information about companies price"""
        data = self._sort_elements('price',
                                   self.usd_course,
                                   reverse=True)
        with open(self.file_names['price'], 'w') as fi:
            json.dump(data, fi)

    def _get_worst_pe(self):
        """Save information about P/E coefficient"""
        data = self._sort_elements('P/E')
        with open(self.file_names['pe'], 'w') as fi:
            json.dump(data, fi)

    def _get_best_growth(self):
        """Save information about companies year growth"""
        data = self._sort_elements('growth', reverse=True)
        with open(self.file_names['growth'], 'w') as fi:
            json.dump(data, fi)

    def _get_most_profitable(self):
        """Save information about most potentially profitable companies"""
        data = self._sort_elements('profit', reverse=True)
        with open(self.file_names['profit'], 'w') as fi:
            json.dump(data, fi)

    def get_result(self):
        """Collect companies data and save it to the files"""
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._get_companies_info())
        self._get_most_expensive()
        self._get_worst_pe()
        self._get_best_growth()
        self._get_most_profitable()


if __name__ == '__main__':
    worker = Worker()
    worker.get_result()
