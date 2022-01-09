# import sqlalchemy
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

#
from homework12.fill_models import create_models
from homework12.homework import HomeworkResult, Student, Teacher
from homework12.models import (HomeworkResultTable, HomeworkTable,
                               StudentTable, TeacherTable)


def select_valid_homeworks(session):
    task = select(HomeworkResultTable).filter_by(status=False)
    result = session.execute(task)
    return result


def main():

    engine = create_models()
    opp_teacher = Teacher('Daniil', 'Shadrin', engine, TeacherTable)
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin',
                                      engine, TeacherTable)

    lazy_student = Student('Roman', 'Petrov', engine, StudentTable)
    good_student = Student('Lev', 'Sokolov', engine, StudentTable)

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    print(datetime.today())

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
        print(result_4.author)
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    # temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    # temp_2 = Teacher.homework_done
    # assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    # print(Teacher.homework_done[oop_hw])
    # Teacher.reset_results()
    #
    # jedi_hw = Homework('Take the force with you', 2)
    # print(jedi_hw.is_active())

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
