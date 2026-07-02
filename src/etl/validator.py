def check_duplicate_company_ids(companies_df):
    duplicates = companies_df[companies_df.duplicated(subset=["id"], keep=False)]
    return duplicates


def check_duplicate_company_year(df):
    duplicates = df[df.duplicated(subset=["company_id", "year"], keep=False)]
    return duplicates


def check_foreign_keys(companies_df, child_df):
    valid_ids = set(companies_df["id"])
    invalid_rows = child_df[~child_df["company_id"].isin(valid_ids)]
    return invalid_rows


def check_negative_sales(pl_df):
    invalid_rows = pl_df[pl_df["sales"] <= 0]
    return invalid_rows