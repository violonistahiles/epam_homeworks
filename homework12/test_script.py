# from datetime import datetime

from sqlalchemy import create_engine, select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

# from homework12.client import DBClient
from homework12.models import (HomeworkResultTable, HomeworkTable,
                               StudentTable, TeacherTable)


def main(engine: Engine):

    # db_client = DBClient(engine)
    #
    # opp_teacher = db_client.create_teacher('Daniil', 'Shadrin')
    # advanced_python_teacher = db_client.create_teacher('Aleksandr',
    #                                                    'Smetanin')
    #
    # lazy_student = db_client.create_student('Roman', 'Petrov')
    # good_student = db_client.create_student('Lev', 'Sokolov')
    #
    # oop_hw = db_client.create_homework(opp_teacher, 'Learn OOP', 1)
    # docs_hw = db_client.create_homework(opp_teacher, 'Read docs', 5)
    #
    # print(datetime.today())
    #
    # result_1 = db_client.create_homeworkresult(good_student,
    #                                            oop_hw,
    #                                            'I have done this hw')
    # result_2 = db_client.create_homeworkresult(good_student,
    #                                            docs_hw,
    #                                            'I have done this hw too')
    # result_3 = db_client.create_homeworkresult(lazy_student,
    #                                            docs_hw,
    #                                            'done')
    #
    # db_client.check_homework(opp_teacher, result_1)
    #
    # db_client.check_homework(advanced_python_teacher, result_1)
    #
    # db_client.check_homework(opp_teacher, result_2)
    # db_client.check_homework(opp_teacher, result_3)

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
            print(res)


if __name__ == '__main__':
    engine = create_engine('sqlite:///main.db')
    main(engine)
