import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Sample dataset for network traffic (hypothetical data)
data = {
    'Timestamp': ['2024-01-01 00:00', '2024-01-01 01:00', '2024-01-01 02:00', '2024-01-01 03:00', '2024-01-01 04:00'],
    'Packets Sent': [1200, 1500, 1300, 1400, 1600],
    'Packets Received': [1150, 1550, 1250, 1350, 1650],
    'Error Rate (%)': [0.5, 0.4, 0.6, 0.5, 0.3]
}

df = pd.DataFrame(data)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)

# Data normalization
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# K-Means Clustering
kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(scaled_data)
df['Cluster'] = clusters

# Plotting the results
plt.figure(figsize=(10, 6))
for cluster in df['Cluster'].unique():
    subset = df[df['Cluster'] == cluster]
    plt.scatter(subset.index, subset['Packets Sent'], label=f'Cluster {cluster}')
plt.xlabel('Timestamp')
plt.ylabel('Packets Sent')
plt.title('Network Traffic Clustering')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print(df)
