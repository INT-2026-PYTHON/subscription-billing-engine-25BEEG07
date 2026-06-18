# discounts - percentage.py
class PercentageDiscount(Discount):
    from decimal import Decimal
from billing_engine.money import Money
from billing_engine.discounts.base import DiscountStrategy

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: Decimal) -> None:
        if isinstance(percentage, float):
            raise TypeError("percentage must be a Decimal, not float")
        if not (Decimal("0") <= percentage <= Decimal("1")):
            raise ValueError("percentage must be between 0 and 1")
        self.percentage = percentage

    def apply(self, subtotal: Money, context) -> Money:
        return subtotal * self.percentage

