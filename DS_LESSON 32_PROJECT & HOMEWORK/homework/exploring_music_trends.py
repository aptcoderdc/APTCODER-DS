import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('music_trends.csv')

# Data Exploration
print("Dataset Summary:\n", data.info())
print("Summary Statistics:\n", data.describe())

# Organize Data: Calculate Frequency of Genres
genre_counts = data['Genre'].value_counts()

# Visualize Most Popular Songs Over the Years
plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Most Popular Song'], marker='o', linestyle='-')
plt.title('Most Popular Songs Over the Years')
plt.xlabel('Year')
plt.ylabel('Song')
plt.xticks(data['Year'])
plt.grid(True)
plt.show()

# Visualize Most Popular Genres
plt.figure(figsize=(10, 6))
plt.bar(genre_counts.index, genre_counts.values, color='salmon')
plt.title('Most Popular Genres')
plt.xlabel('Genre')
plt.ylabel('Frequency')
plt.show()

# Output
print("Most Popular Genres:\n", genre_counts)
