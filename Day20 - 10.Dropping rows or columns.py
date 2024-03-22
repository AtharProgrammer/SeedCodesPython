import pandas as pd
# Create a DataFrame from a dictionary
data = pd.read_csv('data.csv')

df = pd.DataFrame(data)

print("Before removing column")
print(df)
# Dropping rows or columns
df.drop(columns=['City'], inplace=True)
print("after removing column")
print(df)


