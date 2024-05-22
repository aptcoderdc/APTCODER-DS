import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Step 1: Generate Synthetic Dataset
np.random.seed(42)  # for reproducibility

# Generate synthetic exoplanet data
num_samples = 1000
exoplanet_data = {
    'star_temperature': np.random.uniform(2000, 10000, num_samples),
    'exoplanet_radius': np.random.uniform(0.1, 10, num_samples),
    'orbital_period': np.random.uniform(1, 1000, num_samples),
    'semi_major_axis': np.random.uniform(0.1, 100, num_samples),
    'is_exoplanet': np.random.choice([0, 1], size=num_samples, p=[0.8, 0.2])  # 80% non-exoplanets, 20% exoplanets
}

# Create DataFrame
data = pd.DataFrame(exoplanet_data)

# Step 2: Data Exploration
print("Dataset preview:")
print(data.head())
print("\nDataset info:")
print(data.info())
print("\nDataset description:")
print(data.describe())

# Step 3: Data Cleaning (if necessary)
# Handle missing values and outliers

# Step 4: Data Visualization
sns.pairplot(data[['star_temperature', 'exoplanet_radius', 'orbital_period', 'semi_major_axis', 'is_exoplanet']], hue='is_exoplanet', diag_kind='hist')
plt.show()

# Step 5: Exoplanet Identification
# Split data into features and target variable
X = data.drop('is_exoplanet', axis=1)
y = data['is_exoplanet']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Step 6: Evaluation
# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nAccuracy Score:", accuracy_score(y_test, y_pred))

# Step 7: Conclusion
print("\nConclusion:")
print("The model achieved an accuracy of {:.2f}% on the test set.".format(accuracy_score(y_test, y_pred) * 100))
print("Further improvements and optimizations can be made to enhance the model's performance.")
