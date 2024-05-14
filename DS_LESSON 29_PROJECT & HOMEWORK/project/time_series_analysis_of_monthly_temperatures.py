import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('monthly_temperatures.csv')

# Convert 'Month' to datetime format
data['Month'] = pd.to_datetime(data['Month'], format='%b-%Y')

# Set 'Month' as the index
data.set_index('Month', inplace=True)

# Plot the time series data
plt.figure(figsize=(10, 5))
plt.plot(data, marker='o', linestyle='-', color='b')
plt.title('Monthly Temperatures')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# Calculate basic statistics
mean_temp = data['Temperature'].mean()
median_temp = data['Temperature'].median()

print("Mean Temperature:", mean_temp)
print("Median Temperature:", median_temp)

# Identify seasons
data['Season'] = data.index.month % 12 // 3 + 1
seasonal_mean = data.groupby('Season')['Temperature'].mean()
seasonal_mean.index = ['Winter', 'Spring', 'Summer', 'Fall']

print("\nSeasonal Mean Temperatures:")
print(seasonal_mean)
