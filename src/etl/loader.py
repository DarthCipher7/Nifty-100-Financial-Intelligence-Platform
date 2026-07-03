import pandas as pd
from pathlib import Path
from database import create_connection
from normalizer import normalize_company_id, normalize_year

BASE_PATH = Path("data/raw")

files = {
    "companies": BASE_PATH / "companies.xlsx",
    "profitandloss": BASE_PATH / "profitandloss.xlsx",
    "balancesheet": BASE_PATH / "balancesheet.xlsx",
    "cashflow": BASE_PATH / "cashflow.xlsx",
}


def load_excel(file_path, header=1):
    return pd.read_excel(file_path, header=header)


def clean_dataset(name, df):
    if "company_id" in df.columns:
        df["company_id"] = df["company_id"].apply(normalize_company_id)

    if name == "companies" and "id" in df.columns:
        df["id"] = df["id"].apply(normalize_company_id)

    if "year" in df.columns:
        df["year"] = df["year"].apply(normalize_year)

    return df


if __name__ == "__main__":
    datasets = {}

    for name, path in files.items():
        df = load_excel(path)
        df = clean_dataset(name, df)
        datasets[name] = df

    companies = datasets["companies"]
    pl = datasets["profitandloss"]
    bs = datasets["balancesheet"]
    cf = datasets["cashflow"]

    # Remove duplicate company-year rows
    pl = pl.drop_duplicates(subset=["company_id", "year"], keep="first")
    bs = bs.drop_duplicates(subset=["company_id", "year"], keep="first")
    cf = cf.drop_duplicates(subset=["company_id", "year"], keep="first")

    valid_ids = set(companies["id"])

    pl = pl[pl["company_id"].isin(valid_ids)]
    bs = bs[bs["company_id"].isin(valid_ids)]
    cf = cf[cf["company_id"].isin(valid_ids)]

    conn = create_connection()

    companies.to_sql("companies", conn, if_exists="replace", index=False)
    pl.to_sql("profitandloss", conn, if_exists="replace", index=False)
    bs.to_sql("balancesheet", conn, if_exists="replace", index=False)
    cf.to_sql("cashflow", conn, if_exists="replace", index=False)

    conn.close()

    print("\nDatabase updated successfully!")
    print("Tables loaded:")
    print("- companies")
    print("- profitandloss")
    print("- balancesheet")
    print("- cashflow")