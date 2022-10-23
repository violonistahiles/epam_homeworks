import os
import sqlite3
from typing import Callable, Dict, List

import toml

empty_element = object()


class DatabaseNotExistError(Exception):
    """Database with specified filename is not exists"""


class TableNotExists(Exception):
    """This table is not exists in the database"""


def prepare_database(func: Callable) -> Callable:
    """
    Create connection to database and set up cursor instance during
    function execution

    :param func: Function to do some operation with database
    :type func: Callable
    """
    def wrapper(cls: "TableData", *args, **kwargs):
        database_path = os.path.join(cls._dir_path, cls._database_name)
        if not os.path.exists(database_path):
            raise DatabaseNotExistError

        cls._conn = sqlite3.connect(database_path)
        cls._cursor = cls._conn.cursor()
        result = func(cls, *args, **kwargs)
        cls._conn.close()

        return result

    return wrapper


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
        self._iter_value = empty_element
        self._cursor = None
        self._database_name = database_name

        self._commands = self._read_commands(table_name)
        self._check_table(table_name)

    @prepare_database
    def _check_table(self, table_name: str):
        """
        Check if database contain table with specified name

        :param table_name: Table name from database for interaction
        :type table_name: str
        """
        db_tables = self._cursor.execute(self._commands['TABLES']).fetchall()
        tables = [table[0] for table in db_tables]
        if table_name not in tables:
            raise TableNotExists

    def _read_commands(self, table_name: str) -> Dict:
        """
        Set up command for interaction with database

        :param table_name: Table name from database for interaction
        :type table_name: str
        :return: Dictionary with commands related to table_name
        :rtype: Dict
        """
        commands_file = os.path.join(self._dir_path, 'cmd.toml')
        with open(commands_file) as fi:
            commands = toml.load(fi)

        for act in commands:
            commands[act] = commands[act].format(table_name)

        return commands

    def _read_table_columns(self) -> List:
        """
        Read columns from selected table in database

        :return: List with names of columns from table
        :rtype: List
        """
        data = self._cursor.execute(self._commands['COLUMNS'])
        columns = [column[0] for column in data.description]
        return columns

    @prepare_database
    def __len__(self) -> int:
        db_response = self._cursor.execute(self._commands['LEN'])
        table_len = db_response.fetchall()[0][0]
        return table_len

    @prepare_database
    def __getitem__(self, item: str):
        # Update columns if table was changed
        columns = self._read_table_columns()
        sample = self._cursor.execute(self._commands['GETITEM'],
                                      {'name': item})
        result = sample.fetchall()
        if result:
            return {key: value for key, value in zip(columns, result[0])}

    def __contains__(self, item: str):
        result = self.__getitem__(item)
        return True if result else False

    def __iter__(self):
        # Set flag for starting iteration from first sorted element from table
        self._iter_value = empty_element
        return self

    @prepare_database
    def __next__(self):
        # Update columns if table was changed
        columns = self._read_table_columns()
        if self._iter_value == empty_element:
            sample = self._cursor.execute(self._commands['ITER_START'])
        else:
            sample = self._cursor.execute(self._commands['ITER_NEXT'],
                                          {'name': self._iter_value})
        result = sample.fetchall()
        if result:
            elem = {key: value for key, value in zip(columns, result[0])}
            self._iter_value = elem['name']
            return elem

        raise StopIteration
