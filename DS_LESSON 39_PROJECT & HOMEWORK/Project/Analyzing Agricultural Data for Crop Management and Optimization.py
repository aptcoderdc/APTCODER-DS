import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Manually creating the dataset
data = pd.DataFrame({
    'temperature': [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    'precipitation': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190],
    'soil_quality': [7, 6, 8, 5, 7, 6, 8, 5, 7, 6],
    'crop_yield': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290]
})

print(data.head())

# Data preprocessing
data = data.fillna(method='ffill')
data['temperature'].fillna(data['temperature'].mean(), inplace=True)
data['temp_precip_interaction'] = data['temperature'] * data['precipitation']

# EDA
sns.pairplot(data)
plt.show()

corr = data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

# Modeling
X = data[['temperature', 'precipitation', 'soil_quality']]
y = data['crop_yield']

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
    'temperature': [25, 30],
    'precipitation': [200, 150],
    'soil_quality': [8, 7]
})

new_data['predicted_yield'] = model.predict(new_data)
print(new_data)
