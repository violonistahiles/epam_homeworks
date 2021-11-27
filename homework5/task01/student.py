import sys
from typing import Union

from homework import Homework


class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework: Homework) -> Union[Homework, None]:
        if homework.deadline.days == 0:
            sys.stdout.write('You are late')
            return None
        return homework


if __name__ == '__main__':
    student = Student('Vasiliy', 'Terkin')
    task = Homework('Be a hero', 0)

    print(student.first_name, student.last_name)
    student.do_homework(task)
