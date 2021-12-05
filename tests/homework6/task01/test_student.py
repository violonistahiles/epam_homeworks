import pytest

from homework6.task01.oop_2 import (DeadlineError, Homework, HomeworkResult,
                                    Student)


def test_student_has_time():
    """
    Testing Student class works ok and up-to-date
    task return HomeworkResult class with correct attributes
    """
    student = Student('FirstName', 'LastName')
    task = Homework('Some task', 1)
    solution = 'dummy_solution'
    correct_result = HomeworkResult(student, task, solution)

    result = student.do_homework(task, solution)

    assert result == correct_result


def test_student_is_late(capsys):
    """Testing Student class works ok and overdue task raise DeadlineError"""
    student = Student('FirstName', 'LastName')
    task = Homework('Some task', 0)
    solution = 'dummy_solution'
    std_output = '__main__.DeadlineError: You are late'

    with pytest.raises(DeadlineError):
        student.do_homework(task, solution)
        assert capsys.readouterr().out == std_output
