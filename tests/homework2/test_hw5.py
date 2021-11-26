import string

import pytest

from homework2.hw5 import (NotAllowedError, StepError, custom_range,
                           set_parameters)


def test_parse_parameters_with_wrong_step_case():
    """Testing parsing parameters get error when step direction is wrong"""
    test_example = [4, 5, 6, 1, 7]
    args = [5, 7, -2]

    with pytest.raises(StepError):
        set_parameters(test_example, *args)


def test_parse_parameters_with_str_step_case():
    """Testing parsing parameters get error when step is not int"""
    test_example = [4, 5, 6, 1, 7]
    args = [5, 7, 't']

    with pytest.raises(StepError):
        set_parameters(test_example, *args)


def test_parse_parameters_with_start_stop_step():
    """Testing parsing parameters works ok"""
    test_example = [4, 5, 6, 1, 7]
    args = [5, 7, 2]

    start, stop, step = set_parameters(test_example, *args)

    assert start == 1
    assert stop == 4
    assert step == 2


def test_parse_parameters_with_start_stop():
    """Testing parsing parameters works ok"""
    test_example = [4, 5, 6, 1, 7]
    args = [5, 7]

    start, stop, step = set_parameters(test_example, *args)

    assert start == 1
    assert stop == 4
    assert step == 1


def test_parse_parameters_with_stop():
    """Testing parsing parameters works ok"""
    test_example = [4, 5, 6, 1, 7]
    args = [7]

    start, stop, step = set_parameters(test_example, *args)

    assert start == 0
    assert stop == 4
    assert step == 1


def test_input_dict_with_args_case():
    """
    Testing custom range get error when iterable is
    Dict and passed additional args
    """
    test_example = {3: 1, 5: 2, 6: 4}
    args = [5, 6, 2]

    with pytest.raises(NotAllowedError):
        list(custom_range(test_example, *args))


def test_input_set_with_args_case():
    """
    Testing custom range get error when iterable is
    Set and passed additional args
    """
    test_example = {4, 5, 6, 1, 7}
    args = [5, 7, 2]

    with pytest.raises(NotAllowedError):
        list(custom_range(test_example, *args))


def test_input_tuple_with_start_and_stop_case():
    """
    Testing custom range works correctly when iterable is tuple
    and start and stop arguments are specified
    """
    test_example = [4, 5, 6, 1, 7]
    args = [5, 1]
    correct_result = [5, 6, 1]

    result = list(custom_range(test_example, *args))

    assert result == correct_result


def test_input_list_with_start_stop_and_negative_step_case():
    """
    Testing custom range works correctly when iterable is list
    and start, stop and step arguments are specified
    """
    test_example = [4, 5, 6, 1, 7]
    args = [1, 5, -1]
    correct_result = [1, 6, 5]

    result = list(custom_range(test_example, *args))

    assert result == correct_result


def test_input_string_with_start_stop_and_negative_step_case():
    """
    Testing custom range works correctly when iterable is string
    and start, stop and step arguments are specified
    """
    test_example = string.ascii_lowercase
    args = ['p', 'g', -2]
    correct_result = ['p', 'n', 'l', 'j', 'h']

    result = list(custom_range(test_example, *args))

    assert result == correct_result
