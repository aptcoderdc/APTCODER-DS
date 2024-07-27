import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Hypothetical dataset for stress and psychological factors survey
data = {
    'Age': [25, 30, 22, 28, 24, 31, 29, 27, 23, 26],
    'Anxiety': [5, 7, 6, 4, 5, 6, 8, 7, 5, 6],
    'Depression': [6, 8, 5, 7, 6, 5, 7, 8, 6, 7],
    'Sleep Quality': [7, 6, 8, 5, 7, 6, 5, 7, 8, 6],
    'Stress Level': [3, 5, 4, 2, 3, 4, 5, 4, 3, 4]
}

df = pd.DataFrame(data)

# Checking for missing values
print(df.isnull().sum())

# Splitting the data
X = df[['Age', 'Anxiety', 'Depression', 'Sleep Quality']]
y = df['Stress Level']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizing the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Building the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Making Predictions
y_pred = model.predict(X_test)

# Model Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared:", r2_score(y_test, y_pred))

# Displaying the model coefficients
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coefficients)
