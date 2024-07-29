# Step 1: Data Preprocessing
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Expanded simulated brain activity data
data = {
    'Time (s)': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Alpha Waves': [30, 35, 33, 32, 36, 38, 40, 39, 37, 35, 33, 34, 36, 37, 39],
    'Beta Waves': [15, 18, 16, 17, 19, 21, 20, 22, 23, 21, 19, 18, 20, 21, 22],
    'Gamma Waves': [5, 6, 5, 7, 8, 9, 10, 11, 12, 10, 9, 8, 7, 6, 5]
}

df = pd.DataFrame(data)

# Features and target variable
X = df[['Time (s)']]
y_alpha = df['Alpha Waves']
y_beta = df['Beta Waves']
y_gamma = df['Gamma Waves']

# Splitting the data
X_train, X_test, y_alpha_train, y_alpha_test = train_test_split(X, y_alpha, test_size=0.2, random_state=42)
X_train, X_test, y_beta_train, y_beta_test = train_test_split(X, y_beta, test_size=0.2, random_state=42)
X_train, X_test, y_gamma_train, y_gamma_test = train_test_split(X, y_gamma, test_size=0.2, random_state=42)

# Building the model for Alpha Waves
model_alpha = LinearRegression()
model_alpha.fit(X_train, y_alpha_train)
y_alpha_pred = model_alpha.predict(X_test)

# Building the model for Beta Waves
model_beta = LinearRegression()
model_beta.fit(X_train, y_beta_train)
y_beta_pred = model_beta.predict(X_test)

# Building the model for Gamma Waves
model_gamma = LinearRegression()
model_gamma.fit(X_train, y_gamma_train)
y_gamma_pred = model_gamma.predict(X_test)

# Evaluating the models
print("Alpha Waves - Mean Squared Error:", mean_squared_error(y_alpha_test, y_alpha_pred))
print("Alpha Waves - R-squared:", r2_score(y_alpha_test, y_alpha_pred))
print("Beta Waves - Mean Squared Error:", mean_squared_error(y_beta_test, y_beta_pred))
print("Beta Waves - R-squared:", r2_score(y_beta_test, y_beta_pred))
print("Gamma Waves - Mean Squared Error:", mean_squared_error(y_gamma_test, y_gamma_pred))
print("Gamma Waves - R-squared:", r2_score(y_gamma_test, y_gamma_pred))
