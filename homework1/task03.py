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


class NotIntError(ValueError):
    """Error if line in text file can't be converted to integer"""
    ...


def line_generator(
        file_name: str, encoding: str = 'utf-8', errors: str = 'ignore'
) -> str:
    """Iterate through lines in text file"""
    with open(file_name, encoding=encoding, errors=errors) as file_example:
        line = file_example.readline()
        while line:
            try:
                yield int(line.strip())
            except ValueError:
                raise NotIntError('Sequence elements should be integers')
            line = file_example.readline()


def find_maximum_and_minimum(
        file_name: str, encoding: str = 'utf-8', errors: str = 'ignore'
) -> Tuple[int, int]:

    line_gen = line_generator(
        file_name, encoding=encoding, errors=errors
    )

    max_value = min_value = next(line_gen)
    for number in line_gen:

        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number

    return max_value, min_value
