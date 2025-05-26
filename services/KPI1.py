import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI rendering

def get_attribute_frequency_chart(excel_path: str = "KPI_Data\KPI-1.xlsx", 
                                sheet_name: str = 'KPI-1') -> bytes:
    """
    Generate attribute frequency bar chart from Excel file
    
    Args:
        excel_path: Path to the Excel file
        sheet_name: Name of the sheet to read from
        
    Returns:
        bytes: PNG image data of the chart
    """
    try:
        # Read the Excel file
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
        
        # Count the frequency of each attribute
        attribute_counts = df['Attribute'].value_counts()
        
        # Return empty bytes if no data
        if attribute_counts.empty:
            return b""
        
        # Plot the bar chart with enhancements
        plt.figure(figsize=(12, 7))
        bars = plt.bar(attribute_counts.index, attribute_counts.values, color='skyblue', edgecolor='black')
        
        # Add value labels on each bar
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval),
                     ha='center', va='bottom', fontsize=12, fontweight='bold')
        
        plt.title('Frequency Score for Key Attribute Associations', fontsize=16, fontweight='bold')
        plt.xlabel('Attribute', fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.xticks(rotation=45, fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        # Save to BytesIO buffer
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        buf.seek(0)
        return buf.getvalue()
        
    except Exception as e:
        print(f"Error generating attribute frequency chart: {e}")
        return b""
