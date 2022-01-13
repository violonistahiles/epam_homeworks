import time

from homework5.task01.teacher import Teacher


def test_teacher_create_homework():
    """Testing Teacher class works ok"""
    teacher = Teacher('Daniil', 'Shadrin')
    task = teacher.create_homework('Be a hero', 2)
    time.sleep(0.01)

    assert teacher.first_name == 'Daniil'
    assert teacher.last_name == 'Shadrin'
    assert task.deadline.days == 1
    assert task._text == 'Be a hero'


def test_teacher_create_homework_as_static():
    """Testing Teacher class staticmethod create_homework"""
    task = Teacher.create_homework('Be a hero', 2)
    time.sleep(0.01)

    assert task.deadline.days == 1
    assert task._text == 'Be a hero'
    assert task.is_active()
