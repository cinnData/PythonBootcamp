## [PY-09E] Example - Barcelona Airbnb listings ##

# Q1. Importing the data #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/PythonBootcamp/main/Data/'
filename = path + 'airbnb.csv'
df = pd.read_csv(filename, index_col=0)
df.info()
df.head()

# Q2a. Counting duplicates #
df.index.duplicated().sum()
df.duplicated().sum()

# Q2b. Dropping duplicates #
df = df.drop_duplicates()
df.shape

# Q3. How old are the hosts? #
df['host_id'][df['host_since'] < '2010-01-01'].unique()
len(df['host_id'].unique())
df['host_id'][df['host_since'] < '2010-01-01'].value_counts()

# Q4. Proportion of listings with missing ratings #
df.isna().sum()
df['review_scores_rating'].isna().mean().round(3)

# Q5. Distribution of the price #
df['price'].plot.hist(figsize=(8,6), color='gray', rwidth=0.98);
df['price'].describe()
df['price'][(df['price'] >= 25) & (df['price'] <= 150)].plot.hist(figsize=(8,6),
  color='gray', rwidth=0.94, bins=25);

# Q6. Average price per room type #
df.groupby(by='room_type')['price'].mean().round()
df.groupby(by='room_type')['price'].median().round()

# Q7. Top-10 neighbourhoods #
df['neighbourhood'].value_counts().head(10)
df.groupby(by='neighbourhood')['price'].agg(['count', 'median']).sort_values(by='count',
  ascending=False).head(10)
