import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Manually creating the dataset
data = pd.DataFrame({
    'temperature': [20, 22, 24, 26, 28, 25, 23, 27, 29, 21],
    'humidity': [30, 35, 40, 45, 50, 42, 37, 48, 53, 32],
    'rainfall': [5, 10, 15, 20, 25, 18, 12, 22, 28, 7],
    'soil_type': [1, 2, 1, 3, 2, 1, 3, 2, 1, 3], # 1: Sandy, 2: Clay, 3: Loam
    'soil_moisture': [15, 20, 25, 30, 35, 28, 22, 32, 38, 18]
})

print(data.head())

# Data preprocessing
data = data.fillna(method='ffill')
data['soil_type'] = data['soil_type'].astype('category')

# Convert categorical data to numeric
data = pd.get_dummies(data, drop_first=True)

# EDA
sns.pairplot(data)
plt.show()

corr = data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

# Modeling
X = data.drop('soil_moisture', axis=1)
y = data['soil_moisture']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Prediction and Optimization
new_data = pd.DataFrame({
    'temperature': [27, 30],
    'humidity': [40, 45],
    'rainfall': [18, 25],
    'soil_type_2': [0, 1], # Clay
    'soil_type_3': [1, 0]  # Loam
})

new_data['predicted_soil_moisture'] = model.predict(new_data)
print(new_data)
