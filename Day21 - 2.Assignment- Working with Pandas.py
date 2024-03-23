'''
Perform the following tasks:
Display the first 10 rows of the DataFrame.
Display summary statistics for numerical columns.
Check for missing values in the dataset and handle them appropriately.
Convert the 'Date' column to a datetime format.
Extract the month and year from the 'Date' column and add them as new columns.
Calculate the total sales amount for each month.
Calculate the average sales amount for each product category.
Find the top selling products.
'''


import pandas as pd
import numpy as np


# Create a synthetic dataset
np.random.seed(0)
dates = pd.date_range(start='2022-01-01', end='2022-03-31', freq='D')
products = ['Product A', 'Product B', 'Product C']
categories = ['Category 1', 'Category 2', 'Category 3']
prices = np.random.randint(10, 100, size=len(dates))
quantities = np.random.randint(1, 10, size=len(dates))

data = {
    'Date': dates,
    'Product': np.random.choice(products, len(dates)),
    'Category': np.random.choice(categories, len(dates)),
    'Price': prices,
    'Quantity': quantities
}

# Load the dataset into a Pandas DataFrame
df = pd.DataFrame(data)

# Display the first 10 rows of the DataFrame
print("First 10 rows:")
print(df.head(10))

# Display summary statistics for numerical columns
print("\nSummary statistics:")
print(df.describe())

# Check for missing values in the dataset and handle them appropriately
print("\nMissing values:")
print(df.isnull().sum())

# Convert the 'Date' column to a datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract the month and year from the 'Date' column and add them as new columns
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Calculate the total sales amount for each month
monthly_sales = df.groupby(['Year', 'Month'])['Price'].sum()
print("\nTotal sales amount for each month:")
print(monthly_sales)

# Calculate the average sales amount for each product category
category_avg_sales = df.groupby('Category')['Price'].mean()
print("\nAverage sales amount for each product category:")
print(category_avg_sales)

# Find the top selling products
top_selling_products = df.groupby('Product')['Quantity'].sum().nlargest(5)
print("\nTop selling products:")
print(top_selling_products)


