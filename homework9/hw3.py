"""
Write a function that takes directory path,
a file extension and an optional tokenizer.
It will count lines in all files with that extension
if there are no tokenizer.
If a tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import collections
import os
from pathlib import Path
from typing import Callable, Generator, List, Optional


def empty_tokenizer(line: str) -> List[str]:
    """
    Tokenizer to convert single element as a token

    :param line: Input string
    :type line: str
    :return: List with one element
    :rtype: List[str]
    """
    return [line]


def get_lines(file_path:  str,
              encoding: Optional[str] = 'utf-8',
              errors: Optional[str] = 'ignore',
              tokenizer: Optional[Callable] = None) -> Generator:
    """
    Read file from file_path line by line

    :param file_path: Path to the file
    :type file_path: str
    :param encoding: Codec to decode symbols in file
    :type encoding: Optional[str]
    :param errors: Flag defining the way to handle errors
    :type errors: Optional[str]
    :param tokenizer: Function to convert line into a tokens
    :type tokenizer: Optional[Callable]
    :return: Generator yielding number of tokens in current line from file
    :rtype: Generator
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError

    if not tokenizer:
        tokenizer = empty_tokenizer

    with open(file_path, 'r', encoding=encoding, errors=errors) as fi:
        line = fi.readline()
        while line or '\n' in line:
            tokens = tokenizer(line)

            if isinstance(tokens, collections.abc.Generator):
                yield len(list(tokens))
            else:
                yield len(tokens)

            line = fi.readline()


def universal_file_counter(
    dir_path: Path,
    file_extension: str,
    tokenizer: Optional[Callable] = None,
    encoding: Optional[str] = 'utf-8',
    errors: Optional[str] = 'ignore'
) -> int:
    """
    Counts total number of lines from files with specified
    extension from directory if tokenizer is not defined.
    Or total number of tokens if tokenizer is defined.

    :param dir_path: Path to directory with files
    :type dir_path: Path
    :param file_extension: Extension descriptor for filtering files
    :type file_extension: str
    :param tokenizer:  Function to convert line into a tokens
    :type tokenizer: Optional[Callable]
    :param encoding: Codec to decode symbols in file
    :type encoding: Optional[str]
    :param errors: Flag defining the way to handle errors
    :type errors: Optional[str]
    :return: Total number of counted elements
    :rtype: int
    """
    filenames = os.listdir(dir_path)
    file_paths = [os.path.join(dir_path, filename) for filename in filenames
                  if filename.endswith(file_extension)]

    tokens_number = 0
    for file_path in file_paths:
        tokens_number += sum(list(get_lines(file_path, encoding,
                                            errors, tokenizer)))

    return tokens_number
