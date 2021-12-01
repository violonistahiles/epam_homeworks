from homework5.task01.homework import Homework


class Teacher:
    """Abstract teacher with first and last name which can create task"""
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text: str, days_to_solve: int) -> Homework:
        return Homework(text, days_to_solve)


if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')

    print(teacher.first_name, teacher.last_name)
    task = teacher.create_homework('Be a hero', 2)
    print(task.deadline)
