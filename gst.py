# taxes - gst.py
class GSTCalculator(TaxStrategy):
    """Applies GST split into CGST+SGST (intra) or IGST (inter)."""

    def __init__(self, cgst: Decimal, sgst: Decimal, igst: Decimal) -> None:
        for rate in (cgst, sgst, igst):
            if isinstance(rate, float):
                raise TypeError("rates must be Decimal, not float")
            if not (Decimal("0") <= rate <= Decimal("1")):
                raise ValueError("rates must be between 0 and 1")
        if cgst + sgst != igst:
            raise ValueError("CGST + SGST must equal IGST")

        self.cgst = cgst
        self.sgst = sgst
        self.igst = igst

    def apply(self, taxable: Money, context) -> TaxBreakdown:
        intra = bool(context.customer_state) and context.customer_state == context.seller_state
        if intra:
            cgst_amt = taxable * self.cgst
            sgst_amt = taxable * self.sgst
            components = [
                (f"CGST {self.cgst * 100}%", cgst_amt),
                (f"SGST {self.sgst * 100}%", sgst_amt),
            ]
            total = cgst_amt + sgst_amt
        else:
            igst_amt = taxable * self.igst
            components = [(f"IGST {self.igst * 100}%", igst_amt)]
            total = igst_amt

        return TaxBreakdown(components=components, total=total)

