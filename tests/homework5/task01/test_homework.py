from homework5.task01.homework import Homework


def test_deadline():
    test_task = Homework('eat fish', 2)

    deadline = test_task.deadline.days

    assert deadline == 2
    assert test_task.text == 'eat fish'
