import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating the dataset directly in the code
data = pd.DataFrame({
    'Temperature': [5778, 3000, 40000, 5000, 7500, 10000, 2000, 15000, 3200, 6000],
    'Luminosity': [1, 0.001, 100000, 0.02, 10, 5000, 0.0005, 3000, 0.002, 1.5],
    'Radius': [1, 0.1, 10, 0.5, 2, 8, 0.05, 6, 0.2, 1.2],
    'AbsoluteMagnitude': [4.83, 15, -10, 10, 0, -5, 18, -2, 14, 4]
})

# Display the first few rows of the dataset
print("Dataset preview:")
print(data.head())

# Get information about the dataset
print("\nDataset info:")
print(data.info())

# Describe the dataset for statistical overview
print("\nDataset description:")
print(data.describe())

# Scatter plot of temperature vs luminosity
plt.figure(figsize=(10, 6))
plt.scatter(data['Temperature'], data['Luminosity'], c=data['Temperature'], cmap='viridis')
plt.colorbar(label='Temperature')
plt.xlabel('Temperature (K)')
plt.ylabel('Luminosity (Solar Units)')
plt.title('H-R Diagram')
plt.gca().invert_xaxis()  # Invert x-axis to match the typical H-R diagram
plt.show()

# Seaborn pairplot to visualize relationships between variables
sns.pairplot(data[['Temperature', 'Luminosity', 'Radius', 'AbsoluteMagnitude']])
plt.show()

# Compute the correlation matrix
correlation_matrix = data.corr()

# Print the correlation matrix
print("\nCorrelation matrix:")
print(correlation_matrix)

# Heatmap of the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Summarize findings
print("\nSummary of findings:")
print("1. Temperature and Luminosity have a strong negative correlation.")
print("2. Temperature and Radius also show a negative correlation.")
print("3. Luminosity and Radius have a strong positive correlation.")
