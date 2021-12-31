from homework11.hw2 import Order, elder_discount, morning_discount


def test_morning_discount():
    """Testing morning discount works correctly"""
    assert morning_discount(100) == 75


def test_elder_discount():
    """Testing elder discount works correctly"""
    assert elder_discount(100) == 10


def test_order_strategy_setting():
    """Testing that strategy setting in Order class works correctly"""
    order_1 = Order(100, morning_discount)
    order_2 = Order(100, elder_discount)

    assert order_1.final_price() == 75
    assert order_2.final_price() == 10
