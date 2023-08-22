## [PY-09E] Example - Barcelona Airbnb listings ##

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
df['price'].plot.hist(figsize=(8,6), color='gray', edgecolor='white');
df['price'].describe()
df['price'][df['price'].between(25,175)].plot.hist(figsize=(8,6), color='gray', edgecolor='white', bins=30);

# Q4. Average price per room type #
pd.pivot_table(df, values='price', index='room_type', aggfunc='mean').round()
pd.pivot_table(df, values='price', index='room_type', aggfunc='median')
roomtype_price =  pd.pivot_table(df, values='price', index='room_type', aggfunc='median')
roomtype_price.plot.bar(figsize=(8,6), color='gray');

# Q5. Top-10 neighbourhoods #
df['neighbourhood'].value_counts().head(10)
df.groupby(by='neighbourhood')['price'].agg(['count', 'median']).sort_values(by='count', ascending=False).head(10)
