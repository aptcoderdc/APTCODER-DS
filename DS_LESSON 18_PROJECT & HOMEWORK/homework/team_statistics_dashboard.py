import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Specify the file path
file_path = 'team_statistics.csv'

# Load the dataset
data = pd.read_csv(file_path)

# Calculate mean, median, and mode
mean_wins = data['Wins'].mean()
median_wins = data['Wins'].median()
mode_wins = data['Wins'].mode()[0]

# Visualization: Bar Chart for Wins
plt.bar(data['Team Name'], data['Wins'], color='skyblue')
plt.xlabel('Team Name')
plt.ylabel('Wins')
plt.title('Wins by Team')
plt.xticks(rotation=45, ha='right')
plt.show()

# Split dataset into features and target variable
X = data[['Losses', 'Goals For', 'Goals Against']]
y = data['Points']

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
print("Mean Wins:", mean_wins)
print("Median Wins:", median_wins)
print("Mode Wins:", mode_wins)
print("Mean Squared Error (Linear Regression):", mse_lr)
print("Accuracy (Random Forest Classifier):", accuracy_rf)
