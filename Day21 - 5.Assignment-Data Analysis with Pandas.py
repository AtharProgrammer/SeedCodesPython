'''
Assignment 5: Data Analysis with Pandas

Problem Statement:
You are given a CSV file containing information about sales data.
Perform the following tasks using pandas:


Display the first 5 rows of the DataFrame.
Find the total sales amount.
Find the average sales amount per month.
Identify the month with the highest sales amount.
'''

import pandas as pd

# Sample data for sales
data = {'Month': ['January', 'February', 'March', 'April', 'May'],
        'Sales': [10000, 15000, 20000, 18000, 25000]}

# Create DataFrame
sales_data = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(sales_data)

# Find the total sales amount
total_sales = sales_data['Sales'].sum()
print("\nTotal sales amount:", total_sales)

# Find the average sales amount per month
monthly_average_sales = sales_data['Sales'].mean()
print("\nAverage sales amount per month:", monthly_average_sales)

# Identify the month with the highest sales amount
highest_sales_month = sales_data.loc[sales_data['Sales'].idxmax(), 'Month']
print("\nMonth with the highest sales amount:", highest_sales_month)
