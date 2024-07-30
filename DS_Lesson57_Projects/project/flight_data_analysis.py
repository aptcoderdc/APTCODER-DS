import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample flight data
data = {
    'Altitude': [35000, 34000, 33000, 30000, 29000, 32000, 31000, 33000, 35000, 36000],
    'Speed': [500, 520, 540, 460, 450, 500, 490, 510, 530, 540],
    'Fuel_Consumption': [5000, 4800, 4700, 4500, 4400, 4600, 4550, 4700, 4900, 5000],
    'Engine_Temperature': [70, 72, 68, 75, 77, 74, 73, 71, 69, 70]
}

df = pd.DataFrame(data)

# Checking for missing values
print("Missing values:\n", df.isnull().sum())

# Standardize the features
scaler = StandardScaler()
X = df[['Altitude', 'Speed', 'Fuel_Consumption', 'Engine_Temperature']]
X = scaler.fit_transform(X)

# Anomaly Detection using Isolation Forest
model = IsolationForest(contamination=0.2, random_state=42)
df['Anomaly'] = model.fit_predict(X)

# Identifying anomalies
print("Anomalies detected:\n", df[df['Anomaly'] == -1])

# Simple linear regression to predict fuel consumption
X_reg = df[['Altitude', 'Speed', 'Engine_Temperature']]
y_reg = df['Fuel_Consumption']
X_reg = scaler.fit_transform(X_reg)

model_reg = LinearRegression()
model_reg.fit(X_reg, y_reg)

# Predict fuel consumption
df['Predicted_Fuel_Consumption'] = model_reg.predict(X_reg)

# Calculate Mean Squared Error
mse = mean_squared_error(y_reg, df['Predicted_Fuel_Consumption'])
print("Mean Squared Error:", mse)

print("Predicted Fuel Consumption:\n", df[['Altitude', 'Speed', 'Engine_Temperature', 'Predicted_Fuel_Consumption']])
