import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('music_preferences.csv')

# Data Exploration
print("Dataset Summary:\n", data.info())
print("Summary Statistics:\n", data.describe())

# Organize Data: Calculate Frequency of Favorite Songs
favorite_song_counts = data['Favorite Song'].value_counts()

# Visualize Favorite Songs
plt.figure(figsize=(10, 6))
plt.bar(favorite_song_counts.index, favorite_song_counts.values, color='skyblue')
plt.title('Favorite Songs')
plt.xlabel('Song')
plt.ylabel('Number of Students')
plt.show()

# Organize Data: Calculate Frequency of Favorite Artists
favorite_artist_counts = data['Favorite Artist'].value_counts()

# Visualize Favorite Artists
plt.figure(figsize=(10, 6))
plt.bar(favorite_artist_counts.index, favorite_artist_counts.values, color='lightgreen')
plt.title('Favorite Artists')
plt.xlabel('Artist')
plt.ylabel('Number of Students')
plt.show()

# Analyze Hours Listened per Week
hours_listened_mean = data['Hours Listened per Week'].mean()

# Output
print("Favorite Songs:\n", favorite_song_counts)
print("Favorite Artists:\n", favorite_artist_counts)
print("Average Hours Listened per Week:", hours_listened_mean)
