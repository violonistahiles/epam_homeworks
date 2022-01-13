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
        return self._final_day - datetime.datetime.now()

    def is_active(self) -> bool:
        return not datetime.datetime.now() >= self._final_day
