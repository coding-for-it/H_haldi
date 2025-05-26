import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend

def get_kpi8_dashboard_chart_and_data(
    excel_path: str = "KPI_Data\KPI 8.xlsx", 
    sheet_name: str = "Sheet3"
) -> tuple:
    """
    Generates KPI-8 dashboard chart and returns Sheet3 data
    Returns:
        tuple: (PNG image bytes, DataFrame)
    """
    try:
        # Read Excel file
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
        
        # Validate required columns
        required_columns = ['Product', 'Avg Rating', 'Review Trend (% YoY)', 'Search Interest']
        if not all(col in df.columns for col in required_columns):
            return b"", pd.DataFrame()

        if df.empty:
            return b"", pd.DataFrame()

        # Extract data
        products = df['Product']
        avg_ratings = df['Avg Rating']
        review_trend = df['Review Trend (% YoY)']
        search_interest = df['Search Interest']

        # Create vertical bar chart
        plt.figure(figsize=(14, 16))
        
        # 1. Average Rating
        plt.subplot(3, 1, 1)
        bars = plt.bar(products, avg_ratings, color='skyblue')
        plt.title('Average Rating', fontsize=14)
        plt.xticks(rotation=45)
        plt.ylim(3.5, 5)
        
        # Add value labels
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, 
                     f'{yval:.1f}', ha='center', va='bottom')

        # 2. Review Trend
        plt.subplot(3, 1, 2)
        colors = ['green' if x > 0 else 'red' for x in review_trend]
        bars = plt.bar(products, review_trend, color=colors)
        plt.title('Review Trend (% YoY)', fontsize=14)
        plt.xticks(rotation=45)
        
        # Add value labels
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval, 
                     f'{yval}%', ha='center', va='bottom' if yval > 0 else 'top')

        # 3. Search Interest
        plt.subplot(3, 1, 3)
        bars = plt.bar(products, search_interest, color='orange')
        plt.title('Search Interest Score', fontsize=14)
        plt.xticks(rotation=45)
        
        # Add value labels
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval, 
                     str(yval), ha='center', va='bottom')

        plt.tight_layout()
        
        # Save to buffer
        buf = BytesIO()
        plt.savefig(buf, format='png', dpi=200, bbox_inches='tight')
        plt.close()
        buf.seek(0)
        
        return buf.getvalue(), df

    except Exception as e:
        print(f"Error generating dashboard: {str(e)}")
        return b"", pd.DataFrame()