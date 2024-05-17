import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('product_sales.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Calculate the average rating
avg_rating = data['Rating'].mean()
print(f"\nAverage Rating: {avg_rating:.2f}")

# Calculate the total sales
total_sales = data['Sales'].sum()
print(f"Total Sales: {total_sales}")

# Calculate the average price
avg_price = data['Price'].mean()
print(f"Average Price: {avg_price:.2f}")

# Identify the product with the highest sales
max_sales_product = data.loc[data['Sales'].idxmax()]['Product']
max_sales_value = data['Sales'].max()
print(f"Product with the Highest Sales: {max_sales_product} ({max_sales_value} units)")

# Identify the product with the highest rating
max_rating_product = data.loc[data['Rating'].idxmax()]['Product']
max_rating_value = data['Rating'].max()
print(f"Product with the Highest Rating: {max_rating_product} ({max_rating_value} stars)")

# Plot product sales
plt.figure(figsize=(10, 6))
plt.bar(data['Product'], data['Sales'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Product Sales')
plt.show()

# Plot product ratings
plt.figure(figsize=(10, 6))
sns.barplot(x='Product', y='Rating', data=data, palette='viridis')
plt.xlabel('Product')
plt.ylabel('Rating')
plt.title('Product Ratings')
plt.show()

# Plot product prices
plt.figure(figsize=(10, 6))
sns.barplot(x='Product', y='Price', data=data, palette='coolwarm')
plt.xlabel('Product')
plt.ylabel('Price')
plt.title('Product Prices')
plt.show()

# Correlation between price and sales
correlation_price_sales = data['Price'].corr(data['Sales'])
print(f"Correlation between Price and Sales: {correlation_price_sales:.2f}")

# Correlation between rating and sales
correlation_rating_sales = data['Rating'].corr(data['Sales'])
print(f"Correlation between Rating and Sales: {correlation_rating_sales:.2f}")

# Create scatter plot for Price vs Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Price', y='Sales', data=data, hue='Product', palette='deep', s=100)
plt.xlabel('Price')
plt.ylabel('Sales')
plt.title('Price vs Sales')
plt.show()

# Create scatter plot for Rating vs Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Rating', y='Sales', data=data, hue='Product', palette='muted', s=100)
plt.xlabel('Rating')
plt.ylabel('Sales')
plt.title('Rating vs Sales')
plt.show()

# Average Sales by Rating
avg_sales_by_rating = data.groupby('Rating')['Sales'].mean().reset_index()
print("\nAverage Sales by Rating:")
print(avg_sales_by_rating)

# Plot average sales by rating
plt.figure(figsize=(10, 6))
sns.barplot(x='Rating', y='Sales', data=avg_sales_by_rating, palette='Blues_d')
plt.xlabel('Rating')
plt.ylabel('Average Sales')
plt.title('Average Sales by Rating')
plt.show()

# Average Sales by Price Range
data['Price Range'] = pd.cut(data['Price'], bins=[0, 10, 20, 30], labels=['Low', 'Medium', 'High'])
avg_sales_by_price_range = data.groupby('Price Range')['Sales'].mean().reset_index()
print("\nAverage Sales by Price Range:")
print(avg_sales_by_price_range)

# Plot average sales by price range
plt.figure(figsize=(10, 6))
sns.barplot(x='Price Range', y='Sales', data=avg_sales_by_price_range, palette='Oranges_r')
plt.xlabel('Price Range')
plt.ylabel('Average Sales')
plt.title('Average Sales by Price Range')
plt.show()
