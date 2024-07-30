import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Sample flight delay data
data = {
    'Flight_Distance': [300, 450, 500, 150, 200, 700, 600, 800, 650, 300],
    'Departure_Time': [10, 12, 14, 9, 11, 15, 16, 17, 13, 10],
    'Arrival_Time': [12, 14, 16, 11, 13, 18, 19, 20, 15, 12],
    'Weather_Conditions': [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],  # 1: Bad, 0: Good
    'Air_Traffic': [1, 1, 0, 0, 1, 1, 0, 1, 0, 1],          # 1: High, 0: Low
    'Flight_Delay': [0, 1, 0, 0, 1, 1, 0, 1, 0, 0]          # 1: Delayed, 0: On Time
}

df = pd.DataFrame(data)

# Checking for missing values
print("Missing values:\n", df.isnull().sum())

# Features and target
X = df[['Flight_Distance', 'Departure_Time', 'Arrival_Time', 'Weather_Conditions', 'Air_Traffic']]
y = df['Flight_Delay']

# Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict flight delays
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:\n", classification_report(y_test, y_pred))

# Show feature importances
importances = model.feature_importances_
features = ['Flight_Distance', 'Departure_Time', 'Arrival_Time', 'Weather_Conditions', 'Air_Traffic']
print("Feature Importances:")
for feature, importance in zip(features, importances):
    print(f"{feature}: {importance:.4f}")
