import pandas as pd

def get_sheet2_data():
    """
    Reads and returns Sheet2 data from KPI-15.xlsx as a list of dicts.
    """
    file_path = "KPI_Data\KPI 15.xlsx"  # Ensure this file is in the same directory as your script
    df = pd.read_excel(file_path, sheet_name="Sheet2")
    return df.to_dict(orient="records")