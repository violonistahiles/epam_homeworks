import asyncio
import json
import os
from typing import Dict, List, Tuple

import toml

from homework10.scalper import Scalper


class Worker:
    def __init__(self, number_of_elements: int):
        """
        Create class for collecting and filtering data about companies

        :param number_of_elements: Number of companies which information save
                                   to results
        :type number_of_elements: int
        """
        current_path = os.path.abspath(os.getcwd())
        current_path = os.path.join(current_path, 'homework10')
        info_file = os.path.join(current_path, 'links.toml')
        with open(info_file, 'r') as fi:
            info = toml.load(fi)
        # Filenames to save data
        self._files = {'price': os.path.join(current_path, 'price.json'),
                       'pe': os.path.join(current_path, 'pe.json'),
                       'growth': os.path.join(current_path, 'growth.json'),
                       'profit': os.path.join(current_path, 'profit.json')}

        self._scalper = Scalper(info)
        self._number_of_elements = number_of_elements

    async def _get_info(self) -> Tuple[float, List[Dict]]:
        """
        Collect _companies data from web

        :return: Current USD course, List with information about all companies
        :rtype: Tuple[float, List[Dict]]
        """
        number_of_threads = 15
        sem = asyncio.Semaphore(number_of_threads)
        async with sem:
            usd_course = await self._scalper.scalp_usd_course()
            companies_list = await self._scalper.scalp()
        await self._scalper.close_session()

        return usd_course, companies_list

    def _sort_elements(
            self, companies_info: List[Dict], key: str,
            coef: float = 1.0, reverse: bool = False
    ) -> List[Dict]:
        """
        Sort parsed data by some key and take only defined number of elements

        :param companies_info: List with collected information about all
                               companies
        :type companies_info: List[Dict]
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
        elements = [item for item in companies_info if item[key]]
        elements = sorted(elements, key=lambda x: x[key], reverse=reverse)

        data = []
        for i in range(self._number_of_elements):
            tmp_dict = elements[i]
            new_dict = {'name': tmp_dict['name'],
                        'code': tmp_dict['code'],
                        key: tmp_dict[key]*coef}
            data.append(new_dict)

        return data

    def _write_to_file(self, data: List[Dict], category: str):
        """
        Save data to corresponding file

        :param data: List with data
        :type data: List[Dict]
        :param category: Category of the data
        :type category: str
        """
        with open(self._files[category], 'w') as fi:
            json.dump(data, fi)

    def _save_data(
            self, companies_info: List[Dict], key: str,
            coef: float = 1.0, reverse: bool = False
    ) -> None:
        """
        Save specified data category to related file

        :param companies_info: List with collected information about all
                               companies
        :type companies_info: List[Dict]
        :param key: Data category
        :type key: str
        :param coef: Coefficient to convert data
        :type coef: float
        :param reverse: Flag to sort data in increasing or decreasing order
        type reverse: bool
        """
        data = self._sort_elements(companies_info, key, coef, reverse)
        self._write_to_file(data, key)

    def get_result(self):
        """Collect companies data and save it to the files"""
        loop = asyncio.get_event_loop()
        usd_course, companies_info = loop.run_until_complete(self._get_info())
        self._save_data(companies_info, 'price', usd_course, reverse=True)
        self._save_data(companies_info, 'pe')
        self._save_data(companies_info, 'growth', reverse=True)
        self._save_data(companies_info, 'profit', reverse=True)


if __name__ == '__main__':
    worker = Worker(number_of_elements=10)
    worker.get_result()
