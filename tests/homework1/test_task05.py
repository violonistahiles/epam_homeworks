from homework1.task05 import find_maximal_subarray_sum


def test_default_case():
    """Testing program workflow with default input"""
    nums_test = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    result = find_maximal_subarray_sum(nums_test, k)

    assert result == 16


def test_nums_contain_zero_elements_case():
    """Testing program with no elements in nums list"""
    nums_test = []
    k = 3

    result = find_maximal_subarray_sum(nums_test, k)

    assert result is None


def test_nums_contain_one_element_case():
    """Testing program with one element in nums list"""
    nums_test = [5]
    k = 3

    result = find_maximal_subarray_sum(nums_test, k)

    assert result == 5


def test_k_value_greater_then_nums_length_case():
    """Testing program with k argument value grater then length of nums"""
    nums_test = [5, 3]
    k = 3

    result = find_maximal_subarray_sum(nums_test, k)

    assert result == 8


def test_k_value_is_one_case():
    """Testing program with k argument value equal to one"""
    nums_test = [5, 3, 34]
    k = 1

    result = find_maximal_subarray_sum(nums_test, k)

    assert result == 34


def test_k_value_less_then_zero_case():
    """Testing program with k argument value less then zero"""
    nums_test = [5, 3, 34]
    k = -1

    result = find_maximal_subarray_sum(nums_test, k)

    assert result is None
