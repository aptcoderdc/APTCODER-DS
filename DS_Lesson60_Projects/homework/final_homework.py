import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Generate and modify synthetic data
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

def modify_data(data):
    data_with_missing = data.copy()
    data_with_missing.loc[np.random.choice(data.index, size=100, replace=False), 'pollution_level'] = np.nan
    return data_with_missing

data = generate_data(1000)
data_modified = modify_data(data)

# Preprocessing
def preprocess_data(data):
    features = data.drop('target', axis=1)
    target = data['target']
    
    # Define preprocessing steps
    scaler = StandardScaler()
    imputer = SimpleImputer(strategy='mean')
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', Pipeline(steps=[('imputer', imputer), ('scaler', scaler)]), features.columns)
        ]
    )
    
    return preprocessor.fit_transform(features), target, features.columns

X, y, feature_names = preprocess_data(data_modified)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Hyperparameter tuning for RandomForest
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30]
}

grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=3)
grid_search.fit(X_train, y_train)
print(f"Best Parameters: {grid_search.best_params_}")

# Train and evaluate the best model
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
print("Enhanced RandomForest Model:")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Plot feature importance
def plot_feature_importance(model, feature_names):
    importances = model.feature_importances_
    indices = np.argsort(importances)
    plt.figure(figsize=(10, 6))
    plt.title('Feature Importance')
    plt.barh(range(len(importances)), importances[indices], align='center')
    plt.yticks(range(len(importances)), [feature_names[i] for i in indices])
    plt.xlabel('Importance')
    plt.show()

plot_feature_importance(best_model, feature_names)


