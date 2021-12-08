from homework2.hw1 import (count_non_ascii_chars, count_punctuation_chars,
                           get_longest_diverse_words,
                           get_most_common_non_ascii_char, get_rarest_char,
                           lines_generator, tokenize_line)


def test_line_generator(tmpdir):
    """Testing line_generator works fine"""
    text_line_1 = 'abcdef abc acbdabc abcdcd\n'
    text_line_2 = 'abcdefg aaaa\n'
    test_text = text_line_1 + text_line_2
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)
    correct_result = ['abcdef abc acbdabc abcdcd\n', 'abcdefg aaaa\n']

    test_result = list(lines_generator(tmp_path))

    assert test_result == correct_result


def test_line_generator_with_empty_line(tmpdir):
    """Testing line_generator works fine with empty lines in file"""
    text_line_1 = 'abcdef abc acbdabc abcdcd\n'
    text_line_2 = '\n'
    text_line_3 = 'abcdefg aaaa\n'
    test_text = text_line_1 + text_line_2 + text_line_3
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)
    correct_result = ['abcdef abc acbdabc abcdcd\n', '\n', 'abcdefg aaaa\n']

    test_result = list(lines_generator(tmp_path))

    assert test_result == correct_result


def test_line_generator_with_word_wrap(tmpdir):
    """Testing line_generator works fine"""
    text_line_1 = 'abcdef abc acbdabc abcdcd-\n'
    text_line_2 = 'abcdefg aaaa\n'
    test_text = text_line_1 + text_line_2
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)
    correct_result = ['abcdef abc acbdabc abcdcdabcdefg aaaa\n']

    test_result = list(lines_generator(tmp_path))

    assert test_result == correct_result


def test_tokenize_line():
    """Testing line_generator works fine"""
    text_line_1 = 'abcdef abc \n'
    text_line_2 = 'abcdefg aaaa\n'
    test_text = text_line_1 + text_line_2
    correct_result = {'abcdefg', 'abcdef', 'abc', 'aaaa'}

    test_result = tokenize_line(test_text)

    assert test_result == correct_result


def test_longest_diverse_words_when_words_less_then_ten(tmpdir):
    """Testing algorithm when there are less then ten words in document"""
    text_line_1 = 'abcdef abc acbdabc abcdcd\n'
    text_line_2 = 'abcdefg aaaa\n'
    test_text = text_line_1 + text_line_2
    correct_result = ['abcdefg', 'abcdef', 'acbdabc', 'abcdcd', 'abc', 'aaaa']
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)

    test_result = get_longest_diverse_words(tmp_path)

    assert test_result == correct_result


def test_longest_diverse_words_when_words_more_then_ten(tmpdir):
    """Testing algorithm when there are more then ten words in document"""
    text_line_1 = 'abc a ab abcd abb aff\n'
    text_line_2 = 'xyz x xy xyzu xyy xll\n'
    test_text = text_line_1 + text_line_2
    correct_result = ['xyzu', 'abcd', 'xyz', 'abc', 'xyy',
                      'xll', 'aff', 'abb', 'xy', 'ab']
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)

    test_result = get_longest_diverse_words(tmp_path)

    assert test_result == correct_result


def test_rarest_char_case(tmpdir):
    """Testing that algorithm works fine on standard data"""
    text_line_1 = 'fmdo gis pos a fposd\n'
    text_line_2 = 'fd smj fsdi fmois fjoi z\n'
    test_text = text_line_1 + text_line_2
    correct_result = 'z'
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)

    test_result = get_rarest_char(tmp_path)

    assert test_result == correct_result


def test_count_punctuation_chars_case(tmpdir):
    """Testing that algorithm works fine on standard data"""
    text_line_1 = 'fmdo, gis! pos. a- fposd\n'
    text_line_2 = 'fd smj fsdi fm(ois) fjoi z"\n'
    test_text = text_line_1 + text_line_2
    correct_result = 7
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)

    test_result = count_punctuation_chars(tmp_path)

    assert test_result == correct_result


def test_count_punctuation_chars_when_punctuation_chars_not_exist(tmpdir):
    """Testing algorithm when there are no punctuation chars in document"""
    text_line_1 = 'fmdo gis pos a fposd\n'
    text_line_2 = 'fd smj fsdi fmois fjoi z\n'
    test_text = text_line_1 + text_line_2
    correct_result = 0
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)

    test_result = count_punctuation_chars(tmp_path)

    assert test_result == correct_result


def test_count_non_ascii_chars_case(tmpdir):
    """Testing that algorithm works fine on standard data"""
    encoding = 'unicode_escape'
    errors = 'ignore'
    text_line_1 = 'fmdo, gis! pos. a\u00f6- fposd\n'
    text_line_2 = 'fd smj f\u00dfsdi fm(ois) \u00e4fjoi z"\n'
    test_text = text_line_1 + text_line_2
    correct_result = 3
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text.encode(encoding))

    test_result = count_non_ascii_chars(tmp_path, encoding, errors)

    assert test_result == correct_result


def test_count_non_ascii_chars_when_non_ascii_not_exist(tmpdir):
    """Testing algorithm when there are no non ascii symbols in document"""
    text_line_1 = 'fmdo, gis! pos. a- fposd\n'
    text_line_2 = 'fd smj fsdi fm(ois) fjoi z"\n'
    test_text = text_line_1 + text_line_2
    correct_result = 0
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)

    test_result = count_non_ascii_chars(tmp_path)

    assert test_result == correct_result


def get_most_common_non_ascii_char_case(tmpdir):
    """Testing that algorithm works fine on standard data"""
    encoding = 'unicode_escape'
    errors = 'ignore'
    text_line_1 = 'f\u00e4mdo, g\u00f6is! pos. a\u00f6- fposd\n'
    text_line_2 = 'fd smj f\u00dfsdi fm(ois) \u00e4fjo\u00f6i z"\n'
    test_text = text_line_1 + text_line_2
    correct_result = '\u00f6'
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text.encode(encoding))

    test_result = get_most_common_non_ascii_char(tmp_path, encoding, errors)

    assert test_result == correct_result


def get_most_common_non_ascii_when_non_ascii_not_exist(tmpdir):
    """Testing algorithm when there are no non ascii symbols in document"""
    text_line_1 = 'fmdo, gis! pos. a- fposd\n'
    text_line_2 = 'fd smj fsdi fm(ois) fjoi z"\n'
    test_text = text_line_1 + text_line_2
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)

    test_result = get_most_common_non_ascii_char(tmp_path)

    assert not test_result
