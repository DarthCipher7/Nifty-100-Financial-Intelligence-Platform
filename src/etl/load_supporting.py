import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = "db/nifty100.db"
DATA_PATH = Path("data/raw/supporting")

files = {
    "financial_ratios_source": "financial_ratios.xlsx",
    "market_cap": "market_cap.xlsx",
    "peer_groups": "peer_groups.xlsx",
    "sectors": "sectors.xlsx",
    "stock_prices": "stock_prices.xlsx"
}

conn = sqlite3.connect(DB_PATH)

print("\n========== LOADING SUPPORTING DATASETS ==========\n")

for table_name, file_name in files.items():

    file_path = DATA_PATH / file_name

    df = pd.read_excel(file_path)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"{table_name:<28} Loaded | Shape: {df.shape}")

conn.close()

print("\nAll supporting datasets loaded successfully!")