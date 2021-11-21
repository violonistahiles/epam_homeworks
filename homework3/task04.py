"""
Armstrong number is a number that is the sum of its own digits each raised to
the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:

- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


Write a function that detects if a number is Armstrong number in functional
style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

### Example function signature and call
"""
from functools import reduce
from typing import Tuple


def number_to_string(number: int) -> Tuple[str, int]:
    """Convert integer to string and get its length"""
    str_number = str(number)
    return str_number, len(str_number)


def get_digits_power_sum(number: int) -> int:
    """Function to get Armstrong sum"""
    str_number, digits_number = number_to_string(number)
    powered_digits = map(lambda x: int(x)**digits_number, str_number)
    digits_sum = reduce(lambda x, y: x+y, powered_digits)
    return digits_sum


def is_armstrong(number: int) -> bool:
    """Check if number is Armstrong number"""
    if number < 0 and not isinstance(number, int):
        return False

    digits_sum = get_digits_power_sum(number)
    return number == digits_sum
