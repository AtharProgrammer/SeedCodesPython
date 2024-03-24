'''
Assignment 1: Analyzing Student Scores
Problem Statement:
You are given a CSV file student_scores.csv containing student names and
their corresponding scores in different subjects. Perform the following tasks:

Load the data into a pandas DataFrame.
Display the first 5 rows of the DataFrame.
Calculate and display the mean, median, and standard deviation of scores
for each subject.
Visualize the distribution of scores for each subject using a histogram.
Save the histogram plots as PNG files.
'''
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data into a pandas DataFrame
student_scores = pd.read_csv('student_scores.csv')

# 2. Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(student_scores.head())

# 3. Calculate and display the mean, median, and standard deviation of scores for each subject
print("\nStatistics for each subject:")
print(student_scores.describe())

# 4. Visualize the distribution of scores for each subject using a histogram
plt.figure(figsize=(10, 6))
plt.hist(student_scores['Math'], bins=10, alpha=0.5, label='Math')
plt.hist(student_scores['Science'], bins=10, alpha=0.5, label='Science')
plt.hist(student_scores['English'], bins=10, alpha=0.5, label='English')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Distribution of Student Scores')
plt.legend()
plt.grid(True)

# 5. Save the histogram plots as PNG files
plt.savefig('score_distribution.png')

plt.show()
