"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:

    fib_sequence_limit = 3
    if len(data) < fib_sequence_limit:
        return False

    fib_1, fib_2 = 0, 1  # Initial Fibonacci sequence
    data_len = len(data) - 1
    k = 0
    while data[k] >= fib_1:
        is_equal = (data[k] == fib_1)

        if is_equal and k == data_len:
            return True
        elif is_equal and k < data_len:
            k += 1
        elif k > 0:
            return False

        fib_1, fib_2 = fib_2, fib_1 + fib_2
    else:
        return False
