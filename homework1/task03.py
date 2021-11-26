"""
Write down the function, which reads input line-by-line, and find maximum and
minimum values. Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [5, 1]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def line_generator(
        file_name: str, encoding: str = 'utf-8', errors: str = 'ignore'
) -> str:
    """Iterate through lines in text file"""
    with open(file_name, encoding=encoding, errors=errors) as file_example:
        line = file_example.readline()
        while line:
            yield line.strip()
            line = file_example.readline()


def find_maximum_and_minimum(
        file_name: str, encoding: str = 'utf-8', errors: str = 'ignore'
) -> Tuple[int, int]:

    line_gen = line_generator(
        file_name, encoding=encoding, errors=errors
    )

    max_value = min_value = int(next(line_gen))
    for line in line_gen:
        number = int(line.strip())

        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number

    return max_value, min_value
