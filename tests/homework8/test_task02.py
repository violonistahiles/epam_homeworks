import os
import sqlite3

import pytest

from homework8.task02 import DatabaseNotExistError, TableData, TableNotExists


def test_len_method():
    """Testing TableData len method work correct"""
    database_name = 'example.db'
    test_table = 'presidents'

    presidents = TableData(database_name, test_table)

    assert len(presidents) == 3


def test_getitem_method():
    """Testing TableData getitem method work correct"""
    database_name = 'example.db'
    test_table = 'presidents'
    correct_result = {'name': 'Yeltsin', 'age': 999, 'country': 'Russia'}

    presidents = TableData(database_name, test_table)

    assert presidents['Yeltsin'] == correct_result


def test_contains_method():
    """Testing TableData contains method work correct"""
    database_name = 'example.db'
    test_table = 'presidents'

    presidents = TableData(database_name, test_table)

    assert 'Yeltsin' in presidents
    assert 'Putin' not in presidents


def test_iter_method():
    """Testing TableData iter method work correct"""
    database_name = 'example.db'
    test_table = 'presidents'
    correct_results = [{'name': 'Yeltsin', 'age': 999, 'country': 'Russia'},
                       {'name': 'Trump', 'age': 1337, 'country': 'US'},
                       {'name': 'Big Man Tyrone', 'age': 101,
                        'country': 'Kekistan'}]

    presidents = TableData(database_name, test_table)

    for correct_president, president_from_table in zip(correct_results,
                                                       presidents):
        assert president_from_table == correct_president


def test_update_table():
    """Testing TableData instance reflects most recent data"""
    database_name = 'example.db'
    test_table = 'presidents'

    presidents = TableData(database_name, test_table)
    assert len(presidents) == 3

    # Add row to the table in database
    db_path = os.path.join(os.path.abspath(os.getcwd()),
                           'homework8',
                           database_name)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("insert into presidents values('Putin', 42, '...')")
    conn.commit()
    assert len(presidents) == 4
    assert 'Putin' in presidents

    # Delete added row
    cursor.execute("delete from presidents where name='Putin'")
    conn.commit()
    conn.close()


def test_table_not_exists():
    """Testing if table is not exists in database raise TableNotExists"""
    database_name = 'example.db'
    test_table = 'animals'

    with pytest.raises(TableNotExists):
        _ = TableData(database_name, test_table)


def test_database_not_exists():
    """Testing if database is not exists raise DatabaseNotExistError"""
    database_name = 'dummy_db'
    test_table = 'presidents'

    with pytest.raises(DatabaseNotExistError):
        _ = TableData(database_name, test_table)
