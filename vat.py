# taxes - vat.py
class VATCalculator(TaxCalculator):
                # TODO Day 1
        from decimal import Decimal
        class VATCalculator(TaxStrategy):

    def __init__(self, rate: Decimal) -> None:
        if isinstance(rate, float):
            raise TypeError("rate must be a Decimal, not float")
        if not (Decimal("0") <= rate <= Decimal("1")):
            raise ValueError("rate must be between 0 and 1")
        self.rate = rate

    def apply(self, taxable: Money, context) -> TaxBreakdown:
        vat = taxable * self.rate
        label = f"VAT {self.rate * 100}%"
        return TaxBreakdown(components=[(label, vat)], total=vat)
