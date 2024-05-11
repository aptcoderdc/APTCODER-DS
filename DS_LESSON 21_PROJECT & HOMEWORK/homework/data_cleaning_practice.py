import pandas as pd

# Load the dataset
data = pd.read_csv('healthcare_data.csv')

# Impute missing values using median
median_age = data['Age'].median()
median_blood_pressure = data['Blood Pressure'].median()

data['Age'].fillna(median_age, inplace=True)
data['Blood Pressure'].fillna(median_blood_pressure, inplace=True)

# Display the cleaned dataset
print("Imputed Dataset:")
print(data.head())
