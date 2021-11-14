from homework2.hw4 import cache


def func(a, b):
    return (a + b) ** 2


def test_cache_function():
    """Testing cache function on equal input data"""
    cache_func = cache(func)
    test_input = 1, 2

    val_1 = cache_func(*test_input)
    val_2 = cache_func(*test_input)

    assert val_1 is val_2
