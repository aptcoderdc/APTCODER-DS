# Step 1: Data Preprocessing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Expanded hypothetical dataset
data = {
    'Age': [25, 35, 45, 55, 65, 30, 50, 40, 60, 70, 32, 48, 52, 58, 68],
    'BMI': [22, 28, 30, 26, 34, 25, 32, 29, 27, 33, 23, 31, 28, 24, 35],
    'Blood Pressure': [80, 85, 90, 75, 88, 84, 89, 77, 92, 83, 86, 79, 91, 76, 87],
    'Glucose Level': [100, 140, 120, 110, 160, 130, 150, 135, 145, 155, 125, 142, 138, 148, 158],
    'Insulin Level': [15, 25, 22, 18, 30, 20, 27, 24, 21, 29, 19, 23, 26, 28, 31],
    'Diabetes': [0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

# Checking for missing values
print(df.isnull().sum())

# Normalizing the data
scaler = StandardScaler()
X = df.drop('Diabetes', axis=1)
y = df['Diabetes']
X = scaler.fit_transform(X)

# Step 2: Building the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 3: Model Evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
