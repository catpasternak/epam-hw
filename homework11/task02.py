"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75
order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""
from abc import ABC, abstractmethod


class Order:
    """Common interface for orders with different discount strategies.
    Can calculate final price depending on discount strategy chosen.
    :param price: order price
    :type price: float
    :param discount_strategy: discount strategy to apply to order price
    :type discount_strategy: :class:`DiscountStrategy`
    """

    def __init__(self, price, discount_strategy):
        """Constructor method."""
        self.price = price
        self._discount_strategy = discount_strategy

    @property
    def discount_strategy(self):
        return self._discount_strategy

    @discount_strategy.setter
    def discount_startegy(self, strategy):
        self._discount_strategy = strategy

    def final_price(self):
        """Calculates final price using discount strategy.
        :returns: final order price after discount
        :rtype: float
        """
        discount = self._discount_strategy(self.price).count_discount()
        return round(self.price - discount, 2)


class DiscountStrategy(ABC):
    """Discount strategy algorithm common to different discount strategies.
    Strategies interface is defined by this class structure.
    :param price: order price
    :type price: float
    """

    def __init__(self, price):
        self.price = price

    @abstractmethod
    def count_discount(self):
        """Class method common to all discount strategies.
        :returns: absolute value of discount
        :rtype: float
        """
        pass
