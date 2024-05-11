import pandas as pd

# Load the dataset
data = pd.read_csv('healthcare_data.csv')

# Display the first few rows of the dataset
print("Original Dataset:")
print(data.head())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Remove rows with missing values
cleaned_data = data.dropna()

# Display the cleaned dataset
print("\nCleaned Dataset:")
print(cleaned_data.head())
