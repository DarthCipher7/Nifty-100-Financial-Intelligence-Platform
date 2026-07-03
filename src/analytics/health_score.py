import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT *
FROM financial_ratios
WHERE year = 2024
"""

df = pd.read_sql(query, conn)

# Fill nulls
df = df.fillna(0)

# Cap extreme values
df["roe_capped"] = df["roe"].clip(upper=50)
df["sales_growth_capped"] = df["sales_growth"].clip(lower=0, upper=30)
df["debt_equity_capped"] = df["debt_equity"].clip(lower=0, upper=3)

# Weighted scoring model
df["roe_score"] = (df["roe_capped"] / 50) * 40
df["growth_score"] = (df["sales_growth_capped"] / 30) * 30
df["debt_score"] = ((3 - df["debt_equity_capped"]) / 3) * 30

df["health_score"] = (
    df["roe_score"] +
    df["growth_score"] +
    df["debt_score"]
)

df = df.sort_values("health_score", ascending=False)

print(df[["company_id", "health_score"]].head(10))

conn.close()