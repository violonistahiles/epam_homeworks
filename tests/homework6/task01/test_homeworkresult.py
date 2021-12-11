import pytest

from homework6.task01.oop_2 import (Homework, HomeworkResult,
                                    HomeworkTypeError, Person)


def test_homework_parameter_is_not_homework_class(capsys):
    """Testing that wrong parameter for homework will raise error"""
    person = Person('FirstName', 'LastName')
    task = 'Wrong task type'
    solution = 'dummy_solution'
    std_output = '__main__.HomeworkTypeError: You gave a not Homework object'

    with pytest.raises(HomeworkTypeError):
        _ = HomeworkResult(person, task, solution)
        assert capsys.readouterr().out == std_output


def test_homeworkresult():
    """Testing creation of class instance"""
    person = Person('FirstName', 'LastName')
    task = Homework('Some task', 1)
    solution = 'dummy_solution'

    test_hwresult = HomeworkResult(person, task, solution)

    assert test_hwresult.author == person
    assert test_hwresult.homework == task
    assert test_hwresult.solution == solution
    assert test_hwresult.created == task._created


def test_compare_two_homeworkresults_when_equal():
    """Testing that two homeworkresults with equal init parameters are equal"""
    person = Person('FirstName', 'LastName')
    task = Homework('Some task', 1)
    solution = 'dummy_solution'

    first_hwresult = HomeworkResult(person, task, solution)
    second_hwresult = HomeworkResult(person, task, solution)

    assert first_hwresult == second_hwresult


def test_compare_two_homeworkresults_when_not_equal():
    """
    Testing that two homeworkresults with different
    init parameters are not equal
    """
    person = Person('FirstName', 'LastName')
    task = Homework('Some task', 1)
    first_solution = 'dummy_solution_first'
    second_solution = 'dummy_solution_second'

    first_hwresult = HomeworkResult(person, task, first_solution)
    second_hwresult = HomeworkResult(person, task, second_solution)

    assert first_hwresult != second_hwresult


def test_hash_homeworkresults_when_equal():
    """Testing that two equal homeworkresults have equal hash"""
    person = Person('FirstName', 'LastName')
    task = Homework('Some task', 1)
    solution = 'dummy_solution'

    first_hwresult = HomeworkResult(person, task, solution)
    second_hwresult = HomeworkResult(person, task, solution)

    assert hash(first_hwresult) == hash(second_hwresult)


def test_hash_homeworkresults_when_not_equal():
    """Testing that two different homeworkresults have different hash"""
    person = Person('FirstName', 'LastName')
    task = Homework('Some task', 1)
    first_solution = 'dummy_solution_first'
    second_solution = 'dummy_solution_second'

    first_hwresult = HomeworkResult(person, task, first_solution)
    second_hwresult = HomeworkResult(person, task, second_solution)

    assert hash(first_hwresult) != hash(second_hwresult)
