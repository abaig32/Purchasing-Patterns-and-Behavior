import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('2019-Oct.csv')
pd.set_option('display.max_columns', None)

#Data Cleaning

# #Analyzing the dataset
df.info()

#Dropping Duplicate Rows
df.drop_duplicates()

#Detecting Missing Values
print(df.isnull().sum())

#Dropping columns to create a smaller subset focusing on product categories
df = df.drop('user_session', axis=1)
df = df.drop('event_time', axis=1)
df.drop('user_id', axis=1)

#Dropping all the null values
df = df.dropna()

#Find and Clean Outlier Values within the price column
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1

lowerFence = Q1 - 1.5 * IQR
upperFence = Q3 + 1.5 * IQR

outliers = df[(df['price'] < lowerFence) | (df['price'] > upperFence)]
df = df.drop(outliers.index)

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

