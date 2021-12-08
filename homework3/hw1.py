"""
Create parametrized decorator that remembers other function output value
and give it out times number only.

@cache(times=2)
def f():
    return input('? ')

# >>> f()
# ? 1
# '1'
# >>> f()      # will remember previous value
# '1'
# >>> f()      # but use it up to two times only
# '1'
# >>> f()
# ? 2
# '2'
"""
from typing import Any, Callable


class CacheSizeError(Exception):
    def __init__(self) -> None:
        print('Argument "times" should be int and greater then 0')


class Cache:
    def __init__(self) -> None:
        self.value = 0
        self.size = 0


def cache(times: int) -> Callable:
    """Cache function result for n invokes"""
    if not isinstance(times, int) or times <= 0:
        raise CacheSizeError()
    # Create class for caching results
    memory = Cache()

    def wrapper(func: Callable) -> Callable:
        def inner_wrapper(*args) -> Any:
            if memory.size > 0:
                memory.size -= 1
                return memory.value
            else:
                result = func(*args)

                memory.value = result
                memory.size = times

                return result

        return inner_wrapper

    return wrapper


@cache(times=1)
def function_for_test():
    return input('?')


if __name__ == '__main__':
    for i in range(2):
        print(function_for_test())
