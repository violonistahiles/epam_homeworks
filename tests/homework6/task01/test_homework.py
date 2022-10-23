import time

import pytest

from homework6.task01.oop_2 import Homework, TimeToSolveError


def test_deadline():
    """Testing deadline property works ok"""
    test_task = Homework('Be a hero', 2)
    time.sleep(0.01)

    deadline = test_task.deadline.days

    assert deadline == 1
    assert test_task._text == 'Be a hero'


def test_is_active_when_is_active():
    """Testing is_active positive case"""
    test_task = Homework('Be a hero', 2)
    assert test_task.is_active()


def test_is_active_when_is_not_active():
    """Testing is_active negative case"""
    test_task = Homework('Be a hero', 0)
    time.sleep(0.01)
    assert not test_task.is_active()


def test_when_days_are_negative():
    """Testing is_active negative case"""
    with pytest.raises(TimeToSolveError):
        _ = Homework('Be a hero', -1)
