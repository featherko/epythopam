"""Task 2.

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
assert order_1.final_price() == 50
order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""

from abc import ABC, abstractmethod


# flake8: noqa


class Strategy(ABC):
    @abstractmethod
    def final_price(self) -> float:
        pass


class MorningDiscount(Strategy):
    def final_price(self) -> float:
        return self.price - self.price * 0.5


class ElderDiscount(Strategy):
    def final_price(self) -> float:
        return self.price - self.price * 0.9


class Order:
    def __init__(self, price: float, strategy: Strategy) -> None:
        self.price = price
        self._strategy = strategy

    def final_price(self) -> float:
        return self._strategy.final_price(self)
