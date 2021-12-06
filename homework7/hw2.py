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


def process_string(string: str) -> str:

    cut_last = string.endswith('#')

    split_string = string.split('#')
    print(len(split_string))
    if len(split_string) == 1:
        if cut_last:
            return split_string[0][:-1]

    words = split_string[:-1]
    proc_words = [word[:-1] for word in words]
    if cut_last:
        proc_words.append(split_string[-1][:-1])
    else:
        proc_words.append(split_string[-1])

    return ''.join(proc_words)


def backspace_compare(first: str, second: str):

    first_result = process_string(first)
    print(first_result)
    second_result = process_string(second)
    print(second_result)

    return first_result == second_result


if __name__ == '__main__':
    s = "ab#c"
    t = "ad#c"
    print(backspace_compare(s, t), end='\n\n')

    s = "a##c"
    t = "#a#c"
    print(backspace_compare(s, t), end='\n\n')

    s = "a##casd#"
    t = "#a#casd#"
    print(backspace_compare(s, t), end='\n\n')

    s = "a#c"
    t = "b"
    print(backspace_compare(s, t))
