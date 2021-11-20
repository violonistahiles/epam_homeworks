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
from typing import List, Union


def fizzbuzz(n: int) -> List[str]:
    """
    Return n numbers where FizzBuzz numbers switched for "fizz" and "buzz"
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    """

    if not isinstance(n, int):
        raise ValueError

    def fizz_cond(x: int) -> Union[int, str]:
        if x % 3 == 0:
            return 'fizz'
        return x

    def buzz_cond(x: int) -> Union[int, str]:
        if x % 5 == 0:
            return 'buzz'
        return x

    fizzbuzz_numbers = []

    for i in range(1, n+1):
        fizz = fizz_cond(i)
        buzz = buzz_cond(i)

        if isinstance(fizz, str) and isinstance(buzz, str):
            fizzbuzz_numbers.append(fizz+buzz)
        elif isinstance(fizz, str):
            fizzbuzz_numbers.append(fizz)
        elif isinstance(buzz, str):
            fizzbuzz_numbers.append(buzz)
        else:
            fizzbuzz_numbers.append(str(i))

    return fizzbuzz_numbers


if __name__ == '__main__':
    print(fizzbuzz(15))
