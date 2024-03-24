'''
4. Bar Plot:
Case Study: Sales Performance Across Product Categories

Objective: Compare sales performance across different product categories.

Example:
We have data on the sales revenue generated by each product category
in a retail store. We want to visualize the sales performance of each
product category to identify the top-performing categories.

This code creates a bar plot showing the sales performance across different product categories.
'''
import pandas as pd
import matplotlib.pyplot as plt

# Example data
product_categories = ['Electronics', 'Clothing', 'Home Decor', 'Toys', 'Books']
sales_revenue = [50000, 60000, 45000, 55000, 70000]

# Plotting
plt.figure(figsize=(8, 6))
plt.bar(product_categories, sales_revenue, color='skyblue')
plt.title('Sales Performance Across Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Sales Revenue ($)')
plt.grid(axis='y')
plt.tight_layout()
plt.show()