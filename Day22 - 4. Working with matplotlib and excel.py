'''
Assignment 2: Data Analysis and Visualization with Pandas

Problem Statement:
You are given a dictionary containing information about employees' salaries and years of experience. Perform the following tasks using pandas:

Create a DataFrame from the given dictionary.
Display the first 5 rows of the DataFrame.
Calculate the average salary.
Identify the employee(s) with the highest salary.
Visualize the distribution of years of experience using a histogram.
'''
import pandas as pd
import matplotlib.pyplot as plt

# Given dictionary of employee salaries and years of experience
employee_data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salary': [60000, 75000, 80000, 90000, 85000],
    'Experience_Years': [3, 5, 7, 4, 6]
}

# Create DataFrame from the dictionary
employee_df = pd.DataFrame(employee_data)

# Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(employee_df.head())

# Calculate the average salary
average_salary = employee_df['Salary'].mean()
print("\nAverage salary:", average_salary)

# Identify the employee(s) with the highest salary
highest_salary_employee = employee_df.loc[employee_df['Salary'].idxmax(), 'Name']
print("\nEmployee(s) with the highest salary:", highest_salary_employee)

# Visualize the distribution of years of experience using a histogram
plt.hist(employee_df['Experience_Years'], bins=range(min(employee_df['Experience_Years']), max(employee_df['Experience_Years']) + 1, 1), edgecolor='black')
plt.xlabel('Years of Experience')
plt.ylabel('Frequency')
plt.title('Distribution of Years of Experience')
plt.show()
