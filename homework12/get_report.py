import csv
import os
from typing import Any, Callable, List, Tuple, Union

from sqlalchemy import create_engine, select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from homework12.models import (Base, HomeworkResultTable, HomeworkTable,
                               StudentTable, TeacherTable)


class ElementNotFoundError(Exception):
    """No such element in database"""


def queries_decorator(func: Callable) -> Callable:
    """
    Decorator to handling exceptions during database queries
    :param func: Parsing function
    :type func: Callable
    :return: Decorated function
    :rtype: Callable
    """
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
        if not result:
            raise ElementNotFoundError

        return result
    return wrapper


class ReportClient:
    """Class for creating report about students homework results"""
    def __init__(self, engine: Engine, data_path: str):
        """
        :param engine: Object establishing connection to database
        :type engine: Engine
        :param data_path: Path to folder where to store report
        :type data_path: str
        """
        self._engine = engine
        self.file_path = os.path.join(data_path, 'report.csv')

    @staticmethod
    @queries_decorator
    def _select(
            session: Session, table: Base, one: bool = True, **kwargs: Any
    ) -> Union[Tuple[Base], Tuple[Tuple[Base], ...]]:
        """
        Select many elements from the table

        :param session: Manages persistence operations for ORM-mapped objects
        :type session: Session
        :param table: ORM mapped class, representing database table
        :type table: Base
        :param one: Flag to return one value or all results
        :type one: bool
        :param **kwargs: Key, value pairs filtering data in table
        :type **kwargs: Any
        :return: ORM mapped class, representing single or many rows
                 from database table
        :rtype: Union[List[Base], Base]
        """
        task = select(table).filter_by(**kwargs)
        result = session.execute(task)
        return result.fetchone() if one else result.fetchall()

    def _save_results(self, data: List, first: bool = False):
        """
        Save single data row to report.csv

        :param data: List with values for single line in .csv file
        :type data: List
        :param first: Flag to save rewrite file and fill header
        :type first: bool
        """
        if first:
            with open(self.file_path, 'w', newline='') as fi:
                report = csv.writer(fi)
                report.writerow(data)
        else:
            with open(self.file_path, 'a', newline='') as fi:
                report = csv.writer(fi)
                report.writerow(data)

    def get_report(self):
        """Save data from database in report.csv file"""
        self._save_results(['Student Name', 'Task', 'Solution',
                            'Teacher', 'Creation Date'], first=True)

        with Session(self._engine) as session:
            hw_results = self._select(session, HomeworkResultTable,
                                      one=False, status=True)
            for res in hw_results:
                hw = self._select(session, HomeworkTable,
                                  id=res[0].homework)[0]
                teacher = self._select(session, TeacherTable,
                                       id=hw.teacher_id)[0]
                student = self._select(session, StudentTable,
                                       id=res[0].author)[0]
                self._save_results([student.name, hw.text, res[0].solution,
                                    teacher.name, res[0].created])


if __name__ == '__main__':
    engine = create_engine('sqlite:///main.db')
    path = os.getcwd()
    reporter = ReportClient(engine, path)
    reporter.get_report()
