'''
Assignment 2: Sales Analysis
Problem Statement:
You are provided with sales data in a CSV file sales_data.csv,
containing information about sales transactions. Perform the following tasks:

Load the data into a pandas DataFrame.
Display the total sales amount for each month.
Visualize the trend of total sales over time using a line plot.
Calculate and display the average sales amount for each product category.
Visualize the average sales amount for each product category using a bar plot.
'''
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'Amount': [1000, 1200, 1100, 1300, 1400],
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Grocery', 'Electronics']
}

# Create DataFrame
sales_data = pd.DataFrame(data)

# 2. Display the total sales amount for each month
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
monthly_sales = sales_data.resample('M', on='Date')['Amount'].sum()
print("Total sales amount for each month:")
print(monthly_sales)

# 3. Visualize the trend of total sales over time using a line plot
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.title('Trend of Total Sales Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 4. Calculate and display the average sales amount for each product category
average_sales_by_category = sales_data.groupby('Category')['Amount'].mean()
print("\nAverage sales amount for each product category:")
print(average_sales_by_category)

# 5. Visualize the average sales amount for each product category using a bar plot
plt.figure(figsize=(8, 6))
average_sales_by_category.plot(kind='bar')
plt.xlabel('Product Category')
plt.ylabel('Average Sales Amount')
plt.title('Average Sales Amount by Product Category')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
