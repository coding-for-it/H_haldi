import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend

def get_brand_personality_radar(excel_path: str = "KPI_Data\kpi 7.xlsx", 
                              sheet_name: str = 'Sheet1') -> bytes:
    """
    Generate brand personality radar chart from Excel file
    
    Args:
        excel_path: Path to the Excel file
        sheet_name: Name of the sheet to read from
        
    Returns:
        bytes: PNG image data of the radar chart
    """
    try:
        # Read the Excel file
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
        
        # Process trait data
        trait_counts = df['Brand Personality Trait'].str.split(',').explode().str.strip().value_counts()
        trait_counts = trait_counts[~trait_counts.index.str.contains(r'\(Negative\)')]
        
        if trait_counts.empty:
            return b""
        
        # Prepare radar chart data
        labels = trait_counts.index.tolist()
        values = trait_counts.values.tolist()
        values += values[:1]
        labels += labels[:1]
        
        # Create radar chart
        plt.figure(figsize=(8, 8))
        ax = plt.subplot(111, polar=True)
        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=True)
        
        # Plot data
        ax.fill(angles, values, color='skyblue', alpha=0.4)
        ax.plot(angles, values, color='blue', linewidth=2)
        
        # Formatting
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels[:-1], fontsize=12)
        ax.set_yticks([max(values)*0.2, max(values)*0.4, max(values)*0.6, max(values)*0.8])
        ax.set_yticklabels([
            f'{int(max(values)*0.2)}',
            f'{int(max(values)*0.4)}',
            f'{int(max(values)*0.6)}',
            f'{int(max(values)*0.8)}'
        ], fontsize=12)
        ax.set_ylim(0, max(values))
        
        plt.title('Perceived Brand Personality Radar Chart', fontsize=16, fontweight='bold', pad=20)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        # Save to buffer
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        buf.seek(0)
        return buf.getvalue()
        
    except Exception as e:
        print(f"Error generating brand personality radar: {e}")
        return b""