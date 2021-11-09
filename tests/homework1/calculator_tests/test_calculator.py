from homework1.sample_project.calculator.calc import check_power_of_2


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)


def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)


def test_zero_input_case():
    """Testing that input value 0 give False"""
    assert not check_power_of_2(0)


def test_one_input_case():
    """Testing that input value 1 give True"""
    assert check_power_of_2(1)


def test_negative_value_case():
    """Testing that negative input value give False"""
    assert not check_power_of_2(-56)


def test_negative_power_of_two_case():
    """Testing that negative power of 2 input False"""
    assert not check_power_of_2(-8)


def test_negative_alternative_of_positive_case():
    """Testing that negative power of 2 input False"""
    # Example: -7 -> -111, -8 -> -1000, -7 & -8 -> -1000
    assert not check_power_of_2(-7)
