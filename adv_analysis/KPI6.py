import pandas as pd

# Hardcoded path to the Excel file
EXCEL_FILE_PATH = "KPI_Data\KPI6.xlsx"

def read_kpi6_excel():
    """
    Reads the KPI6 Excel file from a hardcoded path and returns a pandas DataFrame.
    Returns:
        pd.DataFrame: DataFrame of the first sheet.
    """
    try:
        df = pd.read_excel(EXCEL_FILE_PATH, sheet_name='Sheet1')
        return df
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None