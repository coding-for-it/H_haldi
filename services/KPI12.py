import pandas as pd
import numpy as np

KPI12_FILE_PATH = "KPI_Data\KPI 12.xlsx"

def analyze_kpi12_data():
    try:
        # Read Sheet1 data
        df_sheet1 = pd.read_excel(KPI12_FILE_PATH, sheet_name="Sheet1")
        
        # Clean data
        df_sheet1 = df_sheet1.replace({np.nan: None})
        
        # Calculate metrics
        total_samples = len(df_sheet1)
        evangelist_count = df_sheet1['Evangelist (Yes/No)'].eq('Yes').sum()
        evangelist_rate = round(evangelist_count / total_samples, 3) if total_samples > 0 else 0
        
        # Create KPI 12 formatted output
        kpi12_output = [
            {"Representation": "Total Sample Size", "Unnamed: 1": total_samples},
           # {"Representation": None, "Unnamed: 1": None},
            {"Representation": "Evangelist Mentions:", "Unnamed: 1": f"{evangelist_count}/{total_samples}"},
            #{"Representation": None, "Unnamed: 1": None},
            {"Representation": "Brand Evangelism Rate:", "Unnamed: 1": evangelist_rate}
        ]
        
        return kpi12_output
        
    except Exception as e:
        print(f"Error processing KPI-12 file: {str(e)}")
        return []