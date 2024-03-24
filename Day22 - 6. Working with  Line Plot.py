'''
1. Line Plot:
Case Study: Analyzing Daily Sales

Objective: Analyze the trend of daily sales over a month.

Example:
We have daily sales data for a retail store for the month of January.
We want to visualize the trend of daily sales to identify any patterns or
trends.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Example data
date_range = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
daily_sales = pd.Series([1000, 1200, 1100, 1300, 1400, 1500, 1600, 1800, 2000, 1900, 
                         2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000,
                         3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4200],
                        index=date_range[:-1])  # Remove the last day to match the length of values

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(daily_sales.index, daily_sales.values, marker='o')
plt.title('Daily Sales Trend (January 2024)')
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

#This code creates a line plot showing the trend of daily sales over the month of January.
