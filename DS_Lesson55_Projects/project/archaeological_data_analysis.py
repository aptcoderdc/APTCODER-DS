import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 1: Prepare Data
data = {
    'Site': ['SiteA', 'SiteB', 'SiteC', 'SiteD', 'SiteE'],
    'Year': [1500, 1600, 1700, 1800, 1900],
    'Artifacts Found': [150, 200, 250, 180, 210],
    'Site Size (sq km)': [5.0, 6.5, 7.0, 5.5, 6.0]
}

df = pd.DataFrame(data)

# Step 2: Analyze Data
# Visualize the data
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['Artifacts Found'], s=df['Site Size (sq km)']*10, alpha=0.5, c='blue')
plt.title('Archaeological Sites Analysis')
plt.xlabel('Year')
plt.ylabel('Artifacts Found')
plt.grid(True)
plt.show()

# Step 3: Clustering
# Preparing data for clustering
X = df[['Year', 'Artifacts Found', 'Site Size (sq km)']]
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
df['Cluster'] = kmeans.labels_

print(df)
