from sqlalchemy import select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from homework12.hw_6 import Homework, HomeworkResult, Student, Teacher
from homework12.models import (Base, HomeworkResultTable, HomeworkTable,
                               StudentTable, TeacherTable)


class DBClient:
    """
    Client for manipulating information about students, teachers, homeworks
    and homework results in database
    """
    def __init__(self, engine: Engine):
        """
        :param engine: Object establishing connection to database
        :type engine: Engine
        """
        self._engine = engine

    @staticmethod
    def _get_id(table: Base, session: Session, **kwargs) -> int:
        """
        Return id number of element with requested parameters from db table

        :param table: ORM mapped class, representing database table
        :type table: Base
        :param session: Manages persistence operations for ORM-mapped objects
        :type session: Session
        :param **kwargs: Key, value pairs filtering data in table
        :type **kwargs: Any
        :return: ID number of filtered object
        :rtype: int
        """
        task = select(table.id).filter_by(**kwargs)
        id_sample = session.execute(task).scalar_one()
        return id_sample

    @staticmethod
    def _check_element(table: Base, session: Session, **kwargs) -> Base:
        """
        Check if element exists in table

        :param table: ORM mapped class, representing database table
        :type table: Base
        :param session: Manages persistence operations for ORM-mapped objects
        :type session: Session
        :param **kwargs: Key, value pairs filtering data in table
        :type **kwargs: Any
        :return: ORM mapped class, representing single raw from database table
        :rtype: Base
        """
        task = select(table).filter_by(**kwargs)
        result = session.execute(task).first()
        return result

    def _add_to_bd(self, table: Base, **kwargs) -> int:
        """
        Add new element to database table

        :param table: ORM mapped class, representing database table
        :type table: Base
        :return: ID number of new created table element
        :rtype: int
        """
        sample = table(**kwargs)
        with Session(self._engine) as session:
            if self._check_element(table, session, **kwargs):
                sample_id = self._get_id(table, session, **kwargs)
            else:
                session.add(sample)
                session.commit()
                sample_id = self._get_id(table, session, **kwargs)

        return sample_id

    def create_student(self, first_name: str, last_name: str) -> Student:
        """
        Create new student instance and put it database

        :param first_name: First name of the person
        :type first_name: str
        :param last_name: Last name of the person
        :type last_name: str
        :return: Student instance
        :rtype: Student
        """
        kwargs = {'name': first_name,
                  'surname': last_name}
        student_id = self._add_to_bd(StudentTable, **kwargs)
        student = Student(first_name, last_name, student_id)
        return student

    def create_teacher(self, first_name: str, last_name: str) -> Teacher:
        """
        Create new teacher instance and put it database

        :param first_name: First name of the person
        :type first_name: str
        :param last_name: Last name of the person
        :type last_name: str
        :return: Teacher instance
        :rtype: Teacher
        """
        kwargs = {'name': first_name,
                  'surname': last_name}

        teacher_id = self._add_to_bd(TeacherTable, **kwargs)
        teacher = Teacher(first_name, last_name, teacher_id)
        return teacher

    def create_homework(
            self, teacher: Teacher, task: str, time_limit: int
    ) -> Homework:
        """
        Create new homework instance and put it database

        :param teacher: Teacher instance who created homework
        :type teacher: Teacher
        :param task: Task description
        :type task: str
        :param time_limit: Time to solve task
        :type time_limit: int
        :return: Homework instance
        :rtype: Homework
        """
        homework = teacher.create_homework(task, time_limit)
        kwargs = {'text': homework.text,
                  'created': homework.created,
                  'final_day': homework.final_day,
                  'teacher_id': homework.teacher_id}

        hw_id = self._add_to_bd(HomeworkTable, **kwargs)
        homework.id = hw_id
        return homework

    def create_homeworkresult(
            self, student: Student, homework: Homework, solution: str
    ) -> HomeworkResult:
        """
        Create a new homework result instance and put it the database

        :param student: Student instance who created solution for homework
        :type student: str
        :param homework: Homework instance which student solving
        :type homework: Homework
        :param solution: Text of homework solution
        :type solution: str
        :return: HomeworkResult instance
        :rtype: HomeworkResult
        """
        homeworkresult = student.do_homework(homework, solution)
        kwargs = {'author': homeworkresult.author.id,
                  'homework': homeworkresult.homework.id,
                  'solution': homeworkresult.solution,
                  'created': homeworkresult.created,
                  'status': False}

        _ = self._add_to_bd(HomeworkResultTable, **kwargs)
        return homeworkresult

    def check_homework(self, teacher: Teacher, result: HomeworkResult):
        """
        Check the result of homework with the help of the teacher
        and change its status in the database

        :param teacher: Teacher instance who is checking homework result
        :type teacher: Teacher
        :param result: HomeworkResult instance
        :type result: HomeworkResult
        """
        if teacher.check_homework(result):
            self._change_hw_status(result)

    @staticmethod
    def _get_homework_result(
            session: Session, result: HomeworkResult
    ) -> HomeworkResultTable:
        """
        Get homework result element from the database

        :param session: Manages persistence operations for ORM-mapped objects
        :type session: Session
        :param result: HomeworkResult instance
        :type result: HomeworkResult
        :return: HomeworkResultTable instance
        :rtype: HomeworkResultTable
        """
        task = select(HomeworkResultTable).filter_by(
            author=result.author.id,
            homework=result.homework.id,
            solution=result.solution,
            created=result.created
        )
        hw_result = session.execute(task).scalar_one()
        return hw_result

    def _change_hw_status(self, result: HomeworkResult):
        """
        Change status of the homework result in database

        :param result: HomeworkResult instance
        :type result: HomeworkResult
        """
        with Session(self._engine) as session:
            hw_result = self._get_homework_result(session, result)
            hw_result.status = True
            session.commit()
