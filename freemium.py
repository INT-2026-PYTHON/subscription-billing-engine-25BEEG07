# pricing - freemium.py
class Freemium(PricingStrategy):
    from billing_engine.money import Money
from billing_engine.pricing.base import PricingStrategy

class Freemium(PricingStrategy):
    """Free up to a quota, then charges using another strategy."""

    def __init__(self, free_quota: int, overage_strategy: PricingStrategy) -> None:
        if free_quota < 0:
            raise ValueError("free_quota cannot be negative")
        if not isinstance(overage_strategy, PricingStrategy):
            raise TypeError("overage_strategy must be a PricingStrategy")
        self.free_quota = free_quota
        self.overage_strategy = overage_strategy

    def calculate(self, quantity: int) -> Money:
        currency = self.overage_strategy.calculate(0).currency
        if quantity <= self.free_quota:
            return Money.zero(currency)
        return self.overage_strategy.calculate(quantity - self.free_quota)

