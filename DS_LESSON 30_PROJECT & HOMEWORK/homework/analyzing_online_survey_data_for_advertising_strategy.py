import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('online_survey_data.csv')

# Data Exploration
print("Dataset Summary:\n", data.info())
print("Summary Statistics:\n", data.describe())

# Organize Data: Calculate Frequency of Favorite Social Media
favorite_social_media_counts = data['Favorite Social Media'].value_counts()

# Visualize Favorite Social Media
plt.figure(figsize=(8, 6))
plt.bar(favorite_social_media_counts.index, favorite_social_media_counts.values, color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Favorite Social Media Platforms')
plt.xlabel('Social Media')
plt.ylabel('Number of Students')
plt.show()

# Analyze Daily Usage
daily_usage_mean = data.groupby('Favorite Social Media')['Daily Usage (hours)'].mean()

# Visualize Daily Usage
plt.figure(figsize=(8, 6))
daily_usage_mean.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Average Daily Usage per Social Media Platform')
plt.xlabel('Social Media')
plt.ylabel('Average Daily Usage (hours)')
plt.show()

# Output
print("Favorite Social Media Platforms:\n", favorite_social_media_counts)
print("\nAverage Daily Usage per Social Media Platform:\n", daily_usage_mean)
