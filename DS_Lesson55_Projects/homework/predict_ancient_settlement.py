import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Prepare Data
data = {
    'Site': ['SiteA', 'SiteB', 'SiteC', 'SiteD', 'SiteE', 'SiteF', 'SiteG', 'SiteH'],
    'Year': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200],
    'Artifacts Found': [150, 200, 250, 180, 210, 230, 270, 300],
    'Site Size (sq km)': [5.0, 6.5, 7.0, 5.5, 6.0, 7.5, 8.0, 8.5],
    'Artifact Density (per sq km)': [30, 31, 35, 32, 35, 30, 33, 35]
}

df = pd.DataFrame(data)

# Step 2: Prepare Features and Target Variable
X = df[['Year', 'Artifacts Found', 'Site Size (sq km)']]
y = df['Artifact Density (per sq km)']

# Splitting Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Build and Evaluate the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared:", r2_score(y_test, y_pred))

# Adding Predictions to DataFrame
df['Predicted Density'] = model.predict(X)
print(df)
