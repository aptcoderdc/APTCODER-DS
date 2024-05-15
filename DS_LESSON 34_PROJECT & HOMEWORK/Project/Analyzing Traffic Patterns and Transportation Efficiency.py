import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from heapq import heappush, heappop

# Step 1: Generate Synthetic Traffic Data
np.random.seed(42)

# Generate random timestamps for a day
timestamps = pd.date_range(start='2024-05-15', end='2024-05-16', freq='1min')

# Generate random speed and congestion level data
speeds = np.random.randint(0, 100, size=len(timestamps))
congestion = np.random.choice([0, 1], size=len(timestamps), p=[0.8, 0.2])

# Create a DataFrame
traffic_data = pd.DataFrame({'timestamp': timestamps, 'speed': speeds, 'congestion': congestion})

# Step 2: Exploratory Data Analysis (EDA)
# Visualize traffic patterns
plt.figure(figsize=(10, 6))
plt.hist(traffic_data['timestamp'].dt.hour, bins=24, edgecolor='black')
plt.title('Distribution of Traffic by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Vehicles')
plt.grid(True)
plt.show()

# Step 3: Traffic Prediction Model
# Split data into features (X) and target variable (y)
X = traffic_data[['timestamp', 'speed']].copy()
X['hour'] = X['timestamp'].dt.hour
X.drop('timestamp', axis=1, inplace=True)
y = traffic_data['congestion']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict congestion levels
y_pred = clf.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 4: Route Optimization
def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heappush(queue, (cost + weight, neighbor, path))
    return []

# Example graph representing transportation network
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'C': 1, 'D': 4},
    'C': {'D': 2},
    'D': {}
}

start_node = 'A'
end_node = 'D'
optimal_route = dijkstra(graph, start_node, end_node)
print("Optimal Route:", optimal_route)

# Step 5: Evaluation and Validation
# Validate optimized routes using simulation or real-world testing
