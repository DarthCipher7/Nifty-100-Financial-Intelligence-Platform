import pandas as pd
from pathlib import Path

folder = Path("data/raw/supporting")

for file in folder.glob("*.xlsx"):
    print("\n" + "=" * 70)
    print(file.name)

    df = pd.read_excel(file)

    print("Shape:", df.shape)
    print("Columns:")
    print(df.columns.tolist())

    print("\nFirst 5 rows:")
    print(df.head())