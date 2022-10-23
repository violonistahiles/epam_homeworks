import os
from datetime import datetime

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from homework12.get_report import ElementNotFoundError, ReportClient
from homework12.models import (Base, HomeworkResultTable, HomeworkTable,
                               StudentTable, TeacherTable)


@pytest.fixture
def report():
    """Etalon report"""
    current_path = os.path.abspath(os.getcwd())
    current_path = os.path.join(current_path, 'tests', 'homework12_tests')
    with open(os.path.join(current_path, 'report.csv'), 'r') as fi:
        data = fi.read()
    return data


@pytest.fixture
def database():
    """Create fake database for tests"""
    engine = create_engine('sqlite+pysqlite:///:memory:')
    Base.metadata.create_all(engine)

    student_first = StudentTable(name='Anakin', surname='Skywalker')
    student_second = StudentTable(name='Luke', surname='Skywalker')

    teacher = TeacherTable(name='Obi Wan', surname='Kenobi')

    homework = HomeworkTable(text='Take the force with you',
                             created=datetime.strptime('21:01:10',
                                                       '%y:%m:%d'),
                             final_day=datetime.strptime('21:01:11',
                                                         '%y:%m:%d'),
                             teacher_id=1)

    hw_res_1 = HomeworkResultTable(author=1,
                                   homework=1,
                                   solution='Force is always with me',
                                   created=datetime.strptime('21:01:10',
                                                             '%y:%m:%d'),
                                   status=False)

    hw_res_2 = HomeworkResultTable(author=2,
                                   homework=1,
                                   solution='Make the force to be with you',
                                   created=datetime.strptime('21:01:10',
                                                             '%y:%m:%d'),
                                   status=True)

    with Session(engine) as session:
        session.add_all([student_first, student_second, teacher,
                         homework, hw_res_1, hw_res_2])
        session.commit()

    return engine


def test_select_one(database):
    """
    Test selecting one element from table when after filtering
    there is only one element in table
    """
    reporter = ReportClient(database, 'dummy_path')
    attributes_to_test = ['id', 'name', 'surname']
    correct_tr = TeacherTable(id=1, name='Obi Wan', surname='Kenobi')

    with Session(database) as session:
        test_tr = reporter._select(session, TeacherTable,
                                   one=True, name='Obi Wan')[0]

    for attribute in attributes_to_test:
        assert getattr(test_tr, attribute) == getattr(correct_tr, attribute)


def test_select_one_with_multiple_choice(database):
    """
    Test selecting one element from table when after filtering
    there are many elements in table
    """
    reporter = ReportClient(database, 'dummy_path')
    attributes_to_test = ['id', 'name', 'surname']
    correct_st = StudentTable(id=1, name='Anakin', surname='Skywalker')

    with Session(database) as session:
        test_st = reporter._select(session, StudentTable,
                                   one=True, surname='Skywalker')[0]

    for attribute in attributes_to_test:
        assert getattr(test_st, attribute) == getattr(correct_st, attribute)


def test_select_many(database):
    """
    Test selecting many elements from table when after filtering
    there are many elements in table
    """
    reporter = ReportClient(database, 'dummy_path')
    attributes_to_test = ['id', 'name', 'surname']
    correct_st1 = StudentTable(id=1, name='Anakin', surname='Skywalker')
    correct_st2 = StudentTable(id=2, name='Luke', surname='Skywalker')
    correct = [correct_st1, correct_st2]

    with Session(database) as session:
        test_st = reporter._select(session, StudentTable,
                                   one=False, surname='Skywalker')

    for i, res in enumerate(test_st):
        for attribute in attributes_to_test:
            assert getattr(res[0], attribute) == getattr(correct[i],
                                                         attribute)


def test_select_many_when_element_is_one(database):
    """
    Test selecting many elements from table when after filtering
    there is only one element in table
    """
    reporter = ReportClient(database, 'dummy_path')
    attributes_to_test = ['id', 'name', 'surname']
    correct_tr = TeacherTable(id=1, name='Obi Wan', surname='Kenobi')

    with Session(database) as session:
        test_tr = reporter._select(session, TeacherTable,
                                   one=False, name='Obi Wan')[0][0]

    for attribute in attributes_to_test:
        assert getattr(test_tr, attribute) == getattr(correct_tr, attribute)


def test_select_when_no_such_element(database):
    """
    Test selecting from database when there is no finding element
    """
    reporter = ReportClient(database, 'dummy_path')

    with pytest.raises(ElementNotFoundError):
        with Session(database) as session:
            _ = reporter._select(session, TeacherTable, name='Dart')


def test_get_report(tmpdir, database, report):
    """
    Testing get_report method works correctly
    """
    tmp_path = tmpdir.mkdir('sub')
    reporter = ReportClient(database, tmp_path)
    path_to_test = tmp_path.join('report.csv')

    reporter.get_report()

    with open(path_to_test, 'r') as fi:
        test_data = fi.read()

    assert test_data == report
