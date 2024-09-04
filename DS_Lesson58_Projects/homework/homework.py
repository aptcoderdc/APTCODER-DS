import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Simulated social media data
data = {
    'Tweet': [
        "Floods in City A, need help!",
        "Earthquake shakes City B, massive damage reported.",
        "Hurricane approaching City C, evacuate now!",
        "Mild flood in City D, no major impact.",
        "City E recovering from earthquake, relief efforts underway.",
        "Severe hurricane damages City F, critical situation."
    ],
    'Disaster_Type': ['Flood', 'Earthquake', 'Hurricane', 'Flood', 'Earthquake', 'Hurricane']
}

df = pd.DataFrame(data)

# Convert text data into a numerical representation
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Tweet'])

# Encode the disaster types as numerical labels
y = df['Disaster_Type'].astype('category').cat.codes

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Plot the confusion matrix
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Earthquake', 'Flood', 'Hurricane'],
            yticklabels=['Earthquake', 'Flood', 'Hurricane'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()
