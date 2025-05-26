import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI rendering

def get_value_perception_charts() -> bytes:
    """
    Generate a line chart for Net Value Perception over years and a pie chart for value perception categories.
    
    Returns:
        bytes: PNG image data of the combined chart
    """
    try:
        # Data for line chart
        years = [2023, 2024, 2025]
        net_value_perception = [0, -2, -3]

        # Data for pie chart
        labels = ['Poor Value', 'Fair Value', 'Good Value']
        sizes = [66, 17, 17]
        colors = ['#f44336', '#ffca28', '#4caf50']  # red, yellow, green

        # Create subplots: 1 row, 2 columns
        fig, axs = plt.subplots(1, 2, figsize=(16, 6), facecolor='#fafaf5')

        # Line chart
        axs[0].plot(years, net_value_perception, marker='o', color='blue')
        axs[0].set_xlabel('Year')
        axs[0].set_ylabel('Net Value Perception (Good - Poor)')
        axs[0].set_title('Net Value Perception Over Years')

        # Pie chart
        axs[1].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        axs[1].set_title('Value Perception Categories')
        axs[1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.tight_layout()

        # Save to BytesIO buffer
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        buf.seek(0)
        return buf.getvalue()
        
    except Exception as e:
        print(f"Error generating value perception charts: {e}")
        return b""