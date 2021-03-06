from unittest.mock import Mock, patch

from homework7.hw2 import backspace_compare, collect_data


def test_collect_data_all_backspaces():
    """
    Testing if string full of '#' characters
    function will return empty string
    """
    test_string = '#####'
    correct_result = ''

    test_result = collect_data(test_string)

    assert test_result == correct_result


def test_collect_data_backspace_at_the_end():
    """
    Testing if string with '#' characters in the end
    function will cut only [-2] character from string
    """
    test_string = 'abc#'
    correct_result = 'ab'

    test_result = collect_data(test_string)

    assert test_result == correct_result


def test_collect_data_two_backspaces():
    """
    Testing if string contain '##' characters
    function will remove two following letters
    """
    test_string = 'afb##c#'
    correct_result = 'a'

    test_result = collect_data(test_string)

    assert test_result == correct_result


def test_collect_data_with_multiple_backspaces():
    """Testing function cut all characters before '#'"""
    test_string = 'ab#fs#c#'
    correct_result = 'af'

    test_result = collect_data(test_string)

    assert test_result == correct_result


def test_backspace_compare_when_strings_equal():
    """Testing function return True if strings are equal"""
    first_string = 'dummy_text'
    second_string = 'dummy_text'
    mock = Mock()
    mock.side_effect = ['dummy_text', 'dummy_text']

    with patch('homework7.hw2.process_string', mock):
        assert backspace_compare(first_string, second_string)


def test_backspace_compare_when_strings_not_equal():
    """Testing function return False if strings are not equal"""
    first_string = 'dummy'
    second_string = 'dummy_text'
    mock = Mock()
    mock.side_effect = ['dummy', 'dummy_text']

    with patch('homework7.hw2.process_string', mock):
        assert not backspace_compare(first_string, second_string)
