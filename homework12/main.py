import sqlalchemy
from sqlalchemy import (BOOLEAN, TIMESTAMP, Column, ForeignKey, Integer,
                        String, create_engine)
from sqlalchemy.orm import Session, declarative_base, relationship

print(sqlalchemy.__version__)
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
#     )
#     conn.commit()
#
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM some_table"))
#     for row in result:
#         print(f"x: {row.x}  y: {row.y}")

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)

    homeworks = relationship('HomeworkResult', backref='student')

    def __repr__(self):
        return f"Student(id={self.id!r}, name={self.name!r}," \
               f" surname={self.surname!r})"


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)

    homeworks = relationship('Homework', backref='teacher')

    def __repr__(self):
        return f"Teacher(id={self.id!r}, name={self.name!r}," \
               f" surname={self.surname!r})"


class Homework(Base):
    __tablename__ = 'homeworks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    created = Column(TIMESTAMP)
    final_day = Column(TIMESTAMP)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    solved = relationship('HomeworkResult', backref='origin')

    def __repr__(self):
        return f"Homework(id={self.id!r}, text={self.text!r}," \
               f" created={self.created!r}), final_day={self.final_day!r}"


class HomeworkResult(Base):
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


Base.metadata.create_all(engine)

student1 = Student(name='Oleg', surname='TheFirst')
student2 = Student(name='Vladimir', surname='TheSecond')

session = Session(engine)
session.add(student1)
session.add(student2)

session.flush()
some_student = session.get(Student, 1)
print(some_student)
