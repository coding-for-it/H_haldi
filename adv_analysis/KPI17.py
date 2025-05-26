import pandas as pd
import numpy as np

def get_sheet1_data():
    """
    Reads and processes Sheet1 data, converting NaN to None for JSON compliance
    """
    file_path = "KPI_Data\KPI 17.xlsx"
    df = pd.read_excel(file_path, sheet_name="Sheet1")
    
    # Convert NaN to None for JSON compatibility
    cleaned_df = df.replace({np.nan: None})
    
    return cleaned_df.to_dict(orient="records")