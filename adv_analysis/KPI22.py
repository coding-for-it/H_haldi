import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI rendering

def get_category_pie_chart() -> bytes:
    """
    Generate a pie chart for different categories and return as PNG bytes.
    
    Returns:
        bytes: PNG image data of the pie chart
    """
    labels = [
        'Complaint', 'Purchase Decision', 'Comparison', 'Praise', 'News Reporting',
        'Consumption Moment', 'Praise/Consumption', 'Comparison/Complaint',
        'Complaint/Comparison', 'Suggestion/Complaint', 'Complaint/Suggestion'
    ]
    sizes = [31.1, 14.8, 13.1, 11.5, 9.8, 8.2, 3.3, 3.3, 1.6, 1.6, 1.6]
    colors = [
        'lightblue', 'blue', 'lightgreen', 'green', 'lightpink', 'red',
        'orange', 'darkorange', 'purple', 'violet', 'yellow'
    ]

    plt.figure(figsize=(8, 8))
    plt.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=140
    )
    plt.axis('equal')
    plt.title('Pie Chart of Different Categories')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf.getvalue()