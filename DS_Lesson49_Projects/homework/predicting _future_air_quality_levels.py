# Step 1: Data Preprocessing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Expanded hypothetical dataset for air quality
data = {
    'City': ['CityA', 'CityB', 'CityC', 'CityD', 'CityE', 'CityF', 'CityG', 'CityH', 'CityI', 'CityJ'],
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'AQI': [60, 58, 55, 57, 54, 52, 50, 48, 45, 43],
    'Population': [100000, 150000, 200000, 120000, 180000, 160000, 140000, 130000, 110000, 170000],
    'Industrial Activity': [5, 6, 7, 5, 8, 7, 6, 4, 5, 7]
}

df = pd.DataFrame(data)

# Checking for missing values
print(df.isnull().sum())

# Encoding categorical data
df['City'] = pd.factorize(df['City'])[0]

# Normalizing the data
scaler = StandardScaler()
X = df[['City', 'Year', 'Population', 'Industrial Activity']]
y = df['AQI']
X = scaler.fit_transform(X)

# Step 2: Building the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Step 3: Model Evaluation
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared:", r2_score(y_test, y_pred))
