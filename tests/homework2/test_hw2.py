from homework2.hw2 import major_and_minor_elem


def test_standard_case():
    """Testing """
    test_list = [3,2,3]
    correct_result = 3, 2

    result = major_and_minor_elem(test_list)

    assert result == correct_result


def test_standard_case2():
    """Testing """
    test_list = [2,2,1,1,1,2,2]
    correct_result = 2, 1

    result = major_and_minor_elem(test_list)

    assert result == correct_result