import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend

def get_crisis_sentiment_trends_chart() -> bytes:
    # Data for each crisis event
    weeks_2022 = [0, 2, 4, 6, 8, 10, 12]
    sentiment_2022 = [100, 45, 60, 75, 85, 92, 95]

    weeks_2015 = [0, 2, 4, 8, 12, 16, 20]
    sentiment_2015 = [100, 80, 70, 65, 75, 80, 100]

    weeks_2018 = [0, 2, 4, 8, 12, 20, 25, 30, 35, 40]
    sentiment_2018 = [100, 80, 40, 35, 30, 50, 60, 65, 70, 75]

    weeks_2023 = [0, 2, 4, 6, 8]
    sentiment_2023 = [100, 80, 90, 95, 100]

    # Create the plot
    plt.figure(figsize=(10, 6))

    plt.plot(weeks_2022, sentiment_2022, marker='o', color='#13A5C6', label='2022 Viral Hygiene Incident')
    plt.plot(weeks_2015, sentiment_2015, marker='o', color='#F9C97B', label='2015 Export Safety Ban')
    plt.plot(weeks_2018, sentiment_2018, marker='o', color='#A33C32', label='2018 Contamination Lawsuit')
    plt.plot(weeks_2023, sentiment_2023, marker='o', color='#F6F6D9', label='2023 Packaging Foreign Object')

    plt.xlabel('Weeks Since Crisis Onset')
    plt.ylabel('Sentiment/Search Volume (%)')
    plt.title('Sentiment/Search Volume Trends After Crisis Events')
    plt.legend()
    plt.ylim(20, 110)
    plt.xlim(0, 40)
    plt.grid(False)

    plt.tight_layout()

    # Save to BytesIO buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf.getvalue()