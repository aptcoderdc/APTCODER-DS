# Importing necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset from Seaborn
iris = sns.load_dataset('iris')

# Display the first few rows of the dataset to understand its structure
print(iris.head())

# Get the summary statistics of the dataset
print(iris.describe())

# Check for missing values
print(iris.isnull().sum())

# Visualize the distribution of each feature using histograms
iris.hist(figsize=(10, 8))
plt.show()

# Visualize the relationship between features using pairplot
sns.pairplot(iris, hue='species')
plt.show()

# Visualize the correlation between features using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(iris.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Boxplot for each feature to identify outliers
plt.figure(figsize=(10, 8))
sns.boxplot(data=iris)
plt.show()

# Violin plot to visualize the distribution of features by species
plt.figure(figsize=(10, 8))
sns.violinplot(x='species', y='sepal_length', data=iris)
plt.title('Distribution of Sepal Length by Species')
plt.show()

# Swarm plot to visualize the distribution of features by species
plt.figure(figsize=(10, 8))
sns.swarmplot(x='species', y='petal_length', data=iris)
plt.title('Distribution of Petal Length by Species')
plt.show()
