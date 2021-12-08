"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import unicodedata
from collections import defaultdict
from typing import Dict, Iterator, List, Set, Union


def lines_generator(
        file_path: str, encoding: str = 'utf-8', errors: str = 'ignore'
) -> Iterator[str]:
    """Yield lines from text file"""
    with open(file_path, encoding=encoding, errors=errors) as text:
        line = text.readline()
        while line:
            while line.endswith('-\r\n') or line.endswith('-\n'):
                line = line[:line.rfind('-')] + text.readline()
            yield line
            line = text.readline()


def tokenize_line(line: str) -> Set[str]:
    """Return connected sequences of unicode word symbols"""
    word = ''
    words_set = set()
    for symbol in line:
        if unicodedata.category(symbol).startswith('L'):
            word += symbol
        else:
            if word:
                words_set.add(word)
            word = ''

    if word:
        words_set.add(word)

    return words_set


def get_longest_diverse_words(
        file_path: str, encoding: str = 'utf-8', errors: str = 'ignore'
) -> List[str]:
    """
    Find in text 10 longest words consisting
    from largest amount of unique symbols
    """
    words_set = set()
    line_gen = lines_generator(file_path, encoding, errors)

    # Process file line by line
    for line in line_gen:
        tmp_words_set = tokenize_line(line)
        for word in tmp_words_set:
            words_set.add((len(set(word)), len(word), word))

    # Sort tuples: first by largest amount of unique symbols
    # second by word length
    sorted_words = sorted(words_set, reverse=True)
    final_words = [word_params[2] for word_params in sorted_words]

    if len(final_words) < 10:
        return final_words
    else:
        return final_words[:10]


def get_rarest_char(
    file_path: str, encoding: str = 'utf-8', errors: str = 'ignore'
) -> str:
    """Find rarest symbol for document"""
    symbols_dict = defaultdict(int)

    line_gen = lines_generator(file_path, encoding, errors)

    # Process file line by line
    for line in line_gen:
        for symbol in line:
            symbols_dict[symbol] += 1

    min_count = min(symbols_dict.values())
    rare_chars = filter(lambda x: x[1] == min_count, symbols_dict.items())
    rarest_char = sorted(rare_chars)[-1][0]

    return rarest_char


def count_punctuation_chars(
    file_path: str, encoding: str = 'utf-8', errors: str = 'ignore'
) -> int:
    """Count every punctuation char in document"""
    punctuation_number = 0

    line_gen = lines_generator(file_path, encoding, errors)

    # Process file line by line
    for line in line_gen:
        for symbol in line:
            if unicodedata.category(symbol).startswith('P'):
                punctuation_number += 1

    return punctuation_number


def count_non_ascii_chars(
    file_path: str, encoding: str = 'utf-8', errors: str = 'ignore'
) -> int:
    """Count every non ascii char in document"""
    non_ascii_number = 0

    line_gen = lines_generator(file_path, encoding, errors)

    # Process file line by line
    for line in line_gen:
        for symbol in line:
            if not symbol.isascii():
                non_ascii_number += 1

    return non_ascii_number


def get_most_common_non_ascii_char(
    file_path: str, encoding: str = 'utf-8', errors: str = 'ignore'
) -> Union[str, None]:
    """Find most common non ascii char for document"""

    def get_most_common(input_dict: Dict) -> str:
        """Return most common element from dict"""
        max_count = max(input_dict.values())
        common_chars = filter(lambda x: x[1] == max_count, input_dict.items())
        common_char = sorted(common_chars)[-1][0]
        return common_char

    non_ascii = defaultdict(int)

    line_gen = lines_generator(file_path, encoding, errors)

    # Process file line by line
    for line in line_gen:
        for symbol in line:
            if not symbol.isascii():
                non_ascii[symbol] += 1

    if len(non_ascii) == 0:
        return None
    else:
        return get_most_common(non_ascii)
