from database import get_connection

class Calculation:

    @staticmethod
    def save(data):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO calculations 
            (gross, deductions, taxable_income, tax_payable, net_income, marginal_rate, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            data["gross"],
            data["deductions"],
            data["taxable_income"],
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