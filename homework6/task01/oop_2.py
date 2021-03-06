"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict
from typing import Union


class DeadlineError(Exception):
    """This homework is already overdue"""


class HomeworkTypeError(Exception):
    """Homework parameter must be instance of class Homework"""


class TimeToSolveError(Exception):
    """Days to solve task can't be negative"""


class Person:
    """Basic class for any person"""
    def __init__(self, first_name: str, last_name: str):
        """
        :param first_name: First name of the person
        :type first_name: str
        :param last_name: Last name of the person
        :type last_name: str
        """
        self.first_name = first_name
        self.last_name = last_name


class Homework:
    """Class for storing information about task and its time to complete"""
    def __init__(self, text: str, time_limit: int):
        """
        :param text: Task description
        :type text: str
        :param time_limit: Time to solve task
        :type time_limit: int
        """
        if time_limit < 0:
            raise TimeToSolveError

        self._text = text
        self._created = datetime.datetime.now()
        self._final_day = self._created + datetime.timedelta(days=time_limit)

    @property
    def deadline(self) -> datetime.timedelta:
        """Time in days to complete the task"""
        return self._final_day - datetime.datetime.now()

    def is_active(self) -> bool:
        """Check if there is time to solve the task"""
        return not datetime.datetime.now() >= self._final_day


class HomeworkResult:
    """Store information about homework executor and result"""
    def __init__(self,
                 author: Person,
                 homework: Homework,
                 solution: str):
        """
        :param author: Person who created solution for a task
        :type author: Person
        :param homework: Task to which solution related
        :type homework: Homework
        :param solution: Solution for a task
        :type solution: str
        """
        if not isinstance(homework, Homework):
            raise HomeworkTypeError('You gave a not Homework object')

        self.homework = homework
        self.author = author
        self.solution = solution
        self.created = datetime.datetime.now()
        self._attributes = ['homework', 'author', 'solution']

    def __eq__(self, other):
        for attribute in self._attributes:
            if self.__dict__[attribute] != other.__dict__[attribute]:
                return False
        return True

    def __hash__(self):
        return hash(tuple((self.__dict__[attr] for attr in self._attributes)))


class Student(Person):
    """Student class which can check task info"""
    def do_homework(self,
                    homework: Homework,
                    solution: str
                    ) -> Union[HomeworkResult, None]:
        """
        Create instance of homework solution by current student

        :param homework: Task to which student create solution
        :type homework: Homework
        :param solution: String description of the solution to the task
        :type solution: str
        :return: HomeworkResult instance with information about solution
        :rtype: HomeworkResult
        """
        if not homework.is_active():
            raise DeadlineError('You are late')
        return HomeworkResult(self, homework, solution)


class Teacher(Person):
    """Abstract teacher with first and last name which can create task"""
    # Storage for homework and its solutions
    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text: str, days_to_solve: int) -> Homework:
        """
        Create Homework instance

        :param text: String definition of task
        :type text: str
        :param days_to_solve: Time in days to solve task
        :type days_to_solve: int
        :return: Homework instance
        :rtype: Homework
        """
        return Homework(text, days_to_solve)

    def check_homework(self, result: HomeworkResult) -> bool:
        """
        Check if number of symbols in solution is greater then 5 and
        then add solution to solutions container

        :param result: Instance of the solution for a task
        :type result: HomeworkResult
        :return: State of homework result checking
        :rtype: bool
        """
        if len(result.solution) > 5:
            self.homework_done[result.homework].add(result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework: Union[None, Homework] = None) -> None:
        """
        Delete one or all homework examples from homework storage

        :param homework: Homework to delete from storage
        :type homework: Homework
        :return: None
        :rtype: None
        """
        if homework:
            cls.homework_done.pop(homework)
        else:
            cls.homework_done.clear()


if __name__ == '__main__':
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
