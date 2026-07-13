import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT
    s.broad_sector,
    COUNT(DISTINCT fr.company_id) AS companies,
    ROUND(AVG(fr.roe),2) AS avg_roe,
    ROUND(AVG(fr.sales_growth),2) AS avg_sales_growth,
    ROUND(AVG(mc.market_cap_crore),2) AS avg_market_cap
FROM financial_ratios fr

JOIN sectors s
ON fr.company_id = s.company_id

LEFT JOIN market_cap mc
ON fr.company_id = mc.company_id
AND fr.year = mc.year

WHERE fr.year = 2024

GROUP BY s.broad_sector

ORDER BY avg_roe DESC;
"""

sector_df = pd.read_sql(query, conn)

print("\n========== SECTOR ANALYTICS ==========\n")
print(sector_df)

conn.close()