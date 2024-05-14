import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_csv('animals.csv')

# Prepare the data for clustering
X = data[['Size', 'Weight', 'Lifespan']]

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
data['Cluster'] = kmeans.labels_

# Visualize the clusters
plt.figure(figsize=(10, 6))

plt.scatter(data['Size'], data['Weight'], c=data['Cluster'], cmap='viridis')
for i, txt in enumerate(data['Name']):
    plt.annotate(txt, (data['Size'][i], data['Weight'][i]), fontsize=9)

plt.title('Animal Clustering')
plt.xlabel('Size (meters)')
plt.ylabel('Weight (kg)')
plt.show()

# Output the clustered data
print(data)
