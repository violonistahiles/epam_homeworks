from homework2.hw3 import combinations


def test_combinations_with_three_lists():
    """Testing result of combinations with three lists"""
    test_input = [[1, 2], [3, 4], [5]]
    correct_result = [[1, 3, 5], [1, 4, 5], [2, 3, 5], [2, 4, 5]]

    result = combinations(*test_input)
    print(result)

    assert result == correct_result


def test_combinations_with_two_lists_of_one_element():
    """Testing result of combinations with two lists of one element"""
    test_input = [[1], [3]]
    correct_result = [[1, 3]]

    result = combinations(*test_input)

    assert result == correct_result


def test_combinations_with_one_list_of_one_element():
    """Testing result of combinations with one list of one element"""
    test_input = [[1]]
    correct_result = [[1]]

    result = combinations(*test_input)

    assert result == correct_result
