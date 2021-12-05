from homework6.task01.oop_2 import Person


def test_person():
    """Testing creation of class Person instance"""
    name = 'Name'
    surname = 'Surname'

    person = Person(name, surname)

    assert person.first_name == name
    assert person.last_name == surname
