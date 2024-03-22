import pandas as pd
# Create a DataFrame from a dictionary
data = pd.read_csv('data.csv')

df = pd.DataFrame(data)

#Filtering rows based on a condition
print(df[df['Age'] > 30])




