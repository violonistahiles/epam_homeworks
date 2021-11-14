"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string

some_string = string.ascii_lowercase

assert = custom_range(some_string, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(some_string, 'g', 'p') == ['g', 'h', 'i', 'j', 'k',
                                                 'l', 'm', 'n', 'o']
assert = custom_range(some_string, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Iterable, List, Union


class NotAllowedError(Exception):
    def __init__(self):
        print('For Set and Dict not allowed to select start, stop and step')


class StepError(Exception):
    def __init__(self, start, stop, step, error_ind=2):
        if error_ind == 0:
            print(f'Start index of "{start}" should be greater then '
                  f'stop "{stop}" position index for step "{step}"')
        elif error_ind == 1:
            print(f'Start index of "{start}" should be lower then '
                  f'stop "{stop}" position index for step "{step}"')
        else:
            print(f'Step "{step}" of type {type(step)} should be int')


def custom_range(input_sequence: Iterable, *args: Union[str, int]) -> List:
    """
    Step through the elements of the iterable
    Arguments:
        :args: - any of follow sequences
        [stop], [start, stop], [start, stop, step]
    """
    # Set base parameters
    step = 1
    input_len = len(input_sequence)
    # Check if input sequence is unordered fata type
    if isinstance(input_sequence, dict) or isinstance(input_sequence, set):
        input_sequence = list(input_sequence)
        if len(args) > 0:
            raise NotAllowedError()

    # Set parameters for iteration
    if len(args) == 0:
        start = 0
        stop = input_len - 1
    elif len(args) == 1:
        start = 0
        stop = input_sequence.index(args[0])
    elif len(args) == 2:
        start = input_sequence.index(args[0])
        stop = input_sequence.index(args[1])
    else:
        start = input_sequence.index(args[0])
        stop = input_sequence.index(args[1])
        step = args[2]
        if not isinstance(step, int):
            raise StepError(start, stop, step)

    # Check if parameters are valid
    if start > stop and step > 0:
        raise StepError(start, stop, step, 1)
    elif start < stop and step < 0:
        raise StepError(start, stop, step, 0)

    # Iterate through elements
    while (start <= stop and step > 0) or (start >= stop and step < 0):
        yield input_sequence[start]
        start += step
        if start < 0:
            break


example_1 = {3: 1, 5: 2, 6: 4}
example_2 = set([4, 5, 6, 1, 7])
example_3 = [4, 5, 6, 1, 7]
example_4 = (4, 5, 6, 1, 7)

print(list(example_4))
print(list(custom_range(example_4, 7, 1, -2)))
