from sqlalchemy import (BOOLEAN, TIMESTAMP, Column, ForeignKey, Integer,
                        String, create_engine)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class StudentTable(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)

    homeworks = relationship('HomeworkResultTable', backref='student')

    def __repr__(self):
        return f"Student(id={self.id!r}, name={self.name!r}," \
               f" surname={self.surname!r})"


class TeacherTable(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)

    homeworks = relationship('HomeworkTable', backref='teacher')

    def __repr__(self):
        return f"Teacher(id={self.id!r}, name={self.name!r}," \
               f" surname={self.surname!r})"


class HomeworkTable(Base):
    __tablename__ = 'homeworks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    created = Column(TIMESTAMP)
    final_day = Column(TIMESTAMP)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    solved = relationship('HomeworkResultTable', backref='origin')

    def __repr__(self):
        return f"Homework(id={self.id!r}, text={self.text!r}," \
               f" created={self.created!r}), final_day={self.final_day!r}"


class HomeworkResultTable(Base):
    __tablename__ = 'homework_results'

    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(Integer, ForeignKey('students.id'))
    homework = Column(Integer, ForeignKey('homeworks.id'))
    solution = Column(String)
    created = Column(TIMESTAMP)
    status = Column(BOOLEAN, default=False)

    def __repr__(self):
        return f"HomeworkResult(id={self.id!r}, solution={self.solution!r}," \
               f" created={self.created!r}), status={self.status!r}"


if __name__ == '__main__':
    engine = create_engine('sqlite:///main.db')
    Base.metadata.create_all(engine)
