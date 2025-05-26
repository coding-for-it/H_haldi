import pandas as pd

def get_kpi20_sheet2_data():
    """
    Reads and processes Sheet2 from KPI-20.xlsx, converting NaN to None for JSON compliance.
    """
    file_path = "KPI_Data\KPI 20.xlsx"
    df = pd.read_excel(file_path, sheet_name="Sheet2")
    # Replace NaN with None for JSON serialization
    df = df.where(pd.notnull(df), None)
    return df.to_dict(orient="records")