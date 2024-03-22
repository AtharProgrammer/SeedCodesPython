import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(0)

# Generating random dates
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Generating random product names
products = ['Product A', 'Product B', 'Product C']

# Generating random categories
categories = ['Electronics', 'Clothing', 'Books']

# Generating random prices between 10 and 100
prices = np.random.randint(10, 100, size=len(dates))

# Generating random quantities sold between 1 and 20
quantities = np.random.randint(1, 20, size=len(dates))

# Creating a DataFrame
data = {
    'Date': dates,
    'Product': np.random.choice(products, len(dates)),
    'Category': np.random.choice(categories, len(dates)),
    'Price': prices,
    'Quantity': quantities
}

# Load the synthetic dataset into a Pandas DataFrame
df = pd.DataFrame(data)

# Save the synthetic dataset to a CSV file
df.to_csv('sales_data_synthetic.csv', index=False)

# Display the first few rows of the synthetic dataset
print("Synthetic dataset created and saved to 'sales_data_synthetic.csv'")
print(df.head())
