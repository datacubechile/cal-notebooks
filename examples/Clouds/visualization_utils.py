import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd

from scipy.ndimage import gaussian_filter

def draw_ditter_plot(values, dates, figsize = (20,1), color_map = "plasma", sigma = None):
    
    if sigma is not None:
        values = gaussian_filter(values, sigma)
    
    
    # Create a colormap based on values
    norm = plt.Normalize(0, 100)
    cmap = cm.get_cmap(color_map)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize = figsize)

    # Iterate over values and dates to draw vertical lines
    for value, date in zip(values, dates):
        color = cmap(norm(value))
        ax.axvline(x=date, color=color, linewidth=2)

    # Set the colorbar for reference
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm)
    cbar.set_label('Cloud Coverage')

    # Show the plot
    plt.show()

    
def plot_cloud_stats_line_plot(values, dates):
    plt.figure(figsize = (20,5))
    plt.title("Cloud Coverage Percentage")

    smoothed_signal_1 = gaussian_filter(values, 1)
    smoothed_signal_4 = gaussian_filter(values, 4)

    plt.plot(dates,smoothed_signal_1)
    plt.plot(dates, smoothed_signal_4)    

