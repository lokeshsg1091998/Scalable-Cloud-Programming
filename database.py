import sqlite3

DATABASE = "tax.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gross_income REAL NOT NULL,
            deductions REAL NOT NULL,
            taxable_income REAL NOT NULL,
            income_tax REAL NOT NULL,
            usc REAL NOT NULL,
            prsi REAL NOT NULL,
            total_tax REAL NOT NULL,
            net_income REAL NOT NULL,
            marginal_tax_rate REAL NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()