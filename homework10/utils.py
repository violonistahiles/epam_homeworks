from typing import Union


def fill_date(date: int) -> Union[str, int]:
    """
    Add zero at the left of the number if it is single digit

    :param date: Number
    :type date: int
    :return: Number supplemented by zero at left if number is one digit
    :rtype Union[str, int]:
    """
    return ''.join(['0', str(date)]) if len(str(date)) == 1 else date
