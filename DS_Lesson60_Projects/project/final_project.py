import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import plotly.express as px

# Generate synthetic data
def generate_data(num_records):
    np.random.seed(0)
    data = {
        'patient_age': np.random.randint(20, 80, size=num_records),
        'pollution_level': np.random.uniform(0, 100, size=num_records),
        'crime_rate': np.random.uniform(0, 10, size=num_records),
        'star_brightness': np.random.uniform(1, 100, size=num_records),
        'robot_sensor_value': np.random.uniform(0, 1000, size=num_records),
        'target': np.random.randint(0, 2, size=num_records)  # Binary target variable for prediction
    }
    return pd.DataFrame(data)

# Create and save synthetic dataset
data = generate_data(1000)
data.to_csv('synthetic_data.csv', index=False)

# Load dataset
data = pd.read_csv('synthetic_data.csv')

# EDA and Visualization
def plot_eda(data):
    plt.figure(figsize=(14, 8))
    sns.pairplot(data, hue='target', palette='coolwarm')
    plt.title('Pairwise Plot of Features')
    plt.show()

plot_eda(data)

# Preprocessing
def preprocess_data(data):
    features = data.drop('target', axis=1)
    target = data['target']
    
    # Define preprocessing steps
    scaler = StandardScaler()
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', scaler, features.columns)
        ]
    )
    
    return preprocessor.fit_transform(features), target

X, y = preprocess_data(data)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Train models
models = {
    'RandomForest': RandomForestClassifier(),
    'SVM': SVC(),
    'DecisionTree': DecisionTreeClassifier()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"{name} Model:")
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print('-' * 50)

# Interactive Visualization
def plot_interactive(data, predictions):
    fig = px.scatter(data, x='pollution_level', y='star_brightness', color=predictions, title='Predictions vs Features')
    fig.show()

# Example: Plot predictions of the RandomForest model
predictions = models['RandomForest'].predict(X_test)
plot_interactive(data.iloc[X_test.index], predictions)


