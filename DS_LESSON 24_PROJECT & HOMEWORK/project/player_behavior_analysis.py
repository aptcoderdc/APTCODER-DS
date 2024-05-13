import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('player_data.csv')

# Data Exploration
print("Dataset Summary:\n", data.info())
print("Summary Statistics:\n", data.describe())

# Visualize Player Behavior
plt.figure(figsize=(10, 6))

# Histogram of Playtime
plt.subplot(2, 2, 1)
plt.hist(data['Playtime'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Playtime')
plt.xlabel('Playtime (minutes)')
plt.ylabel('Frequency')

# Bar Chart of Levels Completed
plt.subplot(2, 2, 2)
level_counts = data['Levels Completed'].value_counts().sort_index()
plt.bar(level_counts.index, level_counts.values, color='lightgreen')
plt.title('Levels Completed')
plt.xlabel('Levels')
plt.ylabel('Number of Players')

# Pie Chart of Preferred Characters
plt.subplot(2, 2, 3)
character_counts = data['Preferred Character'].value_counts()
plt.pie(character_counts, labels=character_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Preferred Characters')

plt.tight_layout()
plt.show()
