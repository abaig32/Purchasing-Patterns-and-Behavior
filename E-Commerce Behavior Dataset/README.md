HOW TO RUN THE PROGRAM

Click on link for dataset and download

DATASET: https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store 

Insert dataset into data/raw directory
Run the "DataCleaningScript.py" in the src folder
This should create "cleaned_data.csv" in the data/cleaned directory 
Navigate to the E-Commerce Behavior Dataset Exploration.ipynb and run all code
Navigate to the E-Commerce Behavior Clustering.ipynb and run all code

The objective of our analysis was to explore customer purchasing behavior within the e-commerce dataset and uncover key patterns that drive user interactions with products. By analyzing event times, event types, productid, categoryid and more, we aim to understand the factors that influence customer decisions. This analysis also focuses on popular products and brands. We want to focus on and understand deeper relationships and create an understand to why customers tend to buy specific, more popular brands. The main attribute that we want to focus on is event_time. This attribute highlights the key insights that we wanted this analysis to produce. This analysis helps us gain a specific insight into when certain products are bought and fluctuating demand over time based on customer behavior. This analysis should help us to produce a predictor of when certain products are higher and lower in demand. This could be used in cases when a company may need to keep track of inventory based on demand to stop from overpurchasing or underpurchasing inventory. Moving forward, there are some specific questions that we think should be considered. 

1. What time periods show the highest demand for certain products, and how do these patterns fluctuate over time? 
2. Which specific brands and product categories see the highest sales volume during peak times and what factors contribute to their popularity? 
3. How does the length of time between customer interactions (event_type) vary across different product categories, and how can this help us to understand demand? 