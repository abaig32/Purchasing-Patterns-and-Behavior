Name: Mirza Baig, Raaid Chaudry

#1 Summarize the specifics of what you did in the cleaning and analysis steps

In the cleaning section, we made sure to look at the data at a surface level and see if we could identify anything that was wrong. In our case,
there was not much that could be identified for cleaning through observation. When the cleaning began, we made sure to do a deeper dive into the data
by looking at basic info about the dataset. We noticed that there were a large number of null values and got rid of those. There were also several duplicate
rows and we made sure to get rid of those as well. Then we dropped some columns that were redundant to our analysis and created a subset of the dataset. The last
thing in the data cleaning process was clearing out the outliers in the price column by looking at quartiles to get more consistent pricing.

In the analysis step, we made sure to first focus on gaining an overall knowledge of the distributions and overall data through simple plots. After that was done,
the next part of the analysis was to look at trends in certain columns as well as looking at relationships between certain columns. This gave us a greater insight
into what columns could be related to one another and how they could influence purchasing patterns. We used a combination of plots and statistics to better understand
the distribution of data and potential relationships.

#2 List all the interesting or unexpected observations in your analysis and a possible explanation for what's behind them

One interesting observation that we had was that the most popular productID and the price ranges for each product do not completely line up. For example, the most
purchased productID has the second-highest price range when it comes to the top 10 most frequently purchased products. That is something that on the surface, doesn't
make a lot of sense. However, a possible explanation to this could be that this particular product has features or capabilites that the other products do not. The most frequently
purchased items are mostly smartphones, however, this particular productID was the most frequently selling smartphone of them all but at the 2nd highest price.

Something else that we noticed was that the 'event_type' column had 3 data values which were 'view', 'cart', and 'remove_from_cart'. When we did a deeper dive through
the use of stats to see how much of the total spend was weighed by these 3 value, we found that 'view' accounted for around 0.9 or 90% of the values. This means that
the other options of adding to cart or removing from cart are options that people are not doing as much. A possible explanation for this could be that people don't
like a certain product, are spend more time looking through products rather than purchasing, etc.

Another thing that we noticed was the distribution of prices were not uniform. We noticed that a large portion of the prices were between 0-500, however, there were
also a lot of prices out of that range within the range of 750-1750 but had non-uniform frequencies. A possible explanation of this could be the wide range of products
that this store offers. They vary from things such as headphones to water heaters. This can create the big gaps in pricing as seen through the plots that we created.

#3 List a few more specific questions to dive deeper into for a future analysis as a followup to what you have done here

Which brands dominate specific product categories? Do these brands have specific benefits?
Is there a specific difference between popular vs less popular brands? Price? ProductID?
Could there be a way incorporate user_id into the analysis? Could you compare it with category or productID?