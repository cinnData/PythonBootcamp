## [PY-06] Introduction to Pandas ##

# The package Pandas #
import pandas as pd

# Pandas series #
s1 = pd.Series(arr1)
s1
s1.values
s1.index
s2 = pd.Series([1, 5, 'Messi'], index = ['a', 'b', 'c'])
s2
s2.index

# Pandas data frames #
df = pd.DataFrame({'v1': range(1, 6), 'v2': ['a', 'b', 'c', 'd', 'e'], 'v3': [-1.3, None, 2, 7, 0]})
df
df.values
df.index
df.columns
pd.DataFrame(arr2)
import numpy as np
arr = np.array([range(4), [9, 2.3, 7, 0]])
pd.DataFrame(arr)

# Exploring Pandas objects #
df.head(2)
df.info()
df.describe()

# Subsetting data frames #
df['v2']
df[['v1', 'v2']]
df[df['v1'] > 2]
df['v1'] > 2
df[df['v1'] > 2][['v1', 'v2']]