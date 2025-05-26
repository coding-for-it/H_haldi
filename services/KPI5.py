# services/KPI5.py

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO

matplotlib.use('Agg')  # Use non-GUI backend for server environments

def get_kpi5_chart(excel_path: str = "KPI_Data\KPI5.xlsx", sheet_name: str = "KPI5") -> bytes:
    """
    Generate a bar chart for average engagement rate per content type from an Excel file.

    Args:
        excel_path: Path to the Excel file.
        sheet_name: Name of the sheet to read from.

    Returns:
        bytes: PNG image data of the chart, or b"" if no data/error.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
    except Exception as e:
        print(f"Error reading Excel or sheet: {e}")
        return b""

    required_columns = ['Content Type', 'Engagement Rate (%)']
    if not all(col in df.columns for col in required_columns):
        print(f"Missing required columns: {required_columns}")
        return b""

    # Calculate average engagement rate per content type
    avg_engagement = df.groupby('Content Type')['Engagement Rate (%)'].mean().reset_index()
    avg_engagement = avg_engagement.sort_values(by='Engagement Rate (%)', ascending=False)

    if avg_engagement.empty:
        return b""

    # Plot the bar chart
    plt.figure(figsize=(12, 7))
    bars = plt.bar(
        avg_engagement['Content Type'],
        avg_engagement['Engagement Rate (%)'],
        color='skyblue',
        edgecolor='black'
    )

    # Add value labels on each bar
    for bar in bars:
     height = bar.get_height()
     plt.text(bar.get_x() + bar.get_width()/2, height + 0.5,
             f"{height:.2f}%", ha='center', va='bottom', fontsize=12, fontweight='bold')


    plt.title('Average Engagement Rate per Content Type', fontsize=16, fontweight='bold')
    plt.xlabel('Average Engagement Rate (%)', fontsize=14)
    plt.ylabel('Content Type', fontsize=14)
    plt.yticks(fontsize=12)
    plt.xticks(fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf.getvalue()