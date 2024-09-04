import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt

# Simulated real-time data with geospatial information
data = {
    'Location': ['City A', 'City B', 'City C', 'City D'],
    'Latitude': [34.0522, 36.7783, 40.7128, 25.7617],
    'Longitude': [-118.2437, -119.4179, -74.0060, -80.1918],
    'Event_Type': ['Flood', 'Earthquake', 'Hurricane', 'Flood'],
    'Severity': ['High', 'Moderate', 'Critical', 'Low']
}
df = pd.DataFrame(data)

# Create geospatial points
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
geo_df = gpd.GeoDataFrame(df, geometry=geometry)

# Dummy world map data using polygons to represent countries
world_data = {
    'Country': ['Country A', 'Country B', 'Country C'],
    'geometry': [
        Polygon([(-130, 20), (-130, 50), (-100, 50), (-100, 20), (-130, 20)]),  # Roughly USA
        Polygon([(-80, 10), (-80, 40), (-50, 40), (-50, 10), (-80, 10)]),       # Roughly South America
        Polygon([(0, 30), (0, 60), (30, 60), (30, 30), (0, 30)])                # Roughly Europe
    ]
}
world = gpd.GeoDataFrame(world_data, crs="EPSG:4326")

# Define the response plan
response_plan = {
    "Critical": "Deploy all resources",
    "High": "Deploy majority of resources",
    "Moderate": "Deploy half of the resources",
    "Low": "Monitor situation"
}

# Apply the response plan
df['Response'] = df['Severity'].map(response_plan)

# Plot the geospatial data
base = world.plot(color='white', edgecolor='black')

geo_df.plot(ax=base, marker='o', color='red', markersize=50)
plt.title('Real-Time Disaster Response Locations')
for x, y, label in zip(df.Longitude, df.Latitude, df.Location):
    plt.text(x, y, label, fontsize=12)
plt.show()

print(df[['Location', 'Event_Type', 'Severity', 'Response']])
