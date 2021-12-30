from homework11.hw1 import SimplifiedEnum


def test_class_creation_by_metaclass():
    """
    Testing that class creation with metaclass sets values from __keys class
    attribute as class attributes
    """
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"
