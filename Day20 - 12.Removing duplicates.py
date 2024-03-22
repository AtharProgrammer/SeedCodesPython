import pandas as pd
# Sample data for student names and ages

students_data = {
    'Name': ["Alice", "Bob", "Charlie", "David", "Alice", "Eva", "Bob"],
    'Age': [20, 22, 21, 23, 20, 19, 22],
    'Grade': [85, 90, 78, 92, 85, 88, 90],
    'Attendance': [95, 92, 88, 93, 95, 96, 92]
}

# Create a DataFrame
students_df = pd.DataFrame(students_data)
print(students_df)

# Remove all duplicate rows
students_df_no_duplicates = students_df.drop_duplicates(keep=False)
print(students_df_no_duplicates)

# Delete duplicate rows based on specific columns (Name and Age)
students_df_specific_columns = students_df.drop_duplicates(subset=["Name", "Age"], keep=False)
print(students_df_specific_columns)
