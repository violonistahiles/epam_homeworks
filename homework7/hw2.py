"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""
from typing import Generator


def process_string(string: str) -> Generator:
    """
    Delete symbols in string according to backspacing

    :param string: String to process
    :type string: str
    :return: Generator for saved lettres
    :rtype: Generator
    """
    backspace_counter = 0

    for letter in reversed(string):
        if letter == '#':
            backspace_counter += 1
            continue

        if backspace_counter:
            backspace_counter -= 1
            continue

        yield letter


def collect_data(string: str) -> str:
    """
    Service function to form string from generated list

    :param string: String to process
    :type string: str
    :return: String after backspace processing
    :rtype: str
    """
    str_list = list(process_string(string))
    return ''.join(str_list)[::-1]


def backspace_compare(first: str, second: str) -> bool:
    """
    Compare two strings after processing backspace characters

    :param first: first string
    :type first: str
    :param second: second string
    :type second: str
    :return: Result of comparison of two strings after backspace processing
    :rtype: bool
    """
    first_result = collect_data(first)
    print(first_result)
    second_result = collect_data(second)
    print(second_result)

    return first_result == second_result


if __name__ == '__main__':
    s = "ab#c"
    t = "ad#c"
    print(backspace_compare(s, t))

    s = "a##c"
    t = "#a#c"
    print(backspace_compare(s, t))

    s = "####"
    t = "#a#c"
    print(backspace_compare(s, t))
