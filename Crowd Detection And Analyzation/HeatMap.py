#python HeatMap.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation as animation
import csv

# Read data from CSV file into a DataFrame
df = pd.read_csv("data.csv")

# Define a function to update the heatmap
def update_heatmap(frame):
    plt.clf()  # Clear the previous plot
    # Process data for the current frame (assuming the data is already sorted by time)
    data = df.iloc[:frame + 1]  # Use data up to the current frame
    pivot_data = data.pivot(index='No.of People', columns='Time', values='value')
    ax = sns.heatmap(pivot_data, cbar_kws={'ticks': range(1, 21)}, vmin=0, vmax=20, cmap="PuBu", linecolor='red', linewidths=1)
    plt.title(f"Time: {data.iloc[-1]['Time']}")
    plt.pause(0.1)  # Pause to display the plot (adjust as needed)

# Create an animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update_heatmap, frames=len(df), interval=200, repeat=False)

plt.show()
