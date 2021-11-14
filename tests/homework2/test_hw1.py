from unittest import mock

from homework2.hw1 import *


def test_longest_diverse_words_when_words_less_then_ten():
    """Testing algorithm when there are less then ten words in document"""
    dummy_path = 'some_path'
    text_line_1 = 'abcdef abc acbdabc abcdcd\n'
    text_line_2 = 'abcdefg aaaa\n'
    test_text = text_line_1 + text_line_2
    correct_result = ['abcdefg', 'abcdef', 'acbdabc', 'abcdcd', 'abc', 'aaaa']

    mock_open = mock.mock_open(read_data=test_text.encode('unicode-escape'))

    with mock.patch('homework2.hw1.open', mock_open):
        test_result = get_longest_diverse_words(dummy_path)

    assert test_result == correct_result


def test_longest_diverse_words_when_words_more_then_ten():
    """Testing algorithm when there are more then ten words in document"""
    dummy_path = 'some_path'
    text_line_1 = 'abc a ab abcd abb aff\n'
    text_line_2 = 'xyz x xy xyzu xyy xll\n'
    test_text = text_line_1 + text_line_2
    correct_result = ['xyzu', 'abcd', 'xyz', 'abc', 'xyy',
                      'xll', 'aff', 'abb', 'xy', 'ab']

    mock_open = mock.mock_open(read_data=test_text.encode('unicode-escape'))

    with mock.patch('homework2.hw1.open', mock_open):
        test_result = get_longest_diverse_words(dummy_path)
    print(test_result)

    assert test_result == correct_result


def test_rarest_char_case():
    """Testing that algorithm works fine on standard data"""
    dummy_path = 'some_path'
    text_line_1 = 'fmdo gis pos a fposd\n'
    text_line_2 = 'fd smj fsdi fmois fjoi z\n'
    test_text = text_line_1 + text_line_2
    correct_result = 'z'

    mock_open = mock.mock_open(read_data=test_text.encode('unicode-escape'))

    with mock.patch('homework2.hw1.open', mock_open):
        test_result = get_rarest_char(dummy_path)
    print(test_result)

    assert test_result == correct_result


def test_count_punctuation_chars_case():
    """Testing that algorithm works fine on standard data"""
    dummy_path = 'some_path'
    text_line_1 = 'fmdo, gis! pos. a- fposd\n'
    text_line_2 = 'fd smj fsdi fm(ois) fjoi z"\n'
    test_text = text_line_1 + text_line_2
    correct_result = 7

    mock_open = mock.mock_open(read_data=test_text.encode('unicode-escape'))

    with mock.patch('homework2.hw1.open', mock_open):
        test_result = count_punctuation_chars(dummy_path)
    print(test_result)

    assert test_result == correct_result


def test_count_punctuation_chars_when_punctuation_chars_not_exist():
    """Testing algorithm when there are no punctuation chars in document"""
    dummy_path = 'some_path'
    text_line_1 = 'fmdo gis pos a fposd\n'
    text_line_2 = 'fd smj fsdi fmois fjoi z\n'
    test_text = text_line_1 + text_line_2
    correct_result = 0

    mock_open = mock.mock_open(read_data=test_text.encode('unicode-escape'))

    with mock.patch('homework2.hw1.open', mock_open):
        test_result = count_punctuation_chars(dummy_path)
    print(test_result)

    assert test_result == correct_result


def test_count_non_ascii_chars_case():
    """Testing that algorithm works fine on standard data"""
    dummy_path = 'some_path'
    text_line_1 = 'fmdo, gis! pos. a\u00f6- fposd\n'
    text_line_2 = 'fd smj f\u00dfsdi fm(ois) \u00e4fjoi z"\n'
    test_text = text_line_1 + text_line_2
    correct_result = 3

    mock_open = mock.mock_open(read_data=test_text.encode('unicode-escape'))

    with mock.patch('homework2.hw1.open', mock_open):
        test_result = count_non_ascii_chars(dummy_path)
    print(test_result)

    assert test_result == correct_result


def test_count_non_ascii_chars_when_non_ascii_not_exist():
    """Testing algorithm when there are no non ascii symbols in document"""
    dummy_path = 'some_path'
    text_line_1 = 'fmdo, gis! pos. a- fposd\n'
    text_line_2 = 'fd smj fsdi fm(ois) fjoi z"\n'
    test_text = text_line_1 + text_line_2
    correct_result = 0

    mock_open = mock.mock_open(read_data=test_text.encode('unicode-escape'))

    with mock.patch('homework2.hw1.open', mock_open):
        test_result = count_non_ascii_chars(dummy_path)
    print(test_result)

    assert test_result == correct_result


def get_most_common_non_ascii_char():
    """Testing that algorithm works fine on standard data"""
    dummy_path = 'some_path'
    text_line_1 = 'f\u00e4mdo, g\u00f6is! pos. a\u00f6- fposd\n'
    text_line_2 = 'fd smj f\u00dfsdi fm(ois) \u00e4fjo\u00f6i z"\n'
    test_text = text_line_1 + text_line_2
    correct_result = '\u00f6'

    mock_open = mock.mock_open(read_data=test_text.encode('unicode-escape'))

    with mock.patch('homework2.hw1.open', mock_open):
        test_result = get_most_common_non_ascii_char(dummy_path)
    print(test_result)

    assert test_result == correct_result


def get_most_common_non_ascii_when_non_ascii_not_exist():
    """Testing algorithm when there are no non ascii symbols in document"""
    dummy_path = 'some_path'
    text_line_1 = 'fmdo, gis! pos. a- fposd\n'
    text_line_2 = 'fd smj fsdi fm(ois) fjoi z"\n'
    test_text = text_line_1 + text_line_2

    mock_open = mock.mock_open(read_data=test_text.encode('unicode-escape'))

    with mock.patch('homework2.hw1.open', mock_open):
        test_result = get_most_common_non_ascii_char(dummy_path)
    print(test_result)

    assert not test_result
