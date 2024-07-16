# Step 1: Data Preprocessing
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Hypothetical dataset
data = {
    'Age': [30, 40, 50, 60, 70],
    'Cholesterol Level': [200, 240, 230, 220, 260],
    'Blood Pressure': [120, 140, 130, 150, 135],
    'Smoking Status': [0, 1, 1, 0, 1],
    'Physical Activity': [1, 0, 0, 1, 0],
    'Heart Disease': [0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

# Checking for missing values
print(df.isnull().sum())

# Normalizing the data
scaler = StandardScaler()
X = df.drop('Heart Disease', axis=1)
y = df['Heart Disease']
X = scaler.fit_transform(X)

# Step 2: Data Analysis
print("Mean values:\n", df.mean())
print("Standard deviation values:\n", df.std())
print("Correlation with Heart Disease:\n", df.corr()['Heart Disease'])
