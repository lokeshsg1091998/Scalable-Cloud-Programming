from datetime import datetime

class TaxEngine:

    @staticmethod
    def compute(gross, deductions):

        taxable_income = max(gross - deductions, 0)

        # PRSI
        prsi = taxable_income * 0.04

        # Income Tax
        if taxable_income <= 44000:
            income_tax = taxable_income * 0.20
        else:
            income_tax = (44000 * 0.20) + ((taxable_income - 44000) * 0.40)

        # USC
        usc = 0

        usc_bands = [
            (12012, 0.005),
            (27382, 0.02),
            (70044, 0.03),
            (float("inf"), 0.08)
        ]

        previous = 0

        for limit, rate in usc_bands:
            if taxable_income > previous:
                portion = min(taxable_income, limit) - previous
                usc += portion * rate
                previous = limit
            else:
                break

        total_tax = income_tax + usc + prsi

        net_income = taxable_income - total_tax

        # Marginal Rate
        if taxable_income <= 12012:
            marginal_rate = 24.5
        elif taxable_income <= 27382:
            marginal_rate = 26
        elif taxable_income <= 44000:
            marginal_rate = 27
        elif taxable_income <= 70044:
            marginal_rate = 47
        else:
            marginal_rate = 52

        return {
            "gross": gross,
            "deductions": deductions,
            "taxable_income": taxable_income,
            "income_tax": round(income_tax, 2),
            "usc": round(usc, 2),
            "prsi": round(prsi, 2),
            "tax_payable": round(total_tax, 2),
            "net_income": round(net_income, 2),
            "marginal_rate": marginal_rate,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }