
# pricing - usage.py
class UsageBased(PricingStrategy):
    """Charges `unit_price * quantity`."""

    def __init__(self, unit_price: Money) -> None:
        if not isinstance(unit_price, Money):
            raise TypeError(f"UsageBased requires Money, got {type(unit_price).__name__}")
        if unit_price.is_negative():
            raise ValueError("UsageBased unit price must be non-negative")
        self._unit_price = unit_price

    def calculate(self, quantity: int) -> Money:
        if not isinstance(quantity, int):
            raise TypeError(f"Quantity must be int, got {type(quantity).__name__}")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")
        return self._unit_price * quantity
