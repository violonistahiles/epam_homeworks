from unittest.mock import Mock

import pytest

from homework3.hw1 import CacheSizeError, cache


def test_func_called_once():
    """
    Testing that after caching result of the function,
    function don't invoke again"""
    mock_function = Mock()
    mock_function.return_value('dummy_result')
    some_input = 1

    test_funk = cache(times=1)(mock_function)
    _ = test_funk(some_input)
    _ = test_funk(some_input)

    mock_function.assert_called_once()


def test_cache_return_same_value():
    """
    Testing that after reading from cache result it is the same
    as function result
    """
    mock_function = Mock()
    mock_function.return_value('dummy_result')
    some_input = 1

    test_funk = cache(times=1)(mock_function)
    result_1 = test_funk(some_input)
    result_2 = test_funk(some_input)

    assert result_1 is result_2


def test_times_value_is_negative():
    """Testing that times argument should be positive int"""
    mock_function = Mock()
    mock_function.return_value('dummy_result')

    with pytest.raises(CacheSizeError):
        _ = cache(times=-5)(mock_function)


def test_times_value_is_not_int():
    """Testing that times argument should be positive int"""
    mock_function = Mock()
    mock_function.return_value('dummy_result')

    with pytest.raises(CacheSizeError):
        _ = cache(times='y')(mock_function)
