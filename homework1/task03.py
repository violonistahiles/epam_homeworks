"""
Write down the function, which reads input line-by-line, and find maximum and
minimum values. Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:

    with open(file_name) as file_example:
        # Get first line as initial value
        start_number_str = file_example.readline().strip()
        min_value = int(start_number_str)
        max_value = min_value
        # Process other lines and compare values
        for line in file_example:
            number = int(line.strip())

            if number < min_value:
                min_value = number
            if number > max_value:
                max_value = number

    return min_value, max_value


test_path = 'C://Users/kurushin/Desktop/NN/python_practice/epam/hm1_task3.txt'
result = find_maximum_and_minimum(test_path)
print(result)