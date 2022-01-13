from homework6.counter import instances_counter


def test_instances_counter():
    """Testing instances_counter works as expected"""

    @instances_counter
    class User:
        pass

    assert User.get_created_instances() == 0

    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3
    assert user.reset_instances_counter() == 3
    assert User.get_created_instances() == 0
