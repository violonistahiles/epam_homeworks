from homework5.task01.teacher import Teacher


def test_student_have_time():
    """Testing Teacher class works ok"""
    teacher = Teacher('Daniil', 'Shadrin')
    task = teacher.create_homework('Be a hero', 2)

    assert teacher.first_name == 'Daniil'
    assert teacher.last_name == 'Shadrin'
    assert task.deadline.days == 2
    assert task.text == 'Be a hero'
