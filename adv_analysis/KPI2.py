import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend

def get_attribute_frequency_chart_kpi2_with_sentiment(excel_path: str = "KPI_Data\KPI 2.xlsx", 
                                                      sheet_name: str = 'Sheet1') -> bytes:
    """
    Generate stacked bar chart of sentiment breakdown by driver category from KPI-2 Excel file
    Args:
        excel_path: Path to the Excel file
        sheet_name: Name of the sheet to read from
    Returns:
        bytes: PNG image data of the chart
    """
    try:
        # Read the Excel file
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
        
        # Prepare the data
        sentiment_order = ['Positive', 'Neutral', 'Negative']
        color_map = {
            'Positive': '#8ED6FB',   # Light Blue
            'Neutral': '#D3D3D3',    # Light Gray
            'Negative': '#FF7F7F'    # Light Red
        }

        # Ensure Sentiment is categorical for correct stacking order
        df['Sentiment'] = pd.Categorical(df['Sentiment'], categories=sentiment_order, ordered=True)
        sentiment_driver_counts = df.groupby(['Sentiment Driver', 'Sentiment']).size().unstack(fill_value=0)[sentiment_order]

        # Plot the stacked bar chart with numbers on bars
        plt.figure(figsize=(14, 8))
        ax = sentiment_driver_counts.plot(
            kind='bar',
            stacked=True,
            color=[color_map[s] for s in sentiment_order]
        )

        # Add numbers on the bars
        for i, sentiment_driver in enumerate(sentiment_driver_counts.index):
            cumulative = 0
            for sentiment in sentiment_order:
                count = sentiment_driver_counts.loc[sentiment_driver, sentiment]
                if count > 0:
                    ax.text(i, cumulative + count / 2, str(count), ha='center', va='center', fontsize=10, color='black')
                    cumulative += count

        plt.title('Sentiment Breakdown by Driver Category with Counts')
        plt.xlabel('Sentiment Driver')
        plt.ylabel('Number of Reviews')
        plt.xticks(rotation=45, ha='right')
        plt.legend(title='Sentiment')
        plt.tight_layout()

        # Save to BytesIO buffer
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        buf.seek(0)
        return buf.getvalue()

    except Exception as e:
        print(f"Error generating sentiment breakdown chart for KPI-2: {e}")
        return b""