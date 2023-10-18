## [PY-08E] Example - Apple Inc. stock prices ##

# Import the data (edit the path) #
import pandas as pd
%pwd
df = pd.read_csv('Dropbox/py_course/data/aapl.csv')

# Exploring the data #
df.info()
df.head()
df.describe()

# Q1. Data previous to January 15th #
df[df['date'] < '2022-01-15']

# Q2. Line plot for the opening price #
df['open'].plot(figsize=(10,6), color='black', linewidth=1);

Q3a. Line plot for the trading volume #
df['volume'] = df['volume']/10**6
df['volume'].plot(figsize=(10,6), color='black', linewidth=1);

# Q3b. Histogram for the trading volume #
df['volume'].plot.hist(figsize=(8,6), color='gray', edgecolor='white');

# Q4a. Daily variation #
df['dvar'] = df['high'] - df['low']
df.head()

# Q4b. Line plot for the daily variation #
df['dvar'].plot(figsize=(10,6), color='black', linewidth=1);

# Q4c. Histogram for the daily variation #
df['dvar'].plot.hist(figsize=(8,6), color='gray', edgecolor='white');

# Q5a. Scatter plot for the daily price variation and the trading volume # 
df.plot.scatter(x='volume', y='dvar', figsize=(6,6), color='gray');

## Q5b. Correlation #
df['volume'].corr(df['dvar'])
df['volume'].corr(df['dvar']).round(2)
