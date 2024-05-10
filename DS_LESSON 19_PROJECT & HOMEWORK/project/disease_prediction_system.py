import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
data = pd.read_csv('patient_records.csv')

# Data Preprocessing
X = data[['Age', 'Blood Pressure', 'Cholesterol Level']]
y = data['Disease Status']

# Encode categorical variable 'Gender'
label_encoder = LabelEncoder()
X['Gender'] = label_encoder.fit_transform(data['Gender'])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model_rf = RandomForestClassifier(n_estimators=100, random_state=42)
model_rf.fit(X_train, y_train)

# Prediction
y_pred = model_rf.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
