from typing import Any, Callable

from homework5.task02 import save_parameters


def print_result(func: Callable):
    @save_parameters(func)
    def wrapper(*args, **kwargs) -> Any:
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def some_func() -> int:
    """This is test func"""
    return 5


def test_save_parameters(capsys):
    """Testing save_parameters decorator works fine"""
    assert some_func.__doc__ == 'This is test func'
    assert some_func.__name__ == 'some_func'
    assert some_func() == 5
    assert capsys.readouterr().out == '5\n'
