import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Generate Sample Data
np.random.seed(42)
n_samples = 1000
age = np.random.normal(loc=40, scale=10, size=n_samples)
salary = np.random.normal(loc=50000, scale=10000, size=n_samples)
purchased = np.random.choice([0, 1], size=n_samples, p=[0.7, 0.3])

data = pd.DataFrame({'Age': age, 'Salary': salary, 'Purchased': purchased})

# Step 2: Data Exploration
sns.scatterplot(x='Age', y='Salary', hue='Purchased', data=data)
plt.title('Age vs Salary')
plt.show()

# Step 3: Data Preprocessing
X = data[['Age', 'Salary']]
y = data['Purchased']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 4: Model Training and Evaluation
# Decision Tree
dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train_scaled, y_train)
dt_pred = dt_classifier.predict(X_test_scaled)
dt_accuracy = accuracy_score(y_test, dt_pred)
print("Decision Tree Accuracy:", dt_accuracy)

# Random Forest
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train_scaled, y_train)
rf_pred = rf_classifier.predict(X_test_scaled)
rf_accuracy = accuracy_score(y_test, rf_pred)
print("Random Forest Accuracy:", rf_accuracy)

# SVM
svm_classifier = SVC(kernel='linear', random_state=42)
svm_classifier.fit(X_train_scaled, y_train)
svm_pred = svm_classifier.predict(X_test_scaled)
svm_accuracy = accuracy_score(y_test, svm_pred)
print("SVM Accuracy:", svm_accuracy)

# Step 5: Model Evaluation Metrics
print("\nDecision Tree Classification Report:")
print(classification_report(y_test, dt_pred))

print("\nRandom Forest Classification Report:")
print(classification_report(y_test, rf_pred))

print("\nSVM Classification Report:")
print(classification_report(y_test, svm_pred))
