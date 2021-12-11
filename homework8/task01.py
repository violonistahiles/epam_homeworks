"""
We have a file that works as key-value storage, each line is represented
as key and value separated by = symbol, example:

name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers. If a value can be treated both
as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt') that has its keys and values
accessible as collection items and as attributes.
Example:
     storage['name'] # will be string 'kek' storage
     song_name # will be 'shadilay' storage
     power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute
(for example when there's a line 1=something) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into
memory.
"""
from typing import Generator, Tuple, Union


def line_gen(path: str) -> Generator:
    """
    Read file line by line

    :param path: Path to the file
    :type path: str
    :return: Generator yielding lines from file
    :rtype: Generator
    """
    with open(path, 'r') as fi:
        line = fi.readline()
        while line and '\n' in line:
            yield line
            line = fi.readline()


def convert_to_int(input_value: str) -> Union[str, int]:
    """
    Try to convert input string value to integer

    :param input_value: Input string
    :type input_value: str
    :return: Integer if conventing is possible else initial string
    :rtype: Union[str, int]
    """
    try:
        input_value = int(input_value)
        return input_value
    except ValueError:
        return input_value


def process_line(line: str) -> Tuple[Union[int, str], Union[int, str]]:
    """
    Split line to key and value pairs

    :param line: String that looks like "key=value"
    :type line: str
    :return: Key and value from line
    :rtype: Tuple[Union[int, str], Union[int, str]]
    """
    line = line.rstrip('\n')
    key, value = line.split('=')
    return convert_to_int(key), convert_to_int(value)


class KeyValueStorage:
    def __init__(self, path):
        self._get_keys_and_values(path)

    def _get_keys_and_values(self, path):
        """
        Assign key value pairs from file to class attributes

        :param path: Path to the file
        :type path: str
        """
        lines = line_gen(path)
        for line in lines:
            key, value = process_line(line)

            if isinstance(key, int):
                raise ValueError('Int value can\'t be key')
            # Save initial value if key is repeated
            if key in self.__dict__:
                continue

            self.__setitem__(key, value)

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __getattr__(self, key):
        return self.__getitem__(key)

    def items(self):
        return self.__dict__.items()

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()
