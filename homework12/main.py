# import sqlalchemy
# from sqlalchemy import (BOOLEAN, TIMESTAMP, Column, ForeignKey, Integer,
#                         String, create_engine, select)
# from sqlalchemy.orm import Session, declarative_base, relationship
# from datetime import datetime
# import logging
#
# from homework12.fill_models import create_models
# from homework12.models import (StudentTable, TeacherTable,
#                                HomeworkTable, HomeworkResultTable)
from homework12.homework import Homework, HomeworkResult, Student, Teacher


def main():
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
        print(result_4.author)
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()

    jedi_hw = Homework('Take the force with you', 2)
    print(jedi_hw.is_active())


if __name__ == '__main__':
    main()
