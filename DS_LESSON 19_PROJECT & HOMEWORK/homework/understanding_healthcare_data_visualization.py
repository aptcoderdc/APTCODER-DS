import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('patient_records.csv')

# Data Exploration
print("Dataset Summary:\n", data.info())
print("Summary Statistics:\n", data.describe())

# Data Visualization
plt.figure(figsize=(10, 6))

# Distribution of Age
plt.subplot(2, 2, 1)
plt.hist(data['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Distribution of Blood Pressure
plt.subplot(2, 2, 2)
plt.hist(data['Blood Pressure'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribution of Blood Pressure')
plt.xlabel('Blood Pressure')
plt.ylabel('Frequency')

# Distribution of Cholesterol Level
plt.subplot(2, 2, 3)
plt.hist(data['Cholesterol Level'], bins=20, color='salmon', edgecolor='black')
plt.title('Distribution of Cholesterol Level')
plt.xlabel('Cholesterol Level')
plt.ylabel('Frequency')

# Disease Status
plt.subplot(2, 2, 4)
plt.pie(data['Disease Status'].value_counts(), labels=data['Disease Status'].value_counts().index, autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])
plt.title('Distribution of Disease Status')

plt.tight_layout()
plt.show()
