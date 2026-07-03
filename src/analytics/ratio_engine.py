import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

pl = pd.read_sql("SELECT * FROM profitandloss", conn)
bs = pd.read_sql("SELECT * FROM balancesheet", conn)

merged = pd.merge(
    pl,
    bs,
    on=["company_id", "year"],
    how="inner"
)

print("Merged Shape:", merged.shape)

merged["equity"] = merged["equity_capital"] + merged["reserves"]

merged["roe"] = (merged["net_profit"] / merged["equity"]) * 100
merged["debt_equity"] = merged["borrowings"] / merged["equity"]
merged["opm"] = (merged["operating_profit"] / merged["sales"]) * 100
merged["net_margin"] = (merged["net_profit"] / merged["sales"]) * 100

merged["ebit"] = merged["operating_profit"] - merged["depreciation"]
merged["capital_employed"] = merged["total_assets"] - merged["other_liabilities"]
merged["roce"] = (merged["ebit"] / merged["capital_employed"]) * 100

# Additional KPIs
merged["eps_value"] = merged["eps"]
merged["dividend_payout_value"] = merged["dividend_payout"]

merged = merged.sort_values(["company_id", "year"])
merged["sales_growth"] = merged.groupby("company_id")["sales"].pct_change() * 100

# Anomaly Filtering
merged.loc[(merged["roe"] < -100) | (merged["roe"] > 200), "roe"] = None
merged.loc[(merged["debt_equity"] < 0) | (merged["debt_equity"] > 10), "debt_equity"] = None
merged.loc[(merged["opm"] < -100) | (merged["opm"] > 100), "opm"] = None
merged.loc[(merged["net_margin"] < -100) | (merged["net_margin"] > 100), "net_margin"] = None
merged.loc[(merged["roce"] < -100) | (merged["roce"] > 200), "roce"] = None

ratios = merged[
    [
        "company_id",
        "year",
        "roe",
        "debt_equity",
        "opm",
        "net_margin",
        "roce",
        "eps_value",
        "dividend_payout_value",
        "sales_growth"
    ]
]

print(ratios.head())

ratios.to_sql("financial_ratios", conn, if_exists="replace", index=False)

conn.close()

print("\nfinancial_ratios table updated successfully!")