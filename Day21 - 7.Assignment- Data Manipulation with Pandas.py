'''
Assignment 7: Data Manipulation with Pandas

Problem Statement:
You are given a DataFrame containing information about students' exam scores.
Perform the following tasks using pandas:

Load the given CSV file into a pandas DataFrame.
Display the last 3 rows of the DataFrame.
Add a new column named 'Total' that contains the total score of each student (sum of Math, Science, and English scores).
Sort the DataFrame based on the 'Total' column in descending order.
Reset the index of the DataFrame.
'''

import pandas as pd

# Load the CSV file into a pandas DataFrame
student_scores = pd.read_csv('student_scores.csv')

# Display the last 3 rows of the DataFrame
print("Last 3 rows of the DataFrame:")
print(student_scores.tail(3))

# Add a new column 'Total'
student_scores['Total'] = student_scores[['Math', 'Science', 'English']].sum(axis=1)

# Sort the DataFrame based on the 'Total' column in descending order
student_scores.sort_values(by='Total', ascending=False, inplace=True)

# Reset the index of the DataFrame
student_scores.reset_index(drop=True, inplace=True)

# Display the DataFrame after modifications
print("\nDataFrame after modifications:")
print(student_scores)
