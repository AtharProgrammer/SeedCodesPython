import pandas as pd
# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)



# Accessing rows by index
print(df.iloc[0])  # First row
print(df.iloc[1:3])  # Rows 2 to 3
