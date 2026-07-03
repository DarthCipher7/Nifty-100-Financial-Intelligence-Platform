import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT
    company_id,
    roe,
    debt_equity,
    sales_growth
FROM financial_ratios
WHERE year = 2024
AND roe > 20
AND debt_equity < 0.5
AND sales_growth > 10
ORDER BY roe DESC
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()