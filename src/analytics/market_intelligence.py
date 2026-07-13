import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT
    company_id,
    year,
    market_cap_crore
FROM market_cap
ORDER BY market_cap_crore DESC
LIMIT 20;
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()