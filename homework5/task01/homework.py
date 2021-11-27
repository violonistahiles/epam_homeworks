import datetime


class TimeToSolveError(ValueError):
    """Days to solve task can't be negative"""


class Homework:
    """Class for storing information about task and its time to complete"""
    def __init__(self, text: str, days_to_solve: int) -> None:
        if days_to_solve < 0:
            raise TimeToSolveError

        self.text = text
        self.created = datetime.datetime.now()
        self.final_day = self.created + datetime.timedelta(days=days_to_solve)

    @property
    def deadline(self) -> datetime.timedelta:
        current_time = datetime.datetime.now()
        delta = self.final_day - current_time
        return delta

    def is_active(self):
        current_time = datetime.datetime.now()
        if current_time > self.final_day:
            return False
        return True


if __name__ == '__main__':
    task_1 = Homework('Be a hero', 2)
    print(task_1.text, task_1.created, task_1.final_day)
    print(task_1.deadline)
