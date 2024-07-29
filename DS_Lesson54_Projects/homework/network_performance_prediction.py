import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Expanded hypothetical dataset for network traffic
data = {
    'Timestamp': ['2024-01-01 00:00', '2024-01-01 01:00', '2024-01-01 02:00', '2024-01-01 03:00', '2024-01-01 04:00', 
                  '2024-01-01 05:00', '2024-01-01 06:00', '2024-01-01 07:00', '2024-01-01 08:00', '2024-01-01 09:00'],
    'Packets Sent': [1200, 1500, 1300, 1400, 1600, 1550, 1650, 1750, 1700, 1800],
    'Packets Received': [1150, 1550, 1250, 1350, 1650, 1600, 1700, 1800, 1750, 1850],
    'Error Rate (%)': [0.5, 0.4, 0.6, 0.5, 0.3, 0.4, 0.3, 0.2, 0.4, 0.3],
    'Network Latency (ms)': [50, 45, 55, 52, 48, 46, 47, 49, 51, 53]
}

df = pd.DataFrame(data)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)

# Data normalization
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.drop('Error Rate (%)', axis=1))
X = scaled_data
y = df['Error Rate (%)']

# Building the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared:", r2_score(y_test, y_pred))

# Predicting future error rates
future_data = {
    'Packets Sent': [1850, 1900, 1950],
    'Packets Received': [1800, 1850, 1900],
    'Network Latency (ms)': [54, 56, 58]
}
future_df = pd.DataFrame(future_data)
future_scaled = scaler.transform(future_df)
predicted_errors = model.predict(future_scaled)
print("Predicted Future Error Rates:", predicted_errors)
