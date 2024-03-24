'''
Assignment 1: Data Preprocessing and Manipulation with Pandas

Problem Statement:
You are provided with a DataFrame containing information about daily weather conditions. Perform the following tasks:

Load the provided DataFrame into pandas.
Display the first 10 rows of the DataFrame.
Check for missing values and handle them appropriately.
Convert the 'Date' column to datetime format.
Calculate the average temperature for each month.
Identify the day with the highest temperature.
Visualize the trend of temperature over time using a line plot.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Provided DataFrame with daily weather conditions
data = {'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
        'Temperature': [20, 22, 21, None, 25],
        'Humidity': [50, 55, 60, 65, 70],
        'Wind_Speed': [10, 12, None, 14, 15]}

# Create DataFrame
weather_data = pd.DataFrame(data)

# Display the first 10 rows of the DataFrame
print("First 10 rows of the DataFrame:")
print(weather_data.head(10))

# Check for missing values and handle them appropriately
print("\nMissing values before handling:")
print(weather_data.isnull().sum())

# Fill missing values with the mean of the respective column, excluding the 'Date' column
weather_data.fillna(weather_data.drop(columns=['Date']).mean(), inplace=True)

# Convert the 'Date' column to datetime format
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

# Calculate the average temperature for each month
weather_data['Month'] = weather_data['Date'].dt.month
monthly_average_temperature = weather_data.groupby('Month')['Temperature'].mean()
print("\nAverage temperature for each month:")
print(monthly_average_temperature)

# Identify the day with the highest temperature
highest_temperature_day = weather_data.loc[weather_data['Temperature'].idxmax(), 'Date']
print("\nDay with the highest temperature:", highest_temperature_day)

# Visualize the trend of temperature over time using a line plot
plt.plot(weather_data['Date'], weather_data['Temperature'], marker='o')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature Trend Over Time')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
