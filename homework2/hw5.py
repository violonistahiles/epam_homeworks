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
from typing import Iterable, Iterator, Sequence, Tuple, Union


class NotAllowedError(Exception):
    """For Set and Dict not allowed to select start, stop and step"""


class StepError(Exception):
    """Raise Error if something wrong with start, stop or step"""

    def __init__(self, start, stop, step, error_ind=2):
        if error_ind == 0:
            self.massage = (f'Start index of "{start}" must be'
                            f' greater then stop "{stop}"'
                            f' index for step "{step}"')
        elif error_ind == 1:
            self.massage = (f'Start index of "{start}" must be'
                            f' lower then stop "{stop}"'
                            f' index for step "{step}"')
        else:
            self.massage = (f'Step "{step}" of type'
                            f' {type(step)} must be int')

    def __str__(self):
        return self.massage


def set_parameters(input_sequence: Sequence,
                   *args: Tuple[Union[str, int], ...]) -> Tuple[int, int, int]:
    """
        Parse parameters for iteration from args
        Arguments:
        :args: - any of following sequences
        [stop], [start, stop], [start, stop, step]
    """
    # Set base parameters
    step = 1
    input_len = len(input_sequence)

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

    return start, stop, step


def custom_range(input_sequence: Iterable, *args: Union[str, int]) -> Iterator:
    """
    Step through the elements of the iterable
    Arguments:
        :args: - any of following sequences
        [stop], [start, stop], [start, stop, step]
    """
    # Check if input sequence is unordered fata type
    if isinstance(input_sequence, dict) or isinstance(input_sequence, set):
        input_sequence = list(input_sequence)
        if len(args) > 0:
            raise NotAllowedError()

    # Get parameters for iteration
    start, stop, step = set_parameters(input_sequence, *args)

    # Iterate through elements
    while (start <= stop and step > 0) or (start >= stop and step < 0):
        yield input_sequence[start]
        start += step
        if start < 0:
            break
