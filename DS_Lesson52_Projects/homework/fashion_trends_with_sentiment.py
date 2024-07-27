# Step 1: Data Preprocessing
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Expanded hypothetical dataset for fashion trends (Sentiment: Consumer sentiment score)
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Year': [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023],
    'Sentiment': [0.5, 0.6, 0.7, 0.6, 0.8, 0.9, 0.7, 0.8, 0.9, 0.6, 0.7, 0.8],
    'Sales': [150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
}

df = pd.DataFrame(data)

# Checking for missing values
print(df.isnull().sum())

# Encoding categorical data
df['Month'] = pd.factorize(df['Month'])[0]

# Normalizing the data
scaler = StandardScaler()
X = df[['Month', 'Year', 'Sentiment']]
y = df['Sales']
X = scaler.fit_transform(X)

# Step 2: Building the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Step 3: Model Evaluation
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared:", r2_score(y_test, y_pred))

# Visualizing the results
plt.plot(df['Month'], df['Sales'], label='Actual Sales')
plt.plot(df['Month'], model.predict(scaler.transform(df[['Month', 'Year', 'Sentiment']])), label='Predicted Sales', linestyle='--')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.title('Fashion Sales Trends with Sentiment Analysis')
plt.show()
