from homework11.hw1 import SimplifiedEnum


def test_class_creation_by_metaclass():
    """
    Testing that class creation with metaclass sets values from __keys class
    attribute as class attributes
    """
    colors = ("RED", "BLUE", "ORANGE", "BLACK")
    sizes = ("XL", "L", "M", "S", "XS")

    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = colors

    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = sizes

    for attribute in colors:
        assert hasattr(ColorsEnum, attribute)
        assert getattr(ColorsEnum, attribute) == attribute

    for attribute in sizes:
        assert hasattr(SizesEnum, attribute)
        assert getattr(SizesEnum, attribute) == attribute
