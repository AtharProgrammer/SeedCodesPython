'''
Perform the following tasks:
Display the first 5 rows of the DataFrame.
Display the last 3 rows of the DataFrame.
Check the data types of each column.
Find the total number of students in the dataset.
Calculate the average age of the students.
Find the maximum and minimum age of the students.
Count the number of students belonging to each gender category.
Calculate the average grade of the students.
Create a new DataFrame containing only the students with grades above 80.
'''

import pandas as pd

# Sample dataset
data = {
    'Name': ['John', 'Emma', 'Michael', 'Sophia', 'William', 'Olivia'],
    'Age': [20, 21, 19, 22, 20, 21],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Grade': [85, 90, 75, 88, 92, 80]
}

# Load the dataset into a Pandas DataFrame
df = pd.DataFrame(data)

# Display the first 5 rows of the DataFrame
print("First 5 rows:")
print(df.head())

# Display the last 3 rows of the DataFrame
print("\nLast 3 rows:")
print(df.tail(3))

# Check the data types of each column
print("\nData types:")
print(df.dtypes)

# Find the total number of students in the dataset
total_students = len(df)
print("\nTotal number of students:", total_students)

# Calculate the average age of the students
average_age = df['Age'].mean()
print("\nAverage age of the students:", average_age)

# Find the maximum and minimum age of the students
max_age = df['Age'].max()
min_age = df['Age'].min()
print("\nMaximum age of the students:", max_age)
print("Minimum age of the students:", min_age)

# Count the number of students belonging to each gender category
gender_counts = df['Gender'].value_counts()
print("\nNumber of students belonging to each gender category:")
print(gender_counts)

# Calculate the average grade of the students
average_grade = df['Grade'].mean()
print("\nAverage grade of the students:", average_grade)

# Create a new DataFrame containing only the students with grades above 80
high_grade_students = df[df['Grade'] > 80]
print("\nStudents with grades above 80:")
print(high_grade_students)
