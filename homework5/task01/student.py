import sys
from typing import Union

from homework5.task01.homework import Homework


class Student:
    """Abstract student with first and last name which can check task info"""
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework: Homework) -> Union[Homework, None]:
        if homework.is_active():
            return homework

        sys.stdout.write('You are late')
