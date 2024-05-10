import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
data = pd.read_csv('Player_Performance.csv')

# Calculate mean, median, and mode
mean_performance = data['Performance Score'].mean()
median_performance = data['Performance Score'].median()
mode_performance = data['Performance Score'].mode()[0]

# Visualization: Histogram for Performance Score
plt.hist(data['Performance Score'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Performance Score')
plt.ylabel('Frequency')
plt.title('Distribution of Player Performance Score')
plt.show()

# Split dataset into features and target variable
X = data[['Age', 'Height', 'Weight']]
y = data['Performance Score']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression model
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
y_pred_lr = model_lr.predict(X_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)

# Random Forest Classifier model
model_rf = RandomForestClassifier(n_estimators=100, random_state=42)
model_rf.fit(X_train, y_train)
y_pred_rf = model_rf.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)

# Output
print("Mean Performance Score:", mean_performance)
print("Median Performance Score:", median_performance)
print("Mode Performance Score:", mode_performance)
print("Mean Squared Error (Linear Regression):", mse_lr)
print("Accuracy (Random Forest Classifier):", accuracy_rf)
