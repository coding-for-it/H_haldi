from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def get_kpi3_sheet1_campaign_timeline_chart(excel_path: str = "KPI_Data\KPI 3.xlsx", sheet_name: str = "Sheet1") -> bytes:
    """
    Generate campaign timeline chart from KPI-3.xlsx Sheet1 and return as PNG bytes.
    Args:
        excel_path: Path to the Excel file
        sheet_name: Name of the sheet to read from
    Returns:
        bytes: PNG image data of the chart
    """
    try:
        # Load the Excel file and parse specified sheet
        excel_file = pd.ExcelFile(excel_path)
        df = excel_file.parse(sheet_name)

        # Convert 'Date' column to datetime
        df['Date'] = pd.to_datetime(df['Date'])

        # Initialize plot
        fig, ax1 = plt.subplots(figsize=(14, 7))

        # Plot Search Volume
        ax1.plot(df['Date'], df['Search Volume'], label='Search Volume', color='blue', linewidth=1.5)

        # Plot Mention Volume (scaled down for visibility)
        ax1.plot(df['Date'], df['Mention Volume'] / 1000, 
                label='Mention Volume (x1000)', color='green', linewidth=1.5)

        # Configure primary axis
        ax1.set_xlabel("Date", fontsize=12)
        ax1.set_ylabel("Search/Mention Volume", fontsize=12)
        ax1.tick_params(axis='y', labelsize=10)
        ax1.grid(True, alpha=0.3)

        # Highlight campaign events
        campaigns = df['Campaign/Advertisement'].dropna().unique()
        colors = ['#ADD8E6', '#90EE90', '#FFB6C1', '#FAFAD2', '#FFA07A']  # Standard matplotlib colors
        
        for i, campaign in enumerate(campaigns):
            event_dates = df[df['Campaign/Advertisement'] == campaign]['Date']
            if not event_dates.empty:
                start_date = event_dates.min()
                end_date = event_dates.max()
                ax1.axvspan(start_date, end_date, 
                           color=colors[i % len(colors)], 
                           alpha=0.3, 
                           label=campaign)

        # Configure sentiment axis
        ax2 = ax1.twinx()
        ax2.plot(df['Date'], df['Sentiment'], 
                label='Sentiment', color='orange', linewidth=1.2)
        ax2.set_ylabel("Sentiment", color='orange', fontsize=12)
        ax2.tick_params(axis='y', labelcolor='orange', labelsize=10)
        ax2.set_ylim(0.5, 1.0)  # Standard sentiment range

        # Format date axis
        ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
        fig.autofmt_xdate(rotation=45)

        # Combine legends
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, 
                  loc='upper left', 
                  bbox_to_anchor=(0.01, 0.99),
                  fontsize=10)

        # Add title
        plt.title("Campaign Timeline vs. Search/Social Metrics", 
                 fontsize=16, 
                 fontweight='bold', 
                 pad=20)

        # Save to buffer
        buf = BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', dpi=150)
        plt.close()
        buf.seek(0)
        return buf.getvalue()

    except Exception as e:
        print(f"Error generating campaign timeline chart: {e}")
        return b""