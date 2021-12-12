import os
import sqlite3
from typing import Generator, List

import toml


def column_value_gen(data: sqlite3.Cursor, columns: List[str]) -> Generator:
    """
    Generator for database response instances

    :param data: Response containing rows from database
    :type data: sqlite3.Cursor
    :param columns: Database table columns
    :type columns: List[str]
    :return: Generator for dict examples containing
             column_name: data_example_from_column samples
    :rtype: Generator
    """
    for data_example in data:
        yield {key: value for key, value in zip(columns, data_example)}


class TableData:
    def __init__(self, database_name: str, table_name: str):
        """
        :param database_name: Filename of the database
        :type database_name: str
        :param table_name: Name of the table in the database
        :type table_name: str
        """
        current_path = os.path.abspath(os.getcwd())
        self._dir_path = os.path.join(current_path, 'homework8')
        self._prepare_database(database_name)
        self._read_commands(table_name)

    def _prepare_database(self, database_name):
        """
        Create connection to database and set up cursor instance

        :param database_name: Filename of database
        :type database_name: str
        """
        self._database_name = os.path.join(self._dir_path, database_name)
        self._conn = sqlite3.connect(self._database_name)
        self._cursor = self._conn.cursor()

    def _read_commands(self, table_name):
        """
        Set up command for interaction with database

        :param table_name: Table name from database for interaction
        :type table_name: str
        """
        self._commands_file = os.path.join(self._dir_path, 'cmd.toml')
        with open(self._commands_file) as fi:
            self._commands = toml.load(fi)

        for act in self._commands:
            self._commands[act] = self._commands[act].format(table_name)

    def _read_table_columns(self):
        """
        Read columns from selected table in database
        """
        data = self._cursor.execute(self._commands['COLUMNS'])
        self._columns = [column[0] for column in data.description]

    def __len__(self):
        db_response = self._cursor.execute(self._commands['LEN'])
        table_len = db_response.fetchall()[0][0]
        return table_len

    def __getitem__(self, item):
        self._read_table_columns()  # Update columns if table was changed
        sample = self._cursor.execute(self._commands['GETITEM'],
                                      {'item': item})
        result = sample.fetchall()
        if result:
            return {key: value for key, value in zip(self._columns, result[0])}

    def __contains__(self, item):
        result = self.__getitem__(item)
        if result:
            return True

    def __iter__(self):
        self._read_table_columns()  # Update columns if table was changed
        self._samples = self._cursor.execute(self._commands['ITER'])
        return column_value_gen(self._samples, self._columns)


if __name__ == '__main__':
    test_database_name = 'example.db'
    test_table = 'presidents'

    presidents = TableData(test_database_name, test_table)
    print(len(presidents))
    print(presidents['Yeltsin'])
    print('Yeltsin' in presidents)

    for president in presidents:
        print(president['name'])

    # db_path = os.path.join(os.path.abspath(os.getcwd()),
    #                        'homework8',
    #                        test_database_name)
    # conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()
    # cursor.execute("delete from presidents where name='Putin'")
    # cursor.execute("insert into presidents values('Putin', 56, 'ZIP')")
    # conn.commit()
