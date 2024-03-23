'''
Assignment 2: Data Cleaning and Preprocessing with Pandas

Problem Statement:
You have been provided with a dataset containing information about
students' exam scores. However, the dataset is messy and requires cleaning.
Perform the following tasks using pandas:

Load the dataset into a pandas DataFrame.
Check for missing values and handle them appropriately.
Remove any duplicate rows from the DataFrame.
Convert the 'DOB' column to datetime format.
Calculate the average score for each subject.

'''

import pandas as pd
import numpy as np

# Sample data for student scores
data = {'Student_ID': [101, 102, 103, 104, 105,101],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve','ramesh'],
        'DOB': ['1999-05-15', '2000-02-28', '1998-11-10', '2001-07-20', '1997-09-05','1997-09-05'],
        'Math': [85, np.nan, 70, 90, 75,55],
        'Science': [78, 88, 92, np.nan, 85,66],
        'English': [82, 79, 85, 88, np.nan,77]}

# Create DataFrame
student_scores = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(student_scores)

# Check for missing values and handle them appropriately
print("\nMissing values before handling:")
print(student_scores.isnull().sum())
print(student_scores)

# Fill missing values with the mean of the respective column
student_scores.fillna(student_scores.mean(numeric_only=True), inplace=True)
print("Fill missing values with the mean of the respective column")
print(student_scores)

# Remove duplicate rows based on 'Student_ID'
student_scores.drop_duplicates(subset='Student_ID', inplace=True)
print("Remove duplicate rows based on 'Student_ID'")
print(student_scores)

# Convert the 'DOB' column to datetime format
student_scores['DOB'] = pd.to_datetime(student_scores['DOB'])

# Calculate the average score for each subject
average_scores = student_scores[['Math', 'Science', 'English']].mean()
print("\nAverage score for each subject:")
print(average_scores)
