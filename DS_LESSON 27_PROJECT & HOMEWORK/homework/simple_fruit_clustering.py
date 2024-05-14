import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_csv('fruits.csv')

# Prepare the data for clustering
X = data[['Sweetness', 'Sourness', 'Crunchiness']]

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
data['Cluster'] = kmeans.labels_

# Visualize the clusters
plt.figure(figsize=(10, 6))

plt.scatter(data['Sweetness'], data['Sourness'], c=data['Cluster'], cmap='viridis')
for i, txt in enumerate(data['Name']):
    plt.annotate(txt, (data['Sweetness'][i], data['Sourness'][i]), fontsize=9)

plt.title('Fruit Clustering')
plt.xlabel('Sweetness')
plt.ylabel('Sourness')
plt.show()

# Output the clustered data
print(data)
