import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

peer_group = "Private Banks"

query = f"""
SELECT
    pg.peer_group_name,
    pg.company_id,
    pg.is_benchmark,
    fr.roe,
    fr.sales_growth,
    cr.health_score,
    cr.rank
FROM peer_groups pg

LEFT JOIN financial_ratios fr
ON pg.company_id = fr.company_id
AND fr.year = 2024

LEFT JOIN (
    SELECT
        company_id,
        health_score,
        rank
    FROM company_rankings
) cr
ON pg.company_id = cr.company_id

WHERE pg.peer_group_name = '{peer_group}'

ORDER BY cr.rank;
"""

df = pd.read_sql(query, conn)

print("\n========== PEER COMPARISON ==========\n")
print(df)

conn.close()