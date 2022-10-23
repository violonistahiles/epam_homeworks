from typing import Callable


class Order:
    def __init__(self, price: int, discount_method: Callable):
        """
        Create class instance for calculating final price by chosen
        discount strategy

        :param price: Initial price value
        :type price: int
        :param discount_method: Method to calculate price after discount
        :type discount_method: Callable
        """
        self.price = price
        self.discount_method = discount_method

    def final_price(self) -> float:
        """
        Calculate and return price after discount

        :return: Price after discount
        :rtype: float
        """
        return self.discount_method(self.price)


def morning_discount(order: int) -> float:
    """
    Calculate price after morning discount

    :param order: Start price
    :type order: int
    :return: Price after discount
    :rtype: float
    """
    discount = 0.25
    return order - order * discount


def elder_discount(order: int) -> float:
    """
    Calculate price after elder discount

    :param order: Start price
    :type order: int
    :return: Price after discount
    :rtype: float
    """
    discount = 0.9
    return order - order * discount
