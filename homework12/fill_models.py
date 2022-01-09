from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from homework12.models import (Base, HomeworkResultTable, HomeworkTable,
                               StudentTable, TeacherTable)


def create_models():
    engine = create_engine("sqlite+pysqlite:///:memory:",
                           echo=False,
                           future=True)

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
        session.add(student_first)
        session.add(student_second)
        session.add(teacher)
        session.add(homework)
        session.add(hw_res_1)
        session.add(hw_res_2)
        session.commit()

    return engine


if __name__ == '__main__':
    create_models()
