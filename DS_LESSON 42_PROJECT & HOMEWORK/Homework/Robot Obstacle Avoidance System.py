import time
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Data Collection
def collect_data():
    data = []
    for _ in range(1000):
        distance = random.uniform(2.0, 100.0)  # Simulate distance readings in cm
        label = 'Obstacle' if distance < 30.0 else 'No Obstacle'
        data.append([distance, label])
        time.sleep(0.1)  # Simulate sensor reading interval

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(data, columns=['Distance', 'Label'])
    df.to_csv('sensor_data.csv', index=False)

# Step 2: Data Preprocessing
def preprocess_data():
    df = pd.read_csv('sensor_data.csv')
    df['Label'] = df['Label'].map({'Obstacle': 1, 'No Obstacle': 0})
    X = df[['Distance']].values
    y = df['Label'].values
    return X, y

# Step 3: Model Training
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
    joblib.dump(model, 'obstacle_avoidance_model.pkl')

# Step 4: Model Deployment
def deploy_model():
    model = joblib.load('obstacle_avoidance_model.pkl')

    def check_obstacle(distance):
        prediction = model.predict([[distance]])
        return 'Obstacle' if prediction == 1 else 'No Obstacle'

    while True:
        distance = random.uniform(2.0, 100.0)
        decision = check_obstacle(distance)
        if decision == 'Obstacle':
            print("Obstacle detected! Stopping or changing direction.")
        else:
            print("Path is clear. Moving forward.")
        time.sleep(1)  # Simulate control loop interval

if __name__ == "__main__":
    # Collect data
    collect_data()
    
    # Preprocess data
    X, y = preprocess_data()
    
    # Train model
    train_model(X, y)
    
    # Deploy model
    deploy_model()
