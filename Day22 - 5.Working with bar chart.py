import pandas as pd
import matplotlib.pyplot as plt

# Sample data for sales
data = {'Employee_ID': [101, 102, 103, 104, 105],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Years_Experience': [3, 5, 7, 4, 6]}

# Create DataFrame
employee_data = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(employee_data)

# Check for missing values and handle them appropriately
print("\nMissing values before handling:")
print(employee_data.isnull().sum())

# Visualize the distribution of years of experience using a bar plot
plt.bar(employee_data['Name'], employee_data['Years_Experience'])
plt.xlabel('Name')
plt.ylabel('Years of Experience')
plt.title('Distribution of Years of Experience')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
