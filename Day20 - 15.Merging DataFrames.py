import pandas as pd
# Creating two DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 35]})

# Merging DataFrames based on a common column
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)
