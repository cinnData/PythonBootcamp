## Best restaurants in Barcelona according to TripAdvisor ##

# Q1. Importing the data #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/PythonBootcamp/main/Data/'
filename = path + 'trip.csv.zip'
df = pd.read_csv(filename, index_col=2)
df.info()
df.head()

# Q2a. Distribution of the number of reviews #
df['reviewCount'].plot.hist(figsize=(8,6), color='gray', rwidth=0.98);

# Q2b. Distribution of the number of photos #
df['photos'].plot.hist(figsize=(8,6), color='gray', rwidth=0.98);

# Q2c. Association #
df.plot.scatter(x='photos', y='reviewCount', figsize=(6,6), color='gray', s=5);
df['reviewCount'].corr(df['photos']).round(2)

# Q3. Proportion of reviews in English #
df['propEnglish'] = df['revEnglish']/df['reviewCount']
df['propEnglish'].plot.hist(figsize=(8,6), color='gray', rwidth=0.98);

# Q4. Price vs proportion of reviews in English #
df.groupby('priceRange')['propEnglish'].agg(['count', 'mean'])
pd.pivot_table(df, values='propEnglish', index='priceRange', aggfunc='mean')

# Q5a. Rank vs bubbles #
df['bubble'].value_counts()
pd.crosstab(df['rank'] <= 10, df['bubble'])
pd.crosstab(df['rank'] <= 30, df['bubble'])
pd.crosstab(df['rank'].between(31, 60), df['bubble'])

# Q5b. Rank vs number of reviews #
df['reviewCount'].plot.hist(figsize=(8,6), color='gray', rwidth=0.98);
df.plot.scatter(x='rank', y='reviewCount', figsize=(6,6), color='gray');

# Q6a. Special diets vs price #
df['diets'].value_counts()
df['hasdiets'] = ~df['diets'].isna()
pd.crosstab(df['hasdiets'], df['priceRange'])
pd.pivot_table(df, values='hasdiets', index='priceRange', aggfunc='mean')

# Q6b. Vegetarian diets vs price #
df['veget'] = df['diets'].str.contains('Vegetarian')
pd.crosstab(df['veget'], df['priceRange'])

# Q6c. Vegan diets vs price #
df['vegan'] = df['diets'].str.contains('Vegan')
pd.crosstab(df['vegan'], df['priceRange'])

# Q6d. Gluten free vs price #
df['gluten'] = df['diets'].str.contains('Gluten')
pd.crosstab(df['gluten'], df['priceRange'])


