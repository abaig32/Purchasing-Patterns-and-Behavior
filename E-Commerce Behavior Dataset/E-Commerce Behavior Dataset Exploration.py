import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from DataCleaning import clean_data


#Data Cleaning

#Data Cleaning
file = '2019-Oct.csv'
df = clean_data(file)

#Data Exploration and Questions

#1 What is the most common event type?
 
event_counts = df['event_type'].value_counts()
event_counts.plot(kind='bar', title='Most Common Event Type', xlabel='Event Type', ylabel='Count')
plt.show()
 
#2 What is the price variation for each product category and the category with the highest price variation?
 
priceStdPerCategory = df.groupby('category_code')['price'].std()
print("Price Variation per Product Category: ")
print(priceStdPerCategory)
 
highestVarCategory = priceStdPerCategory.idxmax()
highestPriceVariation = priceStdPerCategory.max()
print(f"Category with the highest price variation: {highestVarCategory} (Std: ${highestPriceVariation:.2f})")
 
#3 Which product category is the most popular?
 
categoryCounts = df['category_code'].value_counts()
categoryCounts.head(10).plot(kind='bar', title='Top 10 Most Popular Product Categories', xlabel='Category', ylabel='Count')
plt.show()
 
#4 What are the distribution of prices?
 
df['price'].plot(kind='hist', bins=30, title='Price Distribution')
plt.xlabel('Price')
plt.show()
 
#5 Which Brand has the highest Average Price?
 
avgPricePerBrand = df.groupby('brand')['price'].mean().sort_values(ascending=False)
avgPricePerBrand.head(10).plot(kind='bar', title='Top 10 Brands by Average Price', xlabel='Brand', ylabel='Average Price')
plt.show()
 
#6 What is the correlation between Price and Category ID?
 
plt.figure(figsize=(10,6))
plt.scatter(df['category_id'], df['price'], alpha=0.5, color='skyblue')
plt.title('Price vs. Category ID')
plt.xlabel('Category ID')
plt.ylabel('Price')
plt.grid(True)
plt.show()
 
#7 What are the price trends of each category?
 
averagePriceByCategory = df.groupby('category_code')['price'].mean()
plt.figure(figsize=(12,6))
averagePriceByCategory.plot(kind='line', marker='o', color='skyblue')
plt.title('Average Price Trend Across Categories (Subset)')
plt.xlabel('Category Code')
plt.ylabel('Average Price')
plt.grid(True)
plt.show()
 
#8 What is the price range for the most frequent products in each category?
 
productStats = df.groupby('product_id').agg({'price': ['min', 'max'], 'category_code': 'first'}).reset_index()
productStats.columns = ['product_id', 'price_min', 'price_max', 'category_code']
topProducts = df.groupby('product_id').size().nlargest(10).index
topProductStats = productStats[productStats['product_id'].isin(topProducts)]
plt.figure(figsize=(12,6))
sns.barplot(data=topProductStats, x='product_id', y='price_max', hue='category_code', palette='viridis', ci=None)
plt.title('Price Range for Top 10 Most Frequent Products')
plt.xlabel('Product ID')
plt.ylabel('Max Price')
plt.xticks(rotation=45)
plt.legend(title='Category Code')
plt.grid(True)
plt.show()
 
#9 Which ProductID is the most popular?
 
productIDCounts = df['product_id'].value_counts()
topProducts = productIDCounts.head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=topProducts.index, y=topProducts.values, palette='viridis')
plt.title('Top 10 Most Popular Product IDs')
plt.xlabel('Product ID')
plt.ylabel('Number of Purchases')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
 
#10 How does the price distribution vary across different brands?
 
plt.figure(figsize=(14,8))
sns.boxplot(data=df, x='brand', y='price', palette='viridis')
plt.title('Price Distribution Across Different Brands')
plt.xlabel('Brand')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
 
#11 What is the average price for each category code and how does it compare to the overall average?
 
overall_avg_price = df['price'].mean()
avg_price_by_category = df.groupby('category_code')['price'].mean()
print(f'Overall Average Price: {overall_avg_price:.2f}')
print('\nAverage Price by Category Code:')
print(avg_price_by_category)
 
#12 How does Price Distribution differ between purchased and non-purchased products?
 
df['purchased'] = df['price'] > 0
priceStats = df.groupby('purchased')['price'].describe()
print('Price Distribution Statistics by Purchase Status: ')
print(priceStats)
 
# #13 What proportion of total spend is accounted for by each event type?
 
total_spend_by_event = df.groupby('event_type')['price'].sum()
total_spend = total_spend_by_event.sum()
proportion_by_event = total_spend_by_event / total_spend
print('Proportion of Total Spend by Event Type:')
print(proportion_by_event)
 
#14 What are the mean, median, and mode of the price column?
mean_price = df['price'].mean()
median_price = df['price'].median()
mode_price = df['price'].mode()
print(f'Mean Price: {mean_price:.2f}')
print(f'Median Price: {median_price:.2f}')
print(f'Mode Price(s): {mode_price.tolist()}')
 
#15 Which Brand is the most popular?
brand_counts = df['brand'].value_counts()
plt.figure(figsize=(12,8))
sns.barplot(x=brand_counts.index, y=brand_counts.values, palette='viridis')
plt.title('Brand Popularity')
plt.xlabel('Brand')
plt.ylabel('Number of Occurrences')
plt.xticks(rotation=45)
plt.show()


