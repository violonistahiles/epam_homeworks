from homework5.task01.homework import Homework
from homework5.task01.student import Student


def test_student_have_time():
    student = Student('Vasiliy', 'Terkin')
    task = Homework('Be a hero', 1)

    assert student.first_name == 'Vasiliy'
    assert student.last_name == 'Terkin'
    assert student.do_homework(task) == task


def test_student_are_late(capsys):
    student = Student('Vasiliy', 'Terkin')
    task = Homework('Be a hero', 0)

    assert student.first_name == 'Vasiliy'
    assert student.last_name == 'Terkin'
    assert not student.do_homework(task)
    assert capsys.readouterr().out == 'You are late'
