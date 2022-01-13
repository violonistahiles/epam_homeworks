import time

from homework6.task01.oop_2 import HomeworkResult, Student, Teacher


def test_teacher_create_homework():
    """Testing Teacher class works ok"""
    teacher = Teacher('Name', 'Surname')
    task = teacher.create_homework('Task', 2)
    time.sleep(0.01)

    assert teacher.first_name == 'Name'
    assert teacher.last_name == 'Surname'
    assert task.deadline.days == 1
    assert task._text == 'Task'


def test_teacher_create_homework_as_static():
    """Testing Teacher class staticmethod create_homework"""
    task = Teacher.create_homework('Task', 2)
    time.sleep(0.01)

    assert task.deadline.days == 1
    assert task._text == 'Task'
    assert task.is_active()


def test_teacher_check_homework_when_solution_long():
    """
    Testing teacher method check_homework works fine
    with solutoin length greater then 5
    """
    teacher = Teacher('Teacher_name', 'Teacher_surname')
    task = teacher.create_homework('Task', 2)
    solution = 'Some long solution'
    student = Student('Student_name', 'Student_surname')
    homework_result = HomeworkResult(student, task, solution)

    assert teacher.check_homework(homework_result)
    assert teacher.homework_done[task].pop() == homework_result

    Teacher.homework_done.clear()


def test_teacher_check_homework_when_solution_short():
    """
    Testing teacher method check_homework works fine
    with solution length less or equal 5
    """
    teacher = Teacher('Teacher_name', 'Teacher_surname')
    task = teacher.create_homework('Task', 2)
    solution = 'short'
    student = Student('Student_name', 'Student_surname')
    homework_result = HomeworkResult(student, task, solution)

    assert not teacher.check_homework(homework_result)
    assert len(teacher.homework_done) == 0

    Teacher.homework_done.clear()


def test_teacher_check_homework_when_different_homeworks():
    """
    Testing teacher method check_homework when two different teachers
    check two different homeworks
    """
    teacher_one = Teacher('One_name', 'One_surname')
    teacher_two = Teacher('Two_name', 'Two_surname')
    task_one = teacher_one.create_homework('Task_one', 2)
    task_two = teacher_two.create_homework('Task_two', 2)

    solution = 'Some long solution'
    student = Student('Student_name', 'Student_surname')
    homework_result_one = HomeworkResult(student, task_one, solution)
    homework_result_two = HomeworkResult(student, task_two, solution)

    assert teacher_one.check_homework(homework_result_one)
    assert teacher_two.check_homework(homework_result_two)
    assert len(Teacher.homework_done) == 2

    Teacher.homework_done.clear()


def test_teacher_check_homework_same_homeworks_different_solutions():
    """
    Testing teacher method check_homework when two different solutions
    for one homework
    """
    teacher_one = Teacher('One_name', 'One_surname')
    teacher_two = Teacher('Two_name', 'Two_surname')
    task = teacher_one.create_homework('Task', 2)
    student = Student('Student_name', 'Student_surname')

    solution_one = 'Some long solution one'
    solution_two = 'Some long solution two'

    homework_result_one = HomeworkResult(student, task, solution_one)
    homework_result_two = HomeworkResult(student, task, solution_two)

    assert teacher_one.check_homework(homework_result_one)
    assert teacher_two.check_homework(homework_result_two)
    assert len(Teacher.homework_done) == 1
    assert len(Teacher.homework_done[task]) == 2

    Teacher.homework_done.clear()


def test_teacher_reset_results_for_specific_homework():
    """
    Testing teacher method reset_results works fine
    when delete specific homework
    """
    teacher = Teacher('Teacher_name', 'Teacher_surname')
    task_one = teacher.create_homework('Task one', 2)
    task_two = teacher.create_homework('Task two', 2)
    solution = 'Some long solution'
    student = Student('Student_name', 'Student_surname')
    homework_result_one = HomeworkResult(student, task_one, solution)
    homework_result_two = HomeworkResult(student, task_two, solution)

    teacher.check_homework(homework_result_one)
    teacher.check_homework(homework_result_two)
    assert len(Teacher.homework_done) == 2

    Teacher.reset_results(task_one)
    assert len(Teacher.homework_done) == 1

    Teacher.homework_done.clear()


def test_teacher_reset_results_for_all_homeworks():
    """
    Testing teacher method reset_results works fine
    when delete all homeworks
    """
    teacher = Teacher('Teacher_name', 'Teacher_surname')
    task_one = teacher.create_homework('Task one', 2)
    task_two = teacher.create_homework('Task two', 2)
    solution = 'Some long solution'
    student = Student('Student_name', 'Student_surname')
    homework_result_one = HomeworkResult(student, task_one, solution)
    homework_result_two = HomeworkResult(student, task_two, solution)

    teacher.check_homework(homework_result_one)
    teacher.check_homework(homework_result_two)
    assert len(Teacher.homework_done) == 2

    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0

    Teacher.homework_done.clear()
