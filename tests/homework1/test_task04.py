from homework1.task04 import check_sum_of_four


def test_program_return_right_value():
    """Testing program works correctly with input data"""
    a = [5]
    b = [5]
    c = [-5]
    d = [-5]
    correct_result = 1

    result = check_sum_of_four(a, b, c, d)

    assert result == correct_result


def test_program_with_multiple_identical_combinations_in_first_subset():
    """Testing program works correctly in case of multiple
     identical combinations of equal value in first subset
     """
    a = [5, 2, 6]
    b = [5, 8, 6]
    c = [25, 9, 10]
    d = [4, 7, -35]
    correct_result = 2

    result = check_sum_of_four(a, b, c, d)

    assert result == correct_result


def test_program_with_multiple_identical_combinations_in_second_subset():
    """Testing program works correctly in case of multiple
     identical combinations of equal value in second subset
     """
    a = [5, 3, 6]
    b = [5, 6, 8]
    c = [25, -6, 9]
    d = [-35, -4, 7]
    correct_result = 2

    result = check_sum_of_four(a, b, c, d)

    assert result == correct_result


def test_program_with_multiple_identical_combinations_in_both_subsets():
    """Testing program works correctly in case of multiple
     identical combinations of equal value in both subsets
     """
    a = [5, 2, 6]
    b = [5, 8, 6]
    c = [25, -6, 9]
    d = [-35, -4, 7]
    correct_result = 4

    result = check_sum_of_four(a, b, c, d)

    assert result == correct_result


def test_program_with_all_variants_of_sum():
    """Testing program works correctly in case of multiple
     identical combinations of equal value in both subsets
     """
    a = [5, 2, 100]
    b = [5, 8, -100]
    c = [25, -6, 100]
    d = [-35, -4, -100]
    correct_result = 5

    result = check_sum_of_four(a, b, c, d)

    assert result == correct_result


def test_zero_tuples_number_case():
    """Testing program returns zero when
    there are no subsets equal to zero
    """
    a = [5, 7]
    b = [6, 6]
    c = [25, 56]
    d = [4, 104]
    correct_result = 0

    result = check_sum_of_four(a, b, c, d)

    assert result == correct_result
