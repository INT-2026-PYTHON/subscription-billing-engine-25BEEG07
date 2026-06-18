# discounts - fixed.py
class FixedAmountDiscount(Discount):
    class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: Money) -> None:
        if not isinstance(amount, Money):
            raise TypeError("amount must be a Money instance")
        if amount.is_negative():
            raise ValueError("amount cannot be negative")
        self.amount = amount

    def apply(self, subtotal: Money, context) -> Money:
        if self.amount.currency != subtotal.currency:
            raise ValueError("currency mismatch")
        return min(self.amount, subtotal)



