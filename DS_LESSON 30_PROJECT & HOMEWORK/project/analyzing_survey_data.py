import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('survey_data.csv')

# Data Exploration
print("Dataset Summary:\n", data.info())
print("Summary Statistics:\n", data.describe())

# Organize Data: Calculate Frequency of Preferred Products
preferred_product_counts = data['Preferred Product'].value_counts()

# Visualize Preferred Products
plt.figure(figsize=(8, 6))
plt.bar(preferred_product_counts.index, preferred_product_counts.values, color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Preferred Products')
plt.xlabel('Product')
plt.ylabel('Number of Students')
plt.show()

# Analyze Buying Frequency
buying_frequency_mean = data.groupby('Preferred Product')['Buying Frequency'].mean()

# Visualize Buying Frequency
plt.figure(figsize=(8, 6))
buying_frequency_mean.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Average Buying Frequency per Product')
plt.xlabel('Product')
plt.ylabel('Average Buying Frequency')
plt.show()

# Output
print("Preferred Products:\n", preferred_product_counts)
print("\nAverage Buying Frequency per Product:\n", buying_frequency_mean)
