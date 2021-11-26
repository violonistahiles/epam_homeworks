"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Iterable, Iterator, Sequence

empty_element = object()


def fib_generator(start_item: int) -> Iterator[int]:
    """Generate fibonacci sequence element"""
    i, j = 0, 1
    while True:
        if i >= start_item:
            yield i
        i, j = j, i + j


def peek_first(data_sequence: Iterable[int]) -> Iterator[int]:
    """Generate first element from sequence twice"""
    first = True
    for element in data_sequence:
        if first:
            first = False
            yield element
        yield element


def check_fibonacci(data: Sequence[int]) -> bool:
    """Check if sequence with number of elements larger then 3 is Fibonacci"""
    if len(data) < 3:
        return False

    data = peek_first(data)
    first_element = next(data, empty_element)
    if first_element == empty_element:
        return False
    for fib_element, data_element in zip(fib_generator(first_element), data):
        if fib_element != data_element:
            return False
    return True
