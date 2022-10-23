"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


@contextmanager
def simple_context_manager(exception: Exception):
    """
    Context manager function witch suppresses passed exception

    :param exception: Exception type to suppresses
    :type exception: Exception
    """
    try:
        yield
    except exception:
        pass


class SimpleContextManager:
    """
    Context manager class witch suppresses passed exception
    """
    def __init__(self, exception: Exception):
        """
        :param exception: Exception type to suppresses
        :type exception: Exception
        """
        self._exception_to_ignore = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._exception_to_ignore == exc_type:
            return True
