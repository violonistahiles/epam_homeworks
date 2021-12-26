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

        self.scalper = Scalper(info)
        self.number_of_elements = 10

    def _filter_elements(self, key, coef=1, reverse=False):
        elements = [item for item in self.companies_list if item[key]]
        elements = sorted(elements, key=lambda x: x[key], reverse=reverse)

        data = []
        for i in range(self.number_of_elements):
            tmp_dict = elements[i]
            new_dict = {'name': tmp_dict['name'],
                        'code': tmp_dict['code'],
                        key: tmp_dict[key]*coef}
            data.append(new_dict)

        return data

    def _get_companies_info(self):
        self.companies_list = self.scalper.scalp()
        print(len(self.companies_list))

    def _get_most_expensive(self):
        data = self._filter_elements('price',
                                     self.scalper.dollar_course,
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

    def save_result(self):
        self._get_companies_info()
        self._get_most_expensive()
        self._get_worst_pe()
        self._get_best_growth()
        self._get_most_profitable()


if __name__ == '__main__':
    worker = Worker()
    worker.save_result()
