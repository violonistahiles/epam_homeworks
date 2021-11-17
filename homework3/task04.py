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


def get_digits_number(number: int) -> int:
    """Recursion function to get number of digits"""
    rest_digits = number // 10
    if not rest_digits:
        return 1
    else:
        return 1 + get_digits_number(rest_digits)


def get_sum(number: int, power: int) -> int:
    """Recursion function to power each digit in number"""
    rest_digits = number // 10
    if not rest_digits:
        return pow(number % 10, power)
    else:
        return pow(number % 10, power) + get_sum(rest_digits, power)


def get_digits_power_sum(number: int) -> int:
    """Function to get Armstrong sum"""
    digits_number = get_digits_number(number)
    return get_sum(number, digits_number)


def is_armstrong(number: int) -> bool:
    """Check if number is Armstrong number"""
    if number < 0 and not isinstance(number, int):
        return False
    digits_sum = get_digits_power_sum(number)
    return number == digits_sum
