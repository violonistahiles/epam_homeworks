import pytest

from homework9.hw2 import SimpleContextManager, simple_context_manager


def test_context_manager_function_when_passed_exception_occurred():
    """
    Testing that passes to context manager function exception is suppressed
    """
    a = []
    correct_result = [10]

    with simple_context_manager(IndexError):
        a.append(10)
        _ = a[2]

    assert correct_result == a


def test_context_manager_function_when_different_exception_occurred():
    """
    Testing that different from passes to context manager function exception
    will processed normally
    """
    a = ['a']

    with pytest.raises(ValueError):
        with simple_context_manager(IndexError):
            a[0] = int(a[0])


def test_context_manager_function_when_exception_did_not_occurred():
    """
    Testing that without occurred exception
    context manager function works as expected
    """
    a = ['10']

    with simple_context_manager(IndexError):
        a[0] = int(a[0])

    assert a[0] == 10


def test_context_manager_class_when_passed_exception_occurred():
    """
    Testing that passes to context manager class exception is suppressed
    """
    a = []
    correct_result = [10]

    with SimpleContextManager(IndexError):
        a.append(10)
        _ = a[2]

    assert correct_result == a


def test_context_manager_class_when_different_exception_occurred():
    """
    Testing that different from passes to context manager class exception
    will processed normally
    """
    a = ['a']

    with pytest.raises(ValueError):
        with SimpleContextManager(IndexError):
            a[0] = int(a[0])


def test_context_manager_class_when_exception_did_not_occurred():
    """
    Testing that without occurred exception
    context manager class works as expected
    """
    a = ['10']

    with SimpleContextManager(IndexError):
        a[0] = int(a[0])

    assert a[0] == 10
