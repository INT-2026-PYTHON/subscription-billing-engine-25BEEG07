# pricing -flat.py
class FlatRate(PricingStrategy):
    """Charges a fixed amount every billing period."""

    def __init__(self, amount: Money) -> None:
        if not isinstance(amount, Money):
            raise TypeError(f"FlatRate requires Money, got {type(amount).__name__}")
        if amount.is_negative():
            raise ValueError("FlatRate amount must be non-negative")
        self._amount = amount

    def calculate(self, quantity: int) -> Money:
        if not isinstance(quantity, int):
            raise TypeError(f"Quantity must be int, got {type(quantity).__name__}")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")
        return self._amount