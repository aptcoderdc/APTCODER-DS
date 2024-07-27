import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Hypothetical dataset for personality traits survey
data = {
    'Age': [15, 16, 15, 17, 16, 15, 16, 17, 15, 16],
    'Extroversion': [7, 6, 8, 5, 6, 7, 8, 5, 6, 7],
    'Agreeableness': [5, 6, 7, 6, 5, 7, 6, 5, 7, 6],
    'Conscientiousness': [6, 7, 8, 6, 7, 8, 7, 6, 7, 6],
    'Neuroticism': [5, 4, 3, 4, 5, 3, 4, 5, 3, 4],
    'Openness': [8, 7, 8, 6, 7, 8, 6, 7, 8, 7],
    'Personality Type': ['A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B']
}

df = pd.DataFrame(data)

# Checking for missing values
print(df.isnull().sum())

# Encoding categorical data
df['Personality Type'] = df['Personality Type'].map({'A': 0, 'B': 1})

# Splitting the data
X = df[['Age', 'Extroversion', 'Agreeableness', 'Conscientiousness', 'Neuroticism', 'Openness']]
y = df['Personality Type']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizing the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Building the Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Making Predictions
y_pred = model.predict(X_test)

# Model Evaluation
print(classification_report(y_test, y_pred))
