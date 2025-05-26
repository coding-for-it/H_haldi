import pandas as pd

def get_kpi18_sheet5_data():
    """
    Reads and processes Sheet5 from KPI-18.xlsx, converting NaN to None for JSON compliance.
    """
    file_path = "KPI_Data\KPI 18.xlsx"
    df = pd.read_excel(file_path, sheet_name="Sheet5")
    # Replace NaN with None for JSON serialization
    df = df.where(pd.notnull(df), None)
    return df.to_dict(orient="records")