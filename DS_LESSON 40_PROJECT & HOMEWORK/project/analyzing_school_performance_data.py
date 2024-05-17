import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('school_performance.csv')

# Check for missing values
print("Missing values before filling:\n", data.isnull().sum())

# Fill missing values only for numeric columns
numeric_cols = data.select_dtypes(include='number').columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# Check for missing values after filling
print("Missing values after filling:\n", data.isnull().sum())

# Summary statistics
print(data.describe())

# Visualize the distribution of scores
plt.figure(figsize=(12, 6))
sns.boxplot(data=data[['Math Score', 'Reading Score', 'Science Score']])
plt.title('Distribution of Scores')
plt.show()

# Correlation matrix
corr = data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Regression Analysis
# Feature and target variables
features = data[['Math Score', 'Reading Score', 'Science Score']]
target = data['Grade']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
predictions = model.predict(X_test)

# Evaluate the model
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)

# Create a binary target variable: pass or fail
data['Pass'] = data['Grade'] >= 6

# Feature and target variables for classification
features = data[['Math Score', 'Reading Score', 'Science Score', 'Days Present']]
target = data['Pass']

# Split data into training and testing sets for classification
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train the classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict on test data
predictions = clf.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, predictions)
print("Classification Accuracy:", accuracy)

# Visualize regression results
plt.scatter(y_test, predictions)
plt.xlabel('Actual Grades')
plt.ylabel('Predicted Grades')
plt.title('Actual vs Predicted Grades')
plt.show()

# Visualize classification results
sns.countplot(data=data, x='Pass', hue='School')
plt.title('Pass vs Fail by School')
plt.show()
