## [PY-07] Introduction to Pandas ##

# The package Pandas #
import pandas as pd

# Pandas series #
s1 = pd.Series([2, 7, 14, 5, 9])
s1
s1.values
s1.index
s2 = pd.Series([1, 5, 'Messi'], index = ['a', 'b', 'c'])
s2
s2.index
s2.index[-2:]

# Pandas data frames #
df1 = pd.DataFrame({'v1': range(1, 6), 'v2': ['a', 'b', 'c', 'd', 'e'], 'v3': [-1.3, None, 2, 7, 0]})
df1
df1.values
df1.index
df1.columns
import numpy as np
arr = np.array([range(4), [9, 2.3, 7, 0]])
df2 = pd.DataFrame(arr)
df2.columns

# Exploring Pandas objects #
df1.head(2)
df1.info()
df1.describe()

# Subsetting data frames #
df1['v2']
df1[['v1', 'v2']]
df1[df1['v1'] > 2]
df1['v1'] > 2
df1[df1['v1'] > 2][['v1', 'v2']]
