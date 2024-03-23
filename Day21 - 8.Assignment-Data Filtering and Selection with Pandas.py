'''
Assignment 4: Data Filtering and Selection with Pandas

Problem Statement:
You are given a DataFrame containing information about sales data. Perform the following tasks using pandas:

Load the given CSV file into a pandas DataFrame.
Filter the DataFrame to include only rows where the sales amount is greater than $500.
Select and display only the 'Date' and 'Sales' columns for the filtered DataFrame.
Find the average sales amount for each year.
'''

import pandas as pd


# Load the CSV file into a pandas DataFrame
sales_data = pd.read_csv('sales_data.csv')

# Filter the DataFrame to include only rows where the sales amount is greater than 500
filtered_sales_data = sales_data[sales_data['Sales'] > 500]
print("Filter the DataFrame to include only rows where the sales amount is greater than 500")
print(filtered_sales_data)
# Select and display only the 'Date' and 'Sales' columns for the filtered DataFrame
filtered_sales_data = filtered_sales_data[['Date', 'Sales']]
print("Select and display only the 'Date' and 'Sales' columns for the filtered DataFrame")
print(filtered_sales_data)

# Convert 'Date' column to datetime format
filtered_sales_data['Date'] = pd.to_datetime(filtered_sales_data['Date'])

# Extract year from the 'Date' column
filtered_sales_data['Year'] = filtered_sales_data['Date'].dt.year

# Find the average sales amount for each year
average_sales_per_year = filtered_sales_data.groupby('Year')['Sales'].mean()
print("Find the average sales amount for each year")
print(average_sales_per_year)
