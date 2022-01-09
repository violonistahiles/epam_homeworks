from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from homework12.models import (HomeworkResultTable, HomeworkTable,
                               StudentTable, TeacherTable)


def select_valid_homeworks(session):
    task = select(HomeworkResultTable).filter_by(status=True)
    result = session.execute(task)
    return result


def select_homework_task(session, homework_id):
    task = select(HomeworkTable).filter_by(id=homework_id)
    result = session.execute(task).scalar_one()
    return result


def select_teacher(session, teacher_id):
    task = select(TeacherTable).filter_by(id=teacher_id)
    result = session.execute(task).scalar_one()
    return result


def select_student(session, student_id):
    task = select(StudentTable).filter_by(id=student_id)
    result = session.execute(task).scalar_one()
    return result


if __name__ == '__main__':
    engine = create_engine('sqlite:///main.db')

    with Session(engine) as session:
        hw_results = select_valid_homeworks(session)
        for res in hw_results:
            hw = select_homework_task(session, res[0].homework)
            teach = select_teacher(session, hw.teacher_id)
            student = select_student(session, res[0].author)
            print('Student:', student.name, ', Task:', hw.text,
                  ', Solution:', res[0].solution, ', Teacher:', teach.name,
                  ', Creation_data: ', res[0].created)
        print()
