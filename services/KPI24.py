import pandas as pd
import numpy as np

def get_kpi24_sheet3_data():
    """
    Reads and processes Sheet3 from KPI-24.xlsx, removes all rows with NaN or infinite values,
    and returns only fully valid, readable rows for JSON compliance.
    """
    file_path = r("KPI_Data\KPI 24.xlsx")
    df = pd.read_excel(file_path, sheet_name="Sheet3")
    # Replace inf/-inf with NaN
    df = df.replace([np.inf, -np.inf], np.nan)
    # Drop all rows that have any NaN (including those that were originally null or infinite)
    df = df.dropna(how='any')
    # Optionally, strip whitespace from string columns for readability
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()
    return df.to_dict(orient="records")

def get_kpi24_qualitative_assessment_details():
    """
    Reads and processes 'Qualitative Assessment Details' from Sheet3, removing null/empty entries.
    """
    file_path = "KPI_Data\KPI 24.xlsx"
    df = pd.read_excel(file_path, sheet_name="Sheet4")
    # Only keep the 'Qualitative Assessment Details' column if it exists
    col_candidates = [col for col in df.columns if 'Qualitative Assessment Details' in col]
    if not col_candidates:
        return []
    col = col_candidates[0]
    # Drop rows where the column is NaN/None/empty string
    filtered = df[[col]].dropna()
    filtered = filtered[filtered[col].astype(str).str.strip() != ""]
    # Convert to list of dicts for API
    return filtered.to_dict(orient="records")