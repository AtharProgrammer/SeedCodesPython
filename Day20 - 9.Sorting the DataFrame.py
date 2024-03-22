import pandas as pd
# Create a DataFrame from a dictionary
data = pd.read_csv('data.csv')

df = pd.DataFrame(data)

#Sorting the DataFrame
df.sort_values(by='Age', ascending=False, inplace=True)

print(df)


