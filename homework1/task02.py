"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:

    fib_sequence = [0, 1]  # Initial Fibonacci sequence
    data_len = len(data) - 1
    k = 0
    while data[k] >= fib_sequence[0]:
        if data[k] == fib_sequence[0]:
            if k == data_len:
                return True
            else:
                k += 1
        else:
            if k > 0:
                return False

        fib_sequence.append(sum(fib_sequence))
        fib_sequence = fib_sequence[1:]
    else:
        return False
