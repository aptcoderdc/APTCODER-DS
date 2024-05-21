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
        left_sensor = random.randint(0, 1)   # 0 or 1
        center_sensor = random.randint(0, 1) # 0 or 1
        right_sensor = random.randint(0, 1)  # 0 or 1
        
        if left_sensor == 1 and center_sensor == 0 and right_sensor == 0:
            label = 'Left'
        elif left_sensor == 0 and center_sensor == 0 and right_sensor == 1:
            label = 'Right'
        elif center_sensor == 1:
            label = 'Forward'
        else:
            label = 'Stop'  # In case no sensor detects the line
        
        data.append([left_sensor, center_sensor, right_sensor, label])
        time.sleep(0.1)  # Simulate sensor reading interval

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(data, columns=['Left_Sensor', 'Center_Sensor', 'Right_Sensor', 'Label'])
    df.to_csv('line_following_data.csv', index=False)

# Step 2: Data Preprocessing
def preprocess_data():
    df = pd.read_csv('line_following_data.csv')
    df['Label'] = df['Label'].map({'Left': 0, 'Right': 1, 'Forward': 2, 'Stop': 3})
    X = df[['Left_Sensor', 'Center_Sensor', 'Right_Sensor']].values
    y = df['Label'].values
    return X, y

# Step 3: Model Training
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
    joblib.dump(model, 'line_following_model.pkl')

# Step 4: Model Deployment
def deploy_model():
    model = joblib.load('line_following_model.pkl')

    def decide_movement(left_sensor, center_sensor, right_sensor):
        prediction = model.predict([[left_sensor, center_sensor, right_sensor]])
        if prediction == 0:
            return 'Left'
        elif prediction == 1:
            return 'Right'
        elif prediction == 2:
            return 'Forward'
        else:
            return 'Stop'

    while True:
        left_sensor = random.randint(0, 1)
        center_sensor = random.randint(0, 1)
        right_sensor = random.randint(0, 1)
        
        movement = decide_movement(left_sensor, center_sensor, right_sensor)
        print(f'Sensors: L={left_sensor}, C={center_sensor}, R={right_sensor} -> Movement: {movement}')
        
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
