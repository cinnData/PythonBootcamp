## [PY-08] Introduction to Pandas ##

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
height = [1.65, 1.73, 1.51, 1.63, 1.69, 1.7, 1.81, 1.66, 1.58, 1.66,
    1.62, 1.81, 1.75, 1.65, 1.65]
weight = [61.6, 59.5, 46.5, 75.3, 47.6, 80.2, 67.5, 64.1, 69.5, 57.0,
    68.6, 69.3, 53.2, 66.1, 50.6]
gender = ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'F', 'F', 'M', 'F', 'M',
    'F', 'M', 'M']
bio = pd.DataFrame({'height': height, 'weight': weight, 'gender': gender})
bio
bio.index
bio.values
bio.columns

# Exploring Pandas objects #
bio.shape
bio.head(2)
bio.info()
bio.describe()

# Subsetting data frames #
bio['height']
bio[['height', 'weight']]
bio['bmi'] = bio['weight']/bio['height']**2
bio
male = (bio['gender'] == 'M')
male
bio[male]
bio[male][['height', 'weight']]
