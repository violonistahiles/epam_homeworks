"""
Create parametrized decorator that remembers other function output value
and give it out times number only.

@cache(times=2)
def f():
    return input('? ')

>>> f()
? 1
'1'
>>> f()      # will remember previous value
'1'
>>> f()      # but use it up to two times only
'1'
>>> f()
? 2
'2'
"""
from typing import Any, Callable


class CacheSizeError(Exception):
    def __init__(self):
        print('Argument "times" should be int and greater then 0')


def cache(times: int) -> Callable:
    """Cache function result for n invokes"""

    if not isinstance(times, int) or times <= 0:
        raise CacheSizeError()

    cache_value = []
    cache_size = []

    def wrapper(func: Callable) -> Callable:
        def inner_wrapper(*args) -> Any:
            if len(cache_size) > 0 and cache_size[0] >= 1:
                cache_size[0] -= 1
                return cache_value[0]
            else:
                result = func(*args)

                if len(cache_value) == 0:
                    cache_value.append(result)
                else:
                    cache_value[0] = result

                if len(cache_size) == 0:
                    cache_size.append(times)
                else:
                    cache_size[0] = times

                return result

        return inner_wrapper

    return wrapper
