from database import get_connection

class Calculation:

    @staticmethod
    def save(data):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO calculations 
            (gross_income, deductions, taxable_income, income_tax, usc, prsi, total_tax, net_income, marginal_tax_rate, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["gross"],
            data["deductions"],
            data["taxable_income"],
            data["income_tax"],
            data["usc"],
            data["prsi"],
            data["tax_payable"],
            data["net_income"],
            data["marginal_rate"],
            data["created_at"]
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def last_five():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM calculations
            ORDER BY id DESC
            LIMIT 5
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows