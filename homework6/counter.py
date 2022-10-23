"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""
from typing import Any, Optional


def instances_counter(cls: object) -> object:
    """
    Store information about number of created cls instances

    :param cls: Class for which instances number is counted
    :type cls: object
    """
    instances_number = 0

    some_init = cls.__init__

    def init(self, *args: Any, **kwargs: Optional[Any]) -> None:
        """
        New init function which perform previous init functionality and
        instance number incrementation
        """
        nonlocal instances_number
        instances_number += 1
        some_init(self, *args, **kwargs)

    @staticmethod
    def get_created_instances() -> int:
        """Return number of created cls instances"""
        return instances_number

    def reset_instances_counter(self) -> int:
        """Return number of created cls instances and reset counter"""
        nonlocal instances_number
        self.instances_number = instances_number
        instances_number = 0
        return self.instances_number

    # Redefine class methods
    cls.__init__ = init
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
