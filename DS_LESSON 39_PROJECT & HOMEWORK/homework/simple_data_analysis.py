import pandas as pd

    # Load the dataset
data = pd.read_csv('product_ratings.csv')

    # Calculate average rating
avg_rating = data['Rating'].mean()
print(f"Average Rating: {avg_rating:.2f}")

    # Find the highest and lowest ratings
highest_rating = data['Rating'].max()
lowest_rating = data['Rating'].min()
print(f"Highest Rating: {highest_rating}")
print(f"Lowest Rating: {lowest_rating}")

import matplotlib.pyplot as plt

    # Plot product ratings
plt.figure(figsize=(8, 5))
plt.bar(data['Product'], data['Rating'], color='lightgreen')
plt.xlabel('Product')
plt.ylabel('Rating')
plt.title('Product Ratings')
plt.show()