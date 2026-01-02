import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # 1. Read data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # 3. Line of best fit (all data)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2051)
    sea_level_pred = res.intercept + res.slope * years_extended
    ax.plot(years_extended, sea_level_pred, color='red')

    # 4. Line of best fit (year 2000 onwards)
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000_extended = np.arange(2000, 2051)
    sea_level_2000_pred = res_2000.intercept + res_2000.slope * years_2000_extended
    ax.plot(years_2000_extended, sea_level_2000_pred, color='green')

    # 5. Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Do not modify the next two lines
    fig.savefig('sea_level_plot.png')
    return fig
