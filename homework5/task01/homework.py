import datetime


class TimeToSolveError(ValueError):
    """Days to solve task can't be negative"""


class Homework:
    """Class for storing information about task and its time to complete"""
    def __init__(self, text: str, time_limit: int):
        if time_limit < 0:
            raise TimeToSolveError

        self._text = text
        self._created = datetime.datetime.now()
        self._final_day = self._created + datetime.timedelta(days=time_limit)

    @property
    def deadline(self) -> datetime.timedelta:
        current_time = datetime.datetime.now()
        delta = self._final_day - current_time
        return delta

    def is_active(self) -> bool:
        current_time = datetime.datetime.now()
        return False if current_time >= self._final_day else True


if __name__ == '__main__':
    task_1 = Homework('Be a hero', 2)
    print(task_1._text, task_1._created, task_1._final_day)
    print(task_1.deadline)
