"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections import OrderedDict
from typing import Callable


def cache(func: Callable) -> Callable:
    """Cache input arguments and result of func"""
    cache_dict = OrderedDict()
    cache_size = 100

    def wrapper(*args):
        if args in cache_dict:
            return cache_dict[args]
        else:
            result = func(*args)
            cache_dict[args] = result
            if len(cache_dict) > cache_size:
                cache_dict.popitem(last=False)
            return result

    return wrapper
