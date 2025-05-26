import pandas as pd

def get_sheet2_data():
    """Reads and returns Sheet2 data from KPI-14-2.xlsx"""
    df = pd.read_excel("KPI_Data\KPI 14(2).xlsx", sheet_name="Sheet2")
    return df

def analyze_data():
    """Processes Sheet2 data for API response"""
    df = get_sheet2_data()
    return df.to_dict(orient='records')