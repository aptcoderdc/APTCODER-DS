import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv('student_scores.csv')

# Visualize the relationship between study hours and scores
plt.scatter(data['Study Hours'], data['Scores'], color='blue')
plt.title('Study Hours vs Scores')
plt.xlabel('Study Hours')
plt.ylabel('Scores')
plt.show()

# Prepare the data for linear regression
X = data[['Study Hours']]
y = data['Scores']

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
plt.scatter(data['Study Hours'], data['Scores'], color='blue')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.title('Study Hours vs Scores (Linear Regression)')
plt.xlabel('Study Hours')
plt.ylabel('Scores')
plt.show()

# Predict future scores
future_hours = np.array([[10]])  # Assume 10 study hours
future_score = model.predict(future_hours)
print("Predicted Score for 10 Study Hours:", future_score[0])
