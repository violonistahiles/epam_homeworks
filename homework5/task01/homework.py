import datetime


class Homework:
    def __init__(self, text: str, days_to_solve: int) -> None:
        self.text = text
        self.created = datetime.datetime.now()
        self.final_day = self.created + datetime.timedelta(days=days_to_solve)

    @property
    def deadline(self) -> datetime.timedelta:
        current_time = datetime.datetime.now()
        delta = self.final_day - current_time
        return delta


if __name__ == '__main__':
    task_1 = Homework('eat fish', 2)
    print(task_1.text, task_1.created, task_1.final_day)
    print(task_1.deadline)
