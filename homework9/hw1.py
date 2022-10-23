"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import math
import os
from pathlib import Path
from typing import Generator, Iterator, List, Optional, Union

empty_object = object()


def get_lines(file_path:  str,
              encoding: Optional[str] = 'utf-8',
              errors: Optional[str] = 'ignore') -> Generator:
    """
    Read file from file_path line by line

    :param file_path: Path to the file
    :type file_path: str
    :param encoding: Codec to decode symbols in file
    :type encoding: Optional[str]
    :param errors: Flag defining the way to handle errors
    :type errors: Optional[str]
    :return: Generator yielding lines from file
    :rtype: Generator
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError

    with open(file_path, 'r', encoding=encoding, errors=errors) as fi:
        line = fi.readline()
        while line:
            yield int(line)
            line = fi.readline()
        yield empty_object


def merge_sorted_files(file_list: 'List[Union[Path, str], ...]',
                       encoding:  Optional[str] = 'utf-8',
                       errors: Optional[str] = 'ignore') -> Iterator:
    """
    Merge integers in increasing order from a list of files
    File structure example:
        file1.txt:
        1
        3
        5

    :param file_list: List of filenames
    :type file_list: List[Union[Path, str], ...]
    :param encoding: Codec to decode symbols in file
    :type encoding: Optional[str]
    :param errors: Flag defining the way to handle errors
    :type errors: Optional[str]
    :return: Iterator for merged list
    :rtype: Iterator
    """
    generators = [get_lines(filename, encoding, errors)
                  for filename in file_list]
    data_buffer = [next(gen) for gen in generators]

    # Processing empty files
    wrong_indices = [ind for ind, elem in enumerate(data_buffer)
                     if elem == empty_object]
    for i, index in enumerate(wrong_indices):
        index = index - i
        generators.pop(index)
        data_buffer.pop(index)

    # Generating values
    precessed_generators = 0
    while precessed_generators < len(generators):

        min_element = min(data_buffer)
        min_index = data_buffer.index(min_element)
        data_buffer[min_index] = next(generators[min_index])
        if data_buffer[min_index] == empty_object:
            data_buffer[min_index] = math.inf
            precessed_generators += 1

        yield min_element
