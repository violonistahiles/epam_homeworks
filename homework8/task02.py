import os
import sqlite3
from typing import Generator, List

import toml


class DatabaseNotExistError(Exception):
    """Database with specified filename is not exists"""


class TableNotExists(Exception):
    """This table is not exists in the database"""


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
        self._check_table(table_name)

    def _prepare_database(self, database_name):
        """
        Create connection to database and set up cursor instance

        :param database_name: Filename of database
        :type database_name: str
        """
        database_path = os.path.join(self._dir_path, database_name)
        if not os.path.exists(database_path):
            raise DatabaseNotExistError

        self._conn = sqlite3.connect(database_path)
        self._cursor = self._conn.cursor()

    def _check_table(self, table_name):
        """
        Check if database contain table with specified name

        :param table_name: Table name from database for interaction
        :type table_name: str
        """
        db_tables = self._cursor.execute(self._commands['TABLES']).fetchall()
        tables = [table[0] for table in db_tables]
        print(table_name, tables)
        if table_name not in tables:
            raise TableNotExists

    def _read_commands(self, table_name):
        """
        Set up command for interaction with database

        :param table_name: Table name from database for interaction
        :type table_name: str
        """
        commands_file = os.path.join(self._dir_path, 'cmd.toml')
        with open(commands_file) as fi:
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
        return True if result else False

    def __iter__(self):
        self._read_table_columns()  # Update columns if table was changed
        self._samples = self._cursor.execute(self._commands['ITER'])
        return column_value_gen(self._samples, self._columns)
