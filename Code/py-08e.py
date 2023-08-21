## [PY-08E] Example - Apple Inc. stock prices ##

# Q1. Import the data (edit the path) #
import pandas as pd
df = pd.read_csv('aapl.csv')

# Q2. Check the contens of the data set #
df.shape
df.info()
df.head()
df.tail()
df

# Q3. Data previous to January 15th #
df[df['date'] < '2022-01-15']

# Q4. Line plot for the opening price #
df['open'].plot(figsize=(10,6), color='black', linewidth=1);

Q5a. Line plot for the trading volume #
df['volume'] = df['volume']/10**6
df['volume'].plot(figsize=(10,6), color='black', linewidth=1);

# Q5b. Histogram for the trading volume #
df['volume'].plot.hist(figsize=(8,6), color='gray', rwidth=0.98);

# Q6a. Daily variation #
df['dvar'] = df['high'] - df['low']
df

# Q6b. Line plot for the daily variation #
df['dvar'].plot(figsize=(10,6), color='black', linewidth=1);

# Q6c. Histogram for the daily variation #
df['dvar'].plot.hist(figsize=(8,6), color='gray', rwidth=0.98);

# Q7a. Scatter plot for the daily price variation and the trading volume # 
df.plot.scatter(x='volume', y='dvar', figsize=(6,6), color='gray');

## Q7. Correlation #
df['volume'].corr(df['dvar'])
df['volume'].corr(df['dvar']).round(2)
