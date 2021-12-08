from homework3.task04 import is_armstrong


def test_is_armstrong_when_number_is_not_int():
    """Testing that wrong input will return False"""
    assert not is_armstrong(5.2)


def test_is_armstrong_when_number_is_negative():
    """Testing that wrong input will return False"""
    assert not is_armstrong(-52)


def test_is_armstrong_when_number_is_armstrong():
    """Testing that Armstrong number is really Armstrong"""
    assert is_armstrong(407)


def test_is_armstrong_when_number_is_not_armstrong():
    """Testing that not Armstrong number is really not Armstrong"""
    assert not is_armstrong(123)
