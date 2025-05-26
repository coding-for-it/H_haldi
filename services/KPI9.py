import pandas as pd

# Path to your KPI-9 Excel file (update this path as needed)
KPI9_FILE_PATH = "KPI_Data\KPI 9.xlsx"

def get_kpi9_reviews_data():
    """
    Reads the 'Reviews' sheet from the KPI-9 Excel file and returns it as a list of dicts.
    """
    df = pd.read_excel(KPI9_FILE_PATH, sheet_name="Comparative Summary")
    # Replace NaN with None for JSON compatibility
    return df.where(pd.notnull(df), None).to_dict(orient="records")