'''
Assignment 4: Data Manipulation and Analysis with Pandas

Problem Statement:
You are provided with a DataFrame containing information about students'
exam scores. Perform the following tasks:

Load the provided DataFrame into pandas.
Display the last 5 rows of the DataFrame.
Calculate the total number of students.
Calculate the average score for each subject.
Identify the student(s) with the highest total score.
Calculate the overall passing percentage
(assuming passing score is 60 for each subject).
Solution:
'''
import pandas as pd

# Provided DataFrame with student scores
data = {'Student_ID': [101, 102, 103, 104, 105],
        'Math': [85, 70, 90, 80, 75],
        'Science': [78, 88, 92, 85, 80],
        'English': [82, 79, 85, 88, 90]}

# Create DataFrame
student_scores = pd.DataFrame(data)

# Display the last 5 rows of the DataFrame
print("Last 5 rows of the DataFrame:")
print(student_scores.tail())

# Calculate the total number of students
total_students = student_scores.shape[0]
print("\nTotal number of students:", total_students)

# Calculate the average score for each subject
average_scores = student_scores.mean()
print("\nAverage score for each subject:")
print(average_scores)

# Identify the student(s) with the highest total score
student_scores['Total_Score'] = student_scores[['Math', 'Science', 'English']].sum(axis=1)
highest_score_student = student_scores.loc[student_scores['Total_Score'].idxmax(), 'Student_ID']
print("\nStudent(s) with the highest total score:", highest_score_student)

# Calculate the overall passing percentage
passing_percentage = ((student_scores[['Math', 'Science', 'English']] >= 60).all(axis=1).sum() / total_students) * 100
print("\nOverall passing percentage:", passing_percentage)
