'''
2. Scatter Plot:
Case Study: Relationship Between Advertising Expenditure and Sales

Objective: Investigate the relationship between advertising expenditure
and sales.

Example:
We have data on daily advertising expenditure (in dollars) and
daily sales (in units) for a retail store.
We want to visualize the relationship between advertising
expenditure and sales to see if there's any correlation.

'''
import pandas as pd
import matplotlib.pyplot as plt

# Example data
advertising_expenditure = [100, 200, 300, 400, 500]
daily_sales = [50, 100, 150, 200, 250]

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(advertising_expenditure, daily_sales)
plt.title('Relationship Between Advertising Expenditure and Sales')
plt.xlabel('Advertising Expenditure ($)')
plt.ylabel('Daily Sales (units)')
plt.grid(True)
plt.tight_layout()
plt.show()
