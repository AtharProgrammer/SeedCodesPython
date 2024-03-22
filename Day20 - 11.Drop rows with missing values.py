# importing pandas module
import pandas as pd

# making data frame from csv file
data = pd.read_csv("data.csv")

# making new data frame with dropped NA values
data.dropna()  # Drop rows with missing values
print(data)
new_data = data.dropna(axis=0, how='any')

# comparing sizes of data frames
print("Old data frame length:", len(data),
	"\nNew data frame length:",
	len(new_data), 
	"\nNumber of rows with at least 1 NA value: ",
	(len(data)-len(new_data)))
print(new_data)
