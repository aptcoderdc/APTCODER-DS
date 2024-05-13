import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('telemetry_data.csv')

# Data Cleaning (if necessary)

# Data Analysis
num_players = len(data)
avg_playtime = data['Playtime'].mean()

# Visualize Game Telemetry
plt.figure(figsize=(8, 5))

# Boxplot of Playtime
plt.boxplot(data['Playtime'], vert=False)
plt.title('Playtime Distribution')
plt.xlabel('Playtime (minutes)')

plt.show()

# Output
print("Number of Players:", num_players)
print("Average Playtime:", avg_playtime)
