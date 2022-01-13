from homework9.hw3 import universal_file_counter


def test_counting_lines_from_files(tmp_path):
    """Testing universal_file_counter counts lines from files correctly"""
    test_path = tmp_path / 'sub'
    test_path.mkdir()
    text_1 = '1\n3\n5'
    text_2 = '2\n4\n6'
    path_1 = test_path / 'test_text_1.txt'
    path_1.write_text(text_1)
    path_2 = test_path / 'test_text_2.txt'
    path_2.write_text(text_2)
    file_extension = '.txt'
    correct_result = 6

    test_result = universal_file_counter(test_path, file_extension)

    assert test_result == correct_result


def test_counting_tokens_from_files(tmp_path):
    """Testing universal_file_counter counts tokens from files correctly"""
    test_path = tmp_path / 'sub'
    test_path.mkdir()
    text_1 = '1\n3 5\n5'
    text_2 = '2\n4\n6'
    path_1 = test_path / 'test_text_1.txt'
    path_1.write_text(text_1)
    path_2 = test_path / 'test_text_2.txt'
    path_2.write_text(text_2)
    file_extension = '.txt'
    correct_result = 7

    test_result = universal_file_counter(test_path, file_extension, str.split)

    assert test_result == correct_result


def test_reading_only_specified_files_extension(tmp_path):
    """
    Testing universal_file_counter reads files
    only with specified file extension
    """
    test_path = tmp_path / 'sub'
    test_path.mkdir()
    text_1 = '1\n3 5\n5'
    text_2 = '2\n4\n6'
    path_1 = test_path / 'test_text_1.txt'
    path_1.write_text(text_1)
    path_2 = test_path / 'test_text_2.bin'
    path_2.write_text(text_2)
    file_extension = '.txt'
    correct_result = 3

    test_result = universal_file_counter(test_path, file_extension)

    assert test_result == correct_result


def test_when_tokenizer_is_generator(tmp_path):
    """
    Testing universal_file_counter counts tokens
    correctly when tokenizer is generator
    """
    def simple_generator(line: str):
        symbols = line.split()
        for symbol in symbols:
            yield symbol

    test_path = tmp_path / 'sub'
    test_path.mkdir()
    text_1 = '1\n3 5\n5'
    text_2 = '2\n4 8\n6'
    path_1 = test_path / 'test_text_1.txt'
    path_1.write_text(text_1)
    path_2 = test_path / 'test_text_2.txt'
    path_2.write_text(text_2)
    file_extension = '.txt'
    tokenizer = simple_generator
    correct_result = 8

    test_result = universal_file_counter(test_path, file_extension, tokenizer)

    assert test_result == correct_result


def test_counting_lines_from_files_when_files_are_empty(tmp_path):
    """
    Testing universal_file_counter counts lines
    from files correctly when files are empty"""
    test_path = tmp_path / 'sub'
    test_path.mkdir()
    text_1 = ''
    text_2 = ''
    path_1 = test_path / 'test_text_1.txt'
    path_1.write_text(text_1)
    path_2 = test_path / 'test_text_2.txt'
    path_2.write_text(text_2)
    file_extension = '.txt'
    correct_result = 0

    test_result = universal_file_counter(test_path, file_extension)

    assert test_result == correct_result
