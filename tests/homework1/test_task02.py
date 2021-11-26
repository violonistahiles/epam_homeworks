from homework1.task02 import check_fibonacci, fib_generator, peek_first


def test_fib_generator():
    """Testing Fibonacci generator works ok"""
    fib_sequence = [5, 8, 13, 21, 34]
    for gen_element, true_element in zip(fib_generator(5), fib_sequence):
        assert gen_element == true_element


def test_peek_first():
    """Testing peek_first generator works ok"""
    fib_sequence = [5, 8, 13, 21, 34]
    data_generator = peek_first(fib_sequence)

    first = next(data_generator)
    second = next(data_generator)
    third = next(data_generator)

    assert first == second
    assert first != third


def test_data_is_empty_case():
    """Testing that empty data will return False"""
    data_to_process = []
    assert not check_fibonacci(data_to_process)


def test_fib_sequence_case():
    """Testing that actual Fibonacci sequence give True"""
    data_to_process = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
                       233, 377, 610, 987, 1597, 2584, 4181, 6765]
    assert check_fibonacci(data_to_process)


def test_not_a_fib_sequence_case():
    """Testing that not a Fibonacci sequence give False"""
    data_to_process = [0, 1, 1, 7]
    assert not check_fibonacci(data_to_process)


def test_single_value_from_fib_sequence_case():
    """Testing that single number from actual Fibonacci sequence give True"""
    data_to_process = [2584]
    assert not check_fibonacci(data_to_process)


def test_single_value_not_from_fib_sequence_case():
    """Testing that random number not from Fibonacci sequence give False"""
    data_to_process = [555]
    assert not check_fibonacci(data_to_process)


def test_negative_number_at_start_in_fib_sequence_case():
    """Testing that lower then 0 value at the start of sequence give False"""
    data_to_process = [-1, 3, 5, 8]
    assert not check_fibonacci(data_to_process)


def test_fib_sequence_with_missing_value_case():
    """Testing that actual Fibonacci sequence with missing value give False"""
    data_to_process = [1, 1, 2, 3, 8, 13]
    assert not check_fibonacci(data_to_process)
