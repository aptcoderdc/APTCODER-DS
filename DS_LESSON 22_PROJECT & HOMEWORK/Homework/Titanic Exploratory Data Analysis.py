# Importing necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Display the first few rows of the dataset to understand its structure
print(titanic.head())

# Get the summary statistics of the dataset
print(titanic.describe())

# Check for missing values
print(titanic.isnull().sum())

# Visualize the distribution of each numeric feature using histograms
numeric_cols = titanic.select_dtypes(include=np.number)
numeric_cols.hist(figsize=(10, 8))
plt.show()

# Visualize the relationship between features and survival using bar plots
plt.figure(figsize=(10, 8))
sns.barplot(x='sex', y='survived', data=titanic, ci=None)
plt.title('Survival by Gender')
plt.show()

plt.figure(figsize=(10, 8))
sns.barplot(x='class', y='survived', data=titanic, ci=None)
plt.title('Survival by Passenger Class')
plt.show()

plt.figure(figsize=(10, 8))
sns.barplot(x='alone', y='survived', data=titanic, ci=None)
plt.title('Survival for Passengers Traveling Alone or with Family')
plt.show()

# Visualize the relationship between age and survival using a boxplot
plt.figure(figsize=(10, 8))
sns.boxplot(x='survived', y='age', data=titanic)
plt.title('Age Distribution by Survival')
plt.show()

# Explore survival rates by combining multiple variables
plt.figure(figsize=(10, 8))
sns.pointplot(x='class', y='survived', hue='sex', data=titanic, markers=['o', 'x'], linestyles=['-', '--'])
plt.title('Survival by Passenger Class and Gender')
plt.show()

# Explore survival rates by age and gender
plt.figure(figsize=(10, 8))
sns.violinplot(x='sex', y='age', hue='survived', data=titanic, split=True)
plt.title('Survival by Age and Gender')
plt.show()
