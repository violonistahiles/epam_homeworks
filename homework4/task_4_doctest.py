"""
Write a function that takes a number N as an input
and returns N FizzBuzz numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests

assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран,
                                                  чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Return n numbers where FizzBuzz numbers switched for "fizz" and "buzz"
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> test_result = fizzbuzz(15)
    >>> test_result.count('fizzbuzz')
    1
    >>> test_result.count('fizz')
    4
    >>> test_result.count('buzz')
    2
    >>> fizzbuzz(-3)
    Traceback (most recent call last):
    ValueError
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError

    def fizz_cond(x: int) -> str:
        if x % 3 == 0:
            return 'fizz'
        return ''

    def buzz_cond(x: int) -> str:
        if x % 5 == 0:
            return 'buzz'
        return ''

    fizzbuzz_numbers = []

    for i in range(1, n+1):
        result = ''
        result += fizz_cond(i)
        result += buzz_cond(i)

        if not result:
            result = str(i)

        fizzbuzz_numbers.append(result)

    return fizzbuzz_numbers


if __name__ == '__main__':
    print(fizzbuzz(15))
