from datetime import datetime

class TaxEngine:

    @staticmethod
    def compute(gross, deductions):

        taxable_income = max(gross - deductions, 0)

        brackets = [
            (40000, 0.20),
            (80000, 0.40),
            (float("inf"), 0.45)
        ]

        tax = 0
        previous_limit = 0

        # Lambda function
        calculate_segment = lambda income, limit, prev, rate: max(min(income, limit) - prev, 0) * rate

        for limit, rate in brackets:
            tax += calculate_segment(taxable_income, limit, previous_limit, rate)
            previous_limit = limit

        marginal_rate = next(
            (rate for limit, rate in brackets if taxable_income <= limit),
            0.45
        )

        net_income = taxable_income - tax

        return {
            "gross": gross,
            "deductions": deductions,
            "taxable_income": taxable_income,
            "tax_payable": tax,
            "net_income": net_income,
            "marginal_rate": marginal_rate * 100,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }