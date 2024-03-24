'''
3. Histogram:
Case Study: Distribution of Customer Ages

Objective: Understand the distribution of customer
ages in the store's database.

Example:
We have data on the ages of customers who made purchases at a retail store.
We want to visualize the distribution of customer ages to identify the most
common age groups.
'''
import numpy as np
import matplotlib.pyplot as plt

# Example data
customer_ages = np.random.randint(18, 70, size=100)  # Generate random customer ages between 18 and 70

# Plotting
plt.figure(figsize=(8, 6))
plt.hist(customer_ages, bins=10, edgecolor='black', alpha=0.7)
plt.title('Distribution of Customer Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

#This code creates a histogram showing the distribution of customer ages.
