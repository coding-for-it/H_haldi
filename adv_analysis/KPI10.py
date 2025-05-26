import pandas as pd
import numpy as np

KPI10_FILE_PATH = "KPI_Data\KPI 10.xlsx"

def get_comparison_sheet_sections():
    # Load the sheet
    xls = pd.ExcelFile(KPI10_FILE_PATH)
    df = pd.read_excel(xls, sheet_name='Comparison')

    # Clean up: drop empty rows and columns
    df_clean = df.dropna(axis=0, how='all').dropna(axis=1, how='all')

    # --- 1. Company comparison table (first 4 rows and relevant columns) ---
    company_cols = [
        'Company', 'EBI', 'Overall_Rating', 'WLB_Rating',
        'Culture_Rating', 'Num_Glassdoor_Reviews', 'Num_LinkedIn_Posts', 'Rank'
    ]
    company_comparison = df_clean.iloc[:4][company_cols]
    company_comparison_dict = company_comparison.where(pd.notnull(company_comparison), None).to_dict(orient='records')

    # --- 2. Ranking (best to least preferred) ---
    ranking = company_comparison[['Company', 'Rank']].sort_values(by='Rank')
    ranking_dict = ranking.where(pd.notnull(ranking), None).to_dict(orient='records')

    # --- 3. Summary/analysis section ---
    # The summary text is in the lower part of the sheet, in columns 5-9 (F-J, zero-indexed 5:10)
    # We'll extract non-empty lines as summary
    summary_rows = df.iloc[10:50, 5:10].dropna(how='all')
    summary_text = summary_rows.apply(lambda row: ' '.join(row.dropna().astype(str)), axis=1).tolist()
    summary_text_clean = [line for line in summary_text if line.strip() != '']

    return {
        "company_comparison": company_comparison_dict,
        "ranking": ranking_dict,
        "summary": summary_text_clean
    }