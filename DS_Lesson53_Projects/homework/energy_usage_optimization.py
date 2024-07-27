import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Expanded hypothetical dataset including weather data
data = {
    'Date': pd.date_range(start='1/1/2020', periods=100, freq='D'),
    'Consumption': np.random.randint(100, 500, size=100),
    'Temperature': np.random.randint(-10, 35, size=100),
    'Humidity': np.random.randint(20, 100, size=100)
}

df = pd.DataFrame(data)

# Step 1: Data Preprocessing
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Checking for missing values
print(df.isnull().sum())

# Step 2: Exploratory Data Analysis (EDA)
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Consumption'], label='Energy Consumption')
plt.xlabel('Date')
plt.ylabel('Consumption')
plt.title('Energy Consumption Over Time')
plt.legend()
plt.show()

# Step 3: Predictive Modeling
X = df[['Day', 'Month', 'Year', 'Temperature', 'Humidity']]
y = df['Consumption']
scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Model Evaluation
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared:", r2_score(y_test, y_pred))

# Step 5: Identifying Optimization Opportunities
df['Prediction'] = model.predict(scaler.transform(df[['Day', 'Month', 'Year', 'Temperature', 'Humidity']]))
df['Optimized_Consumption'] = df['Prediction'] * 0.9  # Assuming a 10% optimization potential

plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Consumption'], label='Actual Consumption')
plt.plot(df['Date'], df['Optimized_Consumption'], label='Optimized Consumption', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Consumption')
plt.title('Energy Consumption Optimization')
plt.legend()
plt.show()
