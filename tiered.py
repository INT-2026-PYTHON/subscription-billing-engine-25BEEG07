
# pricing - tiered.py
class TieredPricing(PricingStrategy):
    """Charges based on tiers of usage."""

    def __init__(self, tiers: list[Tier]) -> None:
        if not tiers:
            raise ValueError("tiers cannot be empty")

        # Validate contiguous ranges and currency consistency
        for i in range(len(tiers) - 1):
            if tiers[i+1].from_units != tiers[i].to_units:
                raise ValueError("tiers must be contiguous")
        for i, tier in enumerate(tiers):
            if tier.to_units is None and i != len(tiers) - 1:
                raise ValueError("only last tier can be open-ended")

        currencies = {tier.unit_price.currency for tier in tiers}
        if len(currencies) != 1:
            raise ValueError("all tiers must use the same currency")

        self.tiers = tiers

    def calculate(self, quantity: int) -> Money:
        if quantity < 0:
            raise ValueError("quantity cannot be negative")

        currency = self.tiers[0].unit_price.currency
        total = Money.zero(currency)

        for tier in self.tiers:
            if quantity <= tier.from_units:
                continue
            if tier.to_units is None:
                units_in_tier = quantity - tier.from_units
            else:
                units_in_tier = min(quantity, tier.to_units) - tier.from_units
            total += tier.unit_price * units_in_tier

        return total

