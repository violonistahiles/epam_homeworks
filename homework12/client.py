from sqlalchemy import select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from homework12.hw_6 import Student, Teacher
from homework12.models import (HomeworkResultTable, HomeworkTable,
                               StudentTable, TeacherTable)


class DBClient:
    def __init__(self, engine: Engine):
        self._engine = engine

    @staticmethod
    def _get_id(table, session, **kwargs):
        task = select(table.id).filter_by(**kwargs)
        id_sample = session.execute(task).scalar_one()
        return id_sample

    @staticmethod
    def _check_element(table, session, **kwargs):
        task = select(table).filter_by(**kwargs)
        result = session.execute(task).first()
        return result

    def _add_to_bd(self, table, **kwargs):
        sample = table(**kwargs)
        with Session(self._engine) as session:
            if self._check_element(table, session, **kwargs):
                sample_id = self._get_id(table, session, **kwargs)
            else:
                session.add(sample)
                session.commit()
                sample_id = self._get_id(table, session, **kwargs)

        return sample_id

    def create_student(self, first_name, last_name):
        kwargs = {'name': first_name,
                  'surname': last_name}
        student_id = self._add_to_bd(StudentTable, **kwargs)
        student = Student(first_name, last_name, student_id)
        return student

    def create_teacher(self, first_name, last_name):
        kwargs = {'name': first_name,
                  'surname': last_name}

        teacher_id = self._add_to_bd(TeacherTable, **kwargs)
        teacher = Teacher(first_name, last_name, teacher_id)
        return teacher

    def create_homework(self, teacher, task, time_limit):
        homework = teacher.create_homework(task, time_limit)
        kwargs = {'text': homework.text,
                  'created': homework.created,
                  'final_day': homework.final_day,
                  'teacher_id': homework.teacher_id}

        hw_id = self._add_to_bd(HomeworkTable, **kwargs)
        homework.id = hw_id
        return homework

    def create_homeworkresult(self, student, homework, solution):
        homeworkresult = student.do_homework(homework, solution)
        kwargs = {'author': homeworkresult.author.id,
                  'homework': homeworkresult.homework.id,
                  'solution': homeworkresult.solution,
                  'created': homeworkresult.created,
                  'status': False}

        _ = self._add_to_bd(HomeworkResultTable, **kwargs)
        return homeworkresult

    def check_homework(self, teacher, result):
        if teacher.check_homework(result):
            self._change_hw_status(result)

    @staticmethod
    def _get_homework_result(session, result):
        task = select(HomeworkResultTable).filter_by(
            author=result.author.id,
            homework=result.homework.id,
            solution=result.solution,
            created=result.created
        )
        hw_result = session.execute(task).scalar_one()
        return hw_result

    def _change_hw_status(self, result):
        with Session(self._engine) as session:
            hw_result = self._get_homework_result(session, result)
            hw_result.status = True
            session.commit()
