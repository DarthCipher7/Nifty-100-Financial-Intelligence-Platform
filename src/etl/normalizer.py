import re
import pandas as pd


def normalize_company_id(company_id):
    if pd.isna(company_id):
        return company_id
    return str(company_id).strip().upper()


def normalize_year(year_value):
    if pd.isna(year_value):
        return None

    year_str = str(year_value).strip()

    match_4digit = re.search(r'(20\d{2})', year_str)
    if match_4digit:
        return int(match_4digit.group(1))

    match_2digit = re.search(r'(\d{2})$', year_str)
    if match_2digit:
        return int("20" + match_2digit.group(1))

    return None