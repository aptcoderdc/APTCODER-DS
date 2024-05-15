import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Step 1: Generate Synthetic Public Transportation Data
np.random.seed(42)

# Generate random timestamps and passenger counts for buses
timestamps = pd.date_range(start='2024-05-15', end='2024-05-16', freq='30min')
passenger_counts = np.random.randint(0, 50, size=len(timestamps))

# Create a DataFrame
bus_data = pd.DataFrame({'timestamp': timestamps, 'passenger_count': passenger_counts})

# Step 2: Preprocess Data
# Extract hour and minute from timestamp
bus_data['hour'] = bus_data['timestamp'].dt.hour
bus_data['minute'] = bus_data['timestamp'].dt.minute

# Step 3: Clustering to Identify Demand Patterns
# Select features for clustering
X = bus_data[['hour', 'minute', 'passenger_count']]

# Determine optimal number of clusters using silhouette score
silhouette_scores = []
for n_clusters in range(2, 11):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(X)
    silhouette_avg = silhouette_score(X, cluster_labels)
    silhouette_scores.append(silhouette_avg)

# Choose the number of clusters with highest silhouette score
optimal_num_clusters = silhouette_scores.index(max(silhouette_scores)) + 2

# Perform KMeans clustering with optimal number of clusters
kmeans = KMeans(n_clusters=optimal_num_clusters, random_state=42)
bus_data['cluster'] = kmeans.fit_predict(X)

# Step 4: Analyze Demand Patterns
# Visualize demand patterns for each cluster
plt.figure(figsize=(12, 6))
for cluster in range(optimal_num_clusters):
    plt.subplot(2, 4, cluster+1)
    cluster_data = bus_data[bus_data['cluster'] == cluster]
    plt.hist(cluster_data['passenger_count'], bins=20, edgecolor='black')
    plt.title(f'Cluster {cluster+1}')
    plt.xlabel('Passenger Count')
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Step 5: Optimize Transportation Schedules
# Based on demand patterns identified in clusters, adjust bus schedules accordingly
