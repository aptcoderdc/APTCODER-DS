import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('monthly_rainfall.csv')

# Convert 'Month' to datetime format
data['Month'] = pd.to_datetime(data['Month'], format='%b-%Y')

# Set 'Month' as the index
data.set_index('Month', inplace=True)

# Plot the time series data
plt.figure(figsize=(10, 5))
plt.plot(data, marker='o', linestyle='-', color='g')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()

# Calculate basic statistics
mean_rainfall = data['Rainfall'].mean()
median_rainfall = data['Rainfall'].median()

print("Mean Rainfall:", mean_rainfall)
print("Median Rainfall:", median_rainfall)

# Identify seasons
data['Season'] = data.index.month % 12 // 3 + 1
seasonal_mean = data.groupby('Season')['Rainfall'].mean()
seasonal_mean.index = ['Winter', 'Spring', 'Summer', 'Fall']

print("\nSeasonal Mean Rainfall:")
print(seasonal_mean)
