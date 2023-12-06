## [PY-10E] Example - Barcelona Airbnb listings ##

# Importing the data #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/PythonBootcamp/main/Data/'
df = pd.read_csv(path + 'airbnb.csv', index_col=0)

# Exploring the data #
df.info()
df.head()

# Q1a. Counting duplicates #
df.index.duplicated().sum()
df.duplicated().sum()

# Q1b. Dropping duplicates #
df = df.drop_duplicates()
df.shape

# Q2. Proportion of listings with missing ratings #
df.isna().mean()
df['review_scores_rating'].isna().mean().round(3)

# Q3. Distribution of the price #
df['price'].plot.hist(figsize=(7,5), title='Figure 1. Distribution of the price',
    color='gray', edgecolor='white', xlabel='Price per night (euros)');
df['price'].describe()
filter = df['price'].between(25,175)
df['price'][filter].plot.hist(figsize=(7,5),
    title='Figure 2. Distribution of the price (trimmed data)', 
    color='gray', edgecolor='white', bins=30, xlabel='Price per night (euros)');

# Q4. Average price per room type #
pd.pivot_table(df, values='price', index='room_type', aggfunc='mean').round()
pd.pivot_table(df, values='price', index='room_type', aggfunc='median')
roomtype_price =  pd.pivot_table(df, values='price', index='room_type', aggfunc='median')
roomtype_price.plot.bar(figsize=(7,5), legend=False,
    title='Figure 3. Median price per room type', xlabel='Room type',
    color='gray', ylabel='Price per night (euros)');

# Q5. Top-10 neighbourhoods #
df['neighbourhood'].value_counts().head(10)
df.groupby(by='neighbourhood')['price'].agg(['count', 'median']).sort_values(by='count',
    ascending=False).head(10)
