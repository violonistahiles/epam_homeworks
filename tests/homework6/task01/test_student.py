from homework6.task01.oop_2 import Homework, Student


def test_student_has_time(capsys):
    """Testing Student class works ok and up-to-date task return task"""
    student = Student('Vasiliy', 'Terkin')
    task = Homework('Be a hero', 1)

    assert student.first_name == 'Vasiliy'
    assert student.last_name == 'Terkin'
    assert student.do_homework(task) == task
    assert not capsys.readouterr().out


def test_student_is_late(capsys):
    """Testing Student class works ok and overdue task return None"""
    student = Student('Vasiliy', 'Terkin')
    task = Homework('Be a hero', 0)

    assert student.first_name == 'Vasiliy'
    assert student.last_name == 'Terkin'
    assert not student.do_homework(task)
    assert capsys.readouterr().out == 'You are late'
