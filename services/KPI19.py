import pandas as pd

def get_kpi19_sheet1_data():
    """
    Reads and processes Sheet1 from KPI-19.xlsx, converting NaN to None for JSON compliance.
    """
    file_path = "KPI_Data\KPI 19.xlsx"
    df = pd.read_excel(file_path, sheet_name="Sheet1")
    # Replace NaN with None for JSON serialization
    df = df.where(pd.notnull(df), None)
    return df.to_dict(orient="records")