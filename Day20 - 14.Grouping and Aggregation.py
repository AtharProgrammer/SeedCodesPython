import pandas as pd
# Sample data for student names and ages

students_data = {
    'Name': ["Alice", "Bob", "Charlie", "David", "Alice", "Eva", "Bob"],
    'Age': [20, 22, 21, 23, 20, 19, 22],
    'Grade': [85, 90, 78, 92, 85, 88, 90],
    'Attendance': [95, 92, 88, 93, 95, 96, 92],
    'Gender':["male","female","male","male","female","male","female"]
}

# Create a DataFrame
students_df = pd.DataFrame(students_data)

# Grouping data by a column and calculating aggregate statistics
grouped_data = students_df.groupby('Gender').agg({'Age': ['mean', 'median', 'min', 'max']})
print(grouped_data)

