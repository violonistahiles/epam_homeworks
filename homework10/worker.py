import asyncio
import json
import os

import toml

from homework10.scalper import Scalper


class Worker:
    def __init__(self):
        current_path = os.path.abspath(os.getcwd())
        # current_path = os.path.join(current_path, 'homework10')
        info_file = os.path.join(current_path, 'links.toml')
        self.file_names = {'price': os.path.join(current_path, 'price.json'),
                           'pe': os.path.join(current_path, 'pe.json'),
                           'growth': os.path.join(current_path, 'growth.json'),
                           'profit': os.path.join(current_path, 'profit.json')}
        with open(info_file, 'r') as fi:
            info = toml.load(fi)

        self._scalper = Scalper(info)
        self._number_of_elements = 10

    def _filter_elements(self, key, coef=1, reverse=False):
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
        number_of_threads = 10
        sem = asyncio.Semaphore(number_of_threads)
        async with sem:
            self.dollar_course = await self._scalper.scalp_usd_course()
            self.companies_list = await self._scalper.scalp()
        await self._scalper.client.session.close()

    def _get_most_expensive(self):
        data = self._filter_elements('price',
                                     self.dollar_course,
                                     reverse=True)
        with open(self.file_names['price'], 'w') as fi:
            json.dump(data, fi)

    def _get_worst_pe(self):
        data = self._filter_elements('P/E')
        with open(self.file_names['pe'], 'w') as fi:
            json.dump(data, fi)

    def _get_best_growth(self):
        data = self._filter_elements('growth', reverse=True)
        with open(self.file_names['growth'], 'w') as fi:
            json.dump(data, fi)

    def _get_most_profitable(self):
        data = self._filter_elements('profit', reverse=True)
        with open(self.file_names['profit'], 'w') as fi:
            json.dump(data, fi)

    def get_result(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._get_companies_info())
        self._get_most_expensive()
        self._get_worst_pe()
        self._get_best_growth()
        self._get_most_profitable()


if __name__ == '__main__':
    worker = Worker()
    worker.get_result()
