"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List, Set, Union


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Find in text 10 longest words consisting
    from largest amount of unique symbols
    """
    symbols_to_replace = '!"#$%&()*+,./:;<=>?@[\\]^_{|}~»«'
    words_set = set()

    def process_line(line: str, words_set: Set) -> None:
        """Delete useless symbols from string and get info about words"""
        for symbol in symbols_to_replace:
            line = line.replace(symbol, '')

        words_set_temp = set([word.strip('\t ') for word in line.split()])
        for word in words_set_temp:
            words_set.add((len(set(word)), len(word), word))

        return None

    # Process file line by line
    with open(file_path, 'rb') as text:
        line = text.readline().decode('unicode-escape')
        while line != '':
            line = line.strip('\r\n')
            while line.endswith('-'):  # Concatenate lines with word wrap
                line = line[:-1] + text.readline().decode('unicode-escape')
                line = line.strip('\r\n')
            process_line(line, words_set)
            line = text.readline().decode('unicode-escape')

    # Sort tuples: first by largest amount of unique symbols
    # second by word length
    sorted_words = sorted(words_set, reverse=True)
    final_words = [word_params[2] for word_params in sorted_words]

    if len(final_words) < 10:
        return final_words
    else:
        return final_words[:10]


def get_rarest_char(file_path: str) -> str:
    """Find rarest symbol for document"""
    symbols_dict = dict()

    with open(file_path, 'rb') as file_example:
        line = file_example.readline().decode('unicode-escape')
        while line != '':
            for symbol in line:
                if symbol in symbols_dict:
                    symbols_dict[symbol] += 1
                else:
                    symbols_dict[symbol] = 1

            line = file_example.readline().decode('unicode-escape')

    min_count = min(symbols_dict.values())
    rare_chars = filter(lambda x: x[1] == min_count, symbols_dict.items())
    rarest_char = sorted(rare_chars)[-1][0]

    return rarest_char


def count_punctuation_chars(file_path: str) -> int:
    """Count every punctuation char in document"""
    punctuation_number = 0
    punctuation_chars = '!",.-:;?\'()—…'

    with open(file_path, 'rb') as file_example:
        line = file_example.readline().decode('unicode-escape')
        while line != '':
            for symbol in line:
                if symbol in punctuation_chars:
                    punctuation_number += 1

            line = file_example.readline().decode('unicode-escape')

    return punctuation_number


def count_non_ascii_chars(file_path: str) -> int:
    """Count every non ascii char in document"""
    non_ascii_number = 0

    with open(file_path, 'rb') as file_example:
        line = file_example.readline().decode('unicode-escape')
        while line != '':
            for symbol in line:
                if not symbol.isascii():
                    non_ascii_number += 1

            line = file_example.readline().decode('unicode-escape')

    return non_ascii_number


def get_most_common_non_ascii_char(file_path: str) -> Union[str, None]:
    """Find most common non ascii char for document"""
    non_ascii = dict()

    with open(file_path, 'rb') as file_example:
        line = file_example.readline().decode('unicode-escape')
        while line != '':
            for symbol in line:
                if not symbol.isascii():
                    if symbol in non_ascii:
                        non_ascii[symbol] += 1
                    else:
                        non_ascii[symbol] = 1

            line = file_example.readline().decode('unicode-escape')

    if len(non_ascii) == 0:
        return None
    else:
        max_count = max(non_ascii.values())
        common_chars = filter(lambda x: x[1] == max_count, non_ascii.items())
        common_char = sorted(common_chars)[-1][0]
        return common_char
