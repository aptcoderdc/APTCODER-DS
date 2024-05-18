import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Generate Synthetic Data
np.random.seed(42)
n_samples = 1000
n_features = 5

# Generate synthetic features
X = np.random.rand(n_samples, n_features)

# Generate synthetic target variable
true_coefficients = np.random.randint(1, 10, size=n_features)
true_intercept = np.random.randint(1, 10)
y = X.dot(true_coefficients) + true_intercept + np.random.normal(scale=0.1, size=n_samples)

# Create DataFrame
data = pd.DataFrame(X, columns=[f'Feature_{i}' for i in range(1, n_features+1)])
data['Price'] = y

# Step 2: Data Exploration
print(data.head())
print(data.describe())

sns.pairplot(data)
plt.show()

# Step 3: Data Preprocessing
X = data.drop('Price', axis=1)
y = data['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Model Training and Evaluation
# Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)
lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))
lr_r2 = r2_score(y_test, lr_pred)
print("Linear Regression RMSE:", lr_rmse)
print("Linear Regression R^2 Score:", lr_r2)

# Decision Tree Regression
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)
dt_rmse = np.sqrt(mean_squared_error(y_test, dt_pred))
dt_r2 = r2_score(y_test, dt_pred)
print("\nDecision Tree Regression RMSE:", dt_rmse)
print("Decision Tree Regression R^2 Score:", dt_r2)

# Random Forest Regression
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
rf_r2 = r2_score(y_test, rf_pred)
print("\nRandom Forest Regression RMSE:", rf_rmse)
print("Random Forest Regression R^2 Score:", rf_r2)
