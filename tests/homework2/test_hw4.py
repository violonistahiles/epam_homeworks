from unittest.mock import Mock

from homework2.hw4 import cache


def func(a: int, b: int) -> int:
    return (a + b) ** 2


def test_cache_func_return_case():
    """Testing cache function returns the same value on equal input data"""
    cache_func = cache(func)
    test_input = 1, 2

    val_1 = cache_func(*test_input)
    val_2 = cache_func(*test_input)

    assert val_1 is val_2


def test_cache_func_call_case():
    """
    Testing that function inside cache function calls once
    on equal input data
    """
    test_input = 1, 2
    mock = Mock()
    mock.return_value = 'dummy_result'

    cache_func = cache(mock)

    _ = cache_func(*test_input)
    _ = cache_func(*test_input)

    mock.assert_called_once()
