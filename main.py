#importing library

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# Data for climate changes
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'Temperature Anomalies (°C)': [0.85, 1.02, 0.95, 0.78, 1.10, 1.15, 0.87, 1.03, 0.90, 1.08],
    'CO2 Levels (ppm)': [410.3, 412.5, 415.1, 417.6, 419.2, 421.5, 423.7, 425.8, 428.1, 430.4],
    'Sea Level Rise (mm)': [3.2, 3.5, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.5],
    'Extreme Weather Events': [12, 15, 18, 20, 22, 25, 27, 30, 32, 35],
    'Average Global Temperature (°C)': [14.8, 14.9, 15.0, 15.1, 15.2, 15.3, 15.4, 15.5, 15.6, 15.7],
    'Arctic Sea Ice Extent (M sq km)': [6.5, 6.3, 6.1, 5.9, 5.7, 5.5, 5.3, 5.1, 4.9, 4.7],
    'Ocean Acidification (pH)': [8.1, 8.05, 8.0, 7.95, 7.9, 7.85, 7.8, 7.75, 7.7, 7.65],
    'Global Renewable Energy Production (TWh)': [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900],
    'Forest Area Loss (sq km)': [8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900],
    'Coral Reef Bleaching Events': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
}

# From a dictionary
df = pd.DataFrame(data)

# function for climate indicator

def climate_indicator(row):
    if row['Temperature Anomalies (°C)'] > 1.0 and row['CO2 Levels (ppm)'] > 420 and row['Sea Level Rise (mm)'] > 4.0:
        return 'Worse'
    elif row['Temperature Anomalies (°C)'] > 0.8 and row['CO2 Levels (ppm)'] > 415 and row['Sea Level Rise (mm)'] > 3.8:
        return 'Normal'
    else:
        return 'Good'

df['Climate Condition'] = df.apply(climate_indicator, axis=1)

# Function to plot data
def plot_data():
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Subplot 1: Temperature Anomalies
    axes[0, 0].plot(df['Year'], df['Temperature Anomalies (°C)'], marker='o', linestyle='-', color='r')
    axes[0, 0].set_title('Temperature Anomalies (°C)')
    axes[0, 0].set_xlabel('Year')
    axes[0, 0].set_ylabel('Anomaly (°C)')

    # Subplot 2: CO2 Levels
    axes[0, 1].plot(df['Year'], df['CO2 Levels (ppm)'], marker='o', linestyle='-', color='g')
    axes[0, 1].set_title('CO2 Levels (ppm)')
    axes[0, 1].set_xlabel('Year')
    axes[0, 1].set_ylabel('CO2 Levels (ppm)')

    # Subplot 3: Sea Level Rise
    axes[1, 0].plot(df['Year'], df['Sea Level Rise (mm)'], marker='o', linestyle='-', color='b')
    axes[1, 0].set_title('Sea Level Rise (mm)')
    axes[1, 0].set_xlabel('Year')
    axes[1, 0].set_ylabel('Rise (mm)')

    # Subplot 4: Arctic Sea Ice Extent
    axes[1, 1].plot(df['Year'], df['Arctic Sea Ice Extent (M sq km)'], marker='o', linestyle='-', color='c')
    axes[1, 1].set_title('Arctic Sea Ice Extent (M sq km)')
    axes[1, 1].set_xlabel('Year')
    axes[1, 1].set_ylabel('Extent (M sq km)')

    plt.tight_layout()
    return fig

# Function to display climate conditions
def display_climate_conditions():
    conditions_text = "\n".join([f"Year {row['Year']} Climate Condition: {row['Climate Condition']}" for _, row in df.iterrows()])
    climate_conditions_label.config(text=conditions_text)

# Create the main window
root = tk.Tk()
root.title("Climate Change Indicators")

# Create a frame for the plot
plot_frame = ttk.Frame(root)
plot_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a frame for the climate conditions
conditions_frame = ttk.Frame(root)
conditions_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Plot the data
fig = plot_data()
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Display the climate conditions
climate_conditions_label = ttk.Label(conditions_frame, text="", justify=tk.LEFT, anchor="w")
climate_conditions_label.pack(fill=tk.BOTH, expand=True)
display_climate_conditions()

# Run the application
root.mainloop()
