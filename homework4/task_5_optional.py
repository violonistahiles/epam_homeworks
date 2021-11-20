"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the
implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""


def fizzbuzz(n: int) -> str:
    """
    Generator that yields n FizzBuzz numbers
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError

    start = 1
    end = n + 1
    for i in range(start, end):
        fizz = i % 3 == 0
        buzz = i % 5 == 0
        yield 'fizz'*fizz + 'buzz'*buzz + (not buzz and not fizz)*str(i)


if __name__ == '__main__':
    number = 15
    print(list(fizzbuzz(number)))
