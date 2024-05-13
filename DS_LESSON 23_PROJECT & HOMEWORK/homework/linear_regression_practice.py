import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv('income_expenditure.csv')

# Visualize the relationship between income and expenditure
plt.scatter(data['Income'], data['Expenditure'], color='green')
plt.title('Income vs Expenditure')
plt.xlabel('Income')
plt.ylabel('Expenditure')
plt.show()

# Prepare the data for linear regression
X = data[['Income']]
y = data['Expenditure']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Visualize the regression line
plt.scatter(data['Income'], data['Expenditure'], color='green')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.title('Income vs Expenditure (Linear Regression)')
plt.xlabel('Income')
plt.ylabel('Expenditure')
plt.show()

# Predict future expenditure
future_income = np.array([[50000]])  # Assume $50,000 income
future_expenditure = model.predict(future_income)
print("Predicted Expenditure for $50,000 Income:", future_expenditure[0])
