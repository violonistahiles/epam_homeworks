from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from homework12.client import DBClient
from homework12.fill_models import create_models
from homework12.models import (HomeworkResultTable, HomeworkTable,
                               StudentTable, TeacherTable)


def select_valid_homeworks(session):
    task = select(HomeworkResultTable).filter_by(status=False)
    result = session.execute(task)
    return result


def main():

    engine = create_models()
    db_client = DBClient(engine)

    opp_teacher = db_client.create_teacher('Daniil', 'Shadrin')
    advanced_python_teacher = db_client.create_teacher('Aleksandr', 'Smetanin')

    lazy_student = db_client.create_student('Roman', 'Petrov')
    good_student = db_client.create_student('Lev', 'Sokolov')

    oop_hw = db_client.create_homework(opp_teacher, 'Learn OOP', 1)
    docs_hw = db_client.create_homework(opp_teacher, 'Read docs', 5)

    print(datetime.today())

    result_1 = db_client.create_homeworkresult(good_student,
                                               oop_hw,
                                               'I have done this hw')
    result_2 = db_client.create_homeworkresult(good_student,
                                               docs_hw,
                                               'I have done this hw too')
    result_3 = db_client.create_homeworkresult(lazy_student,
                                               docs_hw,
                                               'done')

    db_client.check_homework(opp_teacher, result_1)

    db_client.check_homework(advanced_python_teacher, result_1)

    db_client.check_homework(opp_teacher, result_2)
    db_client.check_homework(opp_teacher, result_3)

    with Session(engine) as session:
        result = session.execute(select(StudentTable))
        print('StudentTable')
        for res in result:
            print(res)

        result = session.execute(select(TeacherTable))
        print('TeacherTable')
        for res in result:
            print(res)

        result = session.execute(select(HomeworkTable))
        print('HomeworkTable')
        for res in result:
            print(res)

        result = session.execute(select(HomeworkResultTable))
        print('HomeworkResultTable')
        for res in result:
            # print(res[0].author, res[0].homework)
            print(res)


if __name__ == '__main__':
    main()
