import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI rendering

def get_conversion_funnel_chart_improved() -> bytes:
    """
    Generate an improved and more readable Haldiram's website conversion funnel as a PNG image.
    Returns:
        bytes: PNG image data of the improved funnel chart
    """
    # Data for the funnel
    stages = ['Homepage', 'Category', 'Product', 'Checkout']
    percentages = ['-40%', '-60%', '-30%', '-30%']
    labels_red = ['PRODUCT\nDISCOVERY', 'CART', 'CHECK', '']

    # Coordinates for the funnel sections
    coords = [
        [(0, 1), (1, 1), (0.8, 0.75), (0.2, 0.75)],
        [(0.2, 0.75), (0.8, 0.75), (0.7, 0.5), (0.3, 0.5)],
        [(0.3, 0.5), (0.7, 0.5), (0.6, 0.25), (0.4, 0.25)],
        [(0.4, 0.25), (0.6, 0.25), (0.5, 0), (0.5, 0)]
    ]

    fig, ax = plt.subplots(figsize=(8, 8))  # Larger figure for better spacing

    # Define a color gradient for the funnel sections
    colors = ['#4A90E2', '#357ABD', '#2A5D8F', '#1F3B5A']

    # Draw funnel sections with gradient colors and edge
    for i, coord in enumerate(coords):
        polygon = Polygon(coord, closed=True, facecolor=colors[i], edgecolor='black', linewidth=1.5)
        ax.add_patch(polygon)

    # Add stage labels with improved font size and weight
    for i, stage in enumerate(stages):
        y = (coords[i][0][1] + coords[i][2][1]) / 2
        ax.text(-0.15, y, stage, fontsize=16, fontweight='bold', va='center', ha='right', color='#333333')

    # Add red text labels with better font size and alignment
    for i, label in enumerate(labels_red):
        if label:
            y = (coords[i][0][1] + coords[i][2][1]) / 2
            ax.text(0.85, y, label, fontsize=12, color='#D9534F', fontweight='bold', va='center', ha='left')

    # Add percentages with larger font and bold style
    for i, perc in enumerate(percentages):
        y = (coords[i][0][1] + coords[i][2][1]) / 2
        ax.text(0.95, y, perc, fontsize=16, color='#D9534F', fontweight='bold', va='center', ha='left')

    # Add title with improved font size and color
    ax.text(0.5, 1.08, "Haldiram's Website Conversion Funnel", fontsize=20, fontweight='bold', ha='center', color='#222222')

    # Add subtle grid lines for horizontal reference
    ax.hlines([0.875, 0.625, 0.375, 0.125], xmin=-0.3, xmax=1.1, colors='#CCCCCC', linestyles='dashed', linewidth=0.8)

    # Remove axes
    ax.axis('off')

    # Set limits for better spacing
    ax.set_xlim(-0.3, 1.1)
    ax.set_ylim(0, 1.1)

    # Save to BytesIO buffer
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=150)
    plt.close()
    buf.seek(0)
    return buf.getvalue()