#16 - What is the total revenue by product category
total_revenue_per_category = df.groupby('category_code')['price'].sum()
plt.figure(figsize=(12, 6))
total_revenue_per_category.sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('Total Revenue Generated by Each Product Category')
plt.xlabel('Category Code')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

#17 - How many unique products are there per category
unique_products_per_category = df.groupby('category_code')['product_id'].nunique()
print("Unique Products per Product Category:")
print(unique_products_per_category)

#18 - How do event types differ across the day?
df['hour'] = pd.to_datetime(df['event_time']).dt.hour
events_by_hour = df.groupby(['event_type', 'hour']).size().unstack(fill_value=0)
plt.figure(figsize=(12, 6))
events_by_hour.T.plot(kind='line')
plt.title('Event Type Distribution Across Different Times of the Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Events')
plt.grid(True)
plt.show()

#19 - What category has the highest conversionr ate from cart to purchase?
cart_events = df[df['event_type'] == 'cart']
purchase_events = df[df['event_type'] == 'purchase']
conversion_rate = purchase_events.groupby('category_code').size() / cart_events.groupby('category_code').size()
conversion_rate = conversion_rate.sort_values(ascending=False)
print("Conversion Rate from Cart to Purchase per Category:")
print(conversion_rate)
plt.figure(figsize=(12, 6))
conversion_rate.plot(kind='bar', color='darkgreen')
plt.title('Conversion Rate from Cart to Purchase by Category')
plt.xlabel('Category Code')
plt.ylabel('Conversion Rate')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

#20 - What are the 5 priciest products?
top_5_products = df.groupby('product_id')['price'].max().nlargest(5)
print("Most expensive products:")
print(top_5_products)

#21 -  What is the purchase frequency of these top 5 most expensive products?
top_5_pf = df[df['product_id'].isin(top_5_products.index)].groupby('product_id').size()
print("Purchase frequency of the top 5 most expensive products:")
print(top_5_pf)
plt.figure(figsize=(12, 8))
top_5_products.plot(kind='bar', color='orange')
plt.title('Top 5 Most Expensive Products and Purchase Frequency')
plt.xlabel('Product ID')
plt.ylabel('Number of Purchases')
plt.grid(True)
plt.show()

#22 - How do prices and popularity affect eachother?
product_popularity = df.groupby('product_id').size()
product_avg_price = df.groupby('product_id')['price'].mean()
plt.figure(figsize=(12, 8))
plt.scatter(product_popularity, product_avg_price, alpha=0.5, color='purple')
plt.title('Relationship Between Product Popularity and Price')
plt.xlabel('Product Popularity (Number of Occurrences)')
plt.ylabel('Average Price')
plt.grid(True)
plt.show()

#23 - Frequency of add to cart vs. remove from cart events by category?
# Filter cart events
cart_events = df[df['event_type'].isin(['cart', 'remove_from_cart'])]
cart_action_frequency = cart_events.groupby(['category_code', 'event_type']).size().unstack(fill_value=0)
plt.figure(figsize=(12, 6))
cart_action_frequency.plot(kind='bar', stacked=True, color=['blue', 'red'])
plt.title('Cart vs. Remove from Cart Events by Category')
plt.xlabel('Category Code')
plt.ylabel('Number of Events')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

#24 - What are the top 5 users in terms of spending?
user_spending = df.groupby('user_id')['price'].sum().nlargest(5)
print("Top 5 Users by Total Spending:")
print(user_spending)

#25 - What categories are the top 5 users spending the most in?
top_users = user_spending.index
user_category_preference = df[df['user_id'].isin(top_users)].groupby(['user_id', 'category_code']).size()
print("Top Users' Preferred Categories:")
print(user_category_preference)

#26 - How often are products from each brand being added to a cart vs. being purchased?
cart_purchase_events = df[df['event_type'].isin(['cart', 'purchase'])]
brand_cart_vs_purchase = cart_purchase_events.groupby(['brand', 'event_type']).size().unstack(fill_value=0)
plt.figure(figsize=(12, 6))
brand_cart_vs_purchase.plot(kind='bar', stacked=True, color=['blue', 'green'])
plt.title('Cart vs. Purchase Events by Brand')
plt.xlabel('Brand')
plt.ylabel('Number of Events')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

#27 - Does a product price being higher mean more likely to be removed from cart?
cart_vs_remove = df[df['event_type'].isin(['cart', 'remove_from_cart'])].groupby(['price', 'event_type']).size().unstack(fill_value=0)
plt.figure(figsize=(10, 6))
cart_vs_remove.plot(kind='line', marker='o', color=['blue', 'red'])
plt.title('Cart vs. Remove from Cart Frequency by Price')
plt.xlabel('Price')
plt.ylabel('Number of Events')
plt.grid(True)
plt.show()

#28 - Total number of purchases?
total_purchases = df[df['event_type'] == 'purchase'].shape[0]
print(f"Total number of purchases: {total_purchases}")
# Find the most expensive product
most_expensive_product = df.loc[df['price'].idxmax()]

#29 - Most expensive product?
most_expensive_product = df.loc[df['price'].idxmax()]
print(f"Most expensive product details:\n{most_expensive_product}")


#30 - Total number of unique brands?
unique_brands = df['brand'].nunique()
print(f"Number of unique brands: {unique_brands}")