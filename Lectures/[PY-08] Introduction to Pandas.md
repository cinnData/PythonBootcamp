# [PY-08] Introduction to Pandas

## The package Pandas

**Pandas** is a library for managing data in tabular format, inspired in the statistical language R. It is not a simple toolkit, but a huge collection of functions and methods, covering practically anything that you may wish to do with data, often in multiple ways. Therefore, rather than on "learning Pandas", you should think on "using Pandas", learning on the way (maybe no more than what you need). 

This lecture, and the short tutorial contained, are just introductory. The two last lectures of the course present more advanced stuff, such as cleaning data sets, missing values, grouping and aggregating, basic stats, and plotting. Real data will be provided in separate examples.

Pandas is typically imported as:

```
In [1]: import pandas as pd
```

Pandas provides two data container classes, the series (one-dimensional) and the data frame (two-dimensional). A **series** is like a vector whose terms have names, while a **data frame** is like a table with row and column names. These classes address two shortcomings of NumPy arrays: (a) rows and, specially columns, don't have names, (b) there is a unique data type.

A **series** has two components: a 1D array containing the **values** and a list containing **labels** for those values, called the **index**. These components can be extracted as the attributes `.values` and `.index`. A **data frame** has a third component, a list containing the **column names**, that can be extracted as the attribute `.columns`. The series has a data type, but the data frame does not. Instead, each column has its own data type. The numeric types work as usual, but Pandas uses the data type `object` for various things, in particular for strings.

## Pandas series

Although it is not frequent in the real world practice, where the data are imported from external data files, a Pandas series can be created directly with the Pandas function `Series()`. The data can be taken from a vector-like object such as a list or a 1D array.

```
In [2]: s1 = pd.Series([2, 7, 14, 5, 9])
   ...: s1
Out[2]:
0     2
1     7
2    14
3     5
4     9
dtype: int64
```

Now, the values of the series are extracted as a 1D array:

```
In [3]: s1.values
Out[3]: array([ 2,  7, 14,  5,  9])
```

As shown above, when a series is printed, the index appears on the left. Since the index of `s1` has not been specified, a range of consecutive integers has been assigned to the index.

```
In [4]: s1.index
Out[4]: RangeIndex(start=0, stop=5, step=1)
``` 

When the data source mixes data types, a conversion to a common type is performed on the fly, as shown in the following example. Here, instead of letting the Python kernel to create an index automatically, as a `RangeIndex`, we provide an index directly:

```
In [5]: s2 = pd.Series([1, 5, 'Messi'], index = ['a', 'b', 'c'])
   ...: s2
Out[5]:
a        1
b        5
c    Messi
dtype: object
```

Now the index is a plain `Index`:

```
In [6]: s2.index
Out[6]: Index(['a', 'b', 'c'], dtype='object')
```

Altough they are not the same thing, for many purposes a `RangeIndex` object works like a range, and an `Index` object works like a list. For instance, for slicing:

```
In [7]: s2.index[-2:]
Out[7]: Index(['b', 'c'], dtype='object')
```

Though Pandas allows duplicates in an index, good indexes should not have them, so rows can be identified by the index value. Indexes are useful for **filtering** and **joining** data sets. There are many types of indexes, which allow for specific operations. So, do not look at the index as an embarrassment, which is what it seems at first sight, but as a tool for data management.

## Pandas data frames

A Pandas **data frame** can be built in many ways with the Pandas function `DataFrame()`. For instance, from a dictionary of vector-like objects of the same length (including Pandas series). As an example, we revisit the biometric data used in the preceding lecture. We started with three lists, containing heights, weights and genders, respectively.

```
In [8]: height = [1.65, 1.73, 1.51, 1.63, 1.69, 1.7, 1.81, 1.66, 1.58, 1.66,
   ...:     1.62, 1.81, 1.75, 1.65, 1.65]
   ...: weight = [61.6, 59.5, 46.5, 75.3, 47.6, 80.2, 67.5, 64.1, 69.5, 57.0,
   ...:     68.6, 69.3, 53.2, 66.1, 50.6]
   ...: gender = ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'F', 'F', 'M', 'F', 'M',
   ...:     'F', 'M', 'M']
```

Now, we pack these lists as a data frame:

```
In [9]: bio = pd.DataFrame({'height': height, 'weight': weight, 'gender': gender})
   ...: bio
Out[9]: 
    height  weight gender
0     1.65    61.6      M
1     1.73    59.5      M
2     1.51    46.5      F
3     1.63    75.3      F
4     1.69    47.6      M
5     1.70    80.2      F
6     1.81    67.5      M
7     1.66    64.1      F
8     1.58    69.5      F
9     1.66    57.0      M
10    1.62    68.6      F
11    1.81    69.3      M
12    1.75    53.2      F
13    1.65    66.1      M
14    1.65    50.6      M
```

Note that here, `height` was a list, while `'height'` is the name that we give to the first column in the new data frame. We could have chosen a different name. The same for the other two columns. 

The index is printed on the left, as for a series. Without an explicit specification, the index is automatically created as a range index. 

```
In [10]: bio.index
Out[10]: RangeIndex(start=0, stop=15, step=1)
```

The values come as 2D array. The data type reported for the whole data frame is a compromise among the data types of the columns, and does not matter in practice. Here, since the columns have different data types, `bio.values` takes type `object`. 

```
In [11]: bio.values
Out[11]: 
array([[1.65, 61.6, 'M'],
       [1.73, 59.5, 'M'],
       [1.51, 46.5, 'F'],
       [1.63, 75.3, 'F'],
       [1.69, 47.6, 'M'],
       [1.7, 80.2, 'F'],
       [1.81, 67.5, 'M'],
       [1.66, 64.1, 'F'],
       [1.58, 69.5, 'F'],
       [1.66, 57.0, 'M'],
       [1.62, 68.6, 'F'],
       [1.81, 69.3, 'M'],
       [1.75, 53.2, 'F'],
       [1.65, 66.1, 'M'],
       [1.65, 50.6, 'M']], dtype=object)
``` 

The third component of the data frame is an `index` object containing the column names, which can be extracted as the attribute `.columns`.

```
In [12]: bio.columns
Out[12]: Index(['height', 'weight', 'gender'], dtype='object')
```

Data frames can also be extracted from a data source (local or remote), such as a CSV file, an Excel sheet, or a table from a relational database. Irrespective of the type of source used, a range index is automatically created unless an alternative specification is provided. One of the columns of the source is often taken as the index.

## Exploring Pandas objects

A data frame has the same **shape** of the array of values. 

```
In [13]: bio.shape
Out[13]: (15, 3)
```

The methods `.head()` and `.tail()` extract the first and the last rows of a data frame, respectively. The default number of rows extracted is 5, but you can pass a custom number.

```
In [14]: bio.head(2)
Out[14]: 
   height  weight gender
0    1.65    61.6      M
1    1.73    59.5      M
```

The content of a data frame can also be explored with the method `.info()`. It prints a report containing the dimensions, the data type and the number of non-missing values of every column of the data frame. Note that the data type of the third column, for which you would have expected `str`, is reported as `object`. Don't worry about this, you could apply the string methods to this column.

```
In [15]: bio.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 15 entries, 0 to 14
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   height  15 non-null     float64
 1   weight  15 non-null     float64
 2   gender  15 non-null     object 
dtypes: float64(2), object(1)
memory usage: 492.0+ bytes
```

The method `.describe()` prints a statistical summary of a Pandas object. The columns of type `object` are omitted, except when all the columns have that type. In that case, the summary contains only counts. 

```
In [16]: bio.describe()
Out[16]: 
          height     weight
count  15.000000  15.000000
mean    1.673333  62.440000
std     0.079970   9.986477
min     1.510000  46.500000
25%     1.640000  55.100000
50%     1.660000  64.100000
75%     1.715000  68.950000
max     1.810000  80.200000
```

## Subsetting data frames

Pandas offers multiple ways for subsetting data frames. First, you can extract a column, as a series:

```
In [17]: bio['height']
Out[17]: 
0     1.65
1     1.73
2     1.51
3     1.63
4     1.69
5     1.70
6     1.81
7     1.66
8     1.58
9     1.66
10    1.62
11    1.81
12    1.75
13    1.65
14    1.65
Name: height, dtype: float64

````

Note that the syntax is the same as for extracting the value of a key from a dictionary (not by chance). You can also extract a **data subframe** containing a subset of complete columns from a data frame. You can specify this with a list containing the names of those columns:

```
In [18]: bio[['height', 'weight']]
Out[18]: 
    height  weight
0     1.65    61.6
1     1.73    59.5
2     1.51    46.5
3     1.63    75.3
4     1.69    47.6
5     1.70    80.2
6     1.81    67.5
7     1.66    64.1
8     1.58    69.5
9     1.66    57.0
10    1.62    68.6
11    1.81    69.3
12    1.75    53.2
13    1.65    66.1
14    1.65    50.6
```

*Note*. You can extract a data subframe with a single column. Beware that this is not the same as a series. `bio['height']`is a series with shape `(15,)`, and `bio[['height']]` is a data frame with shape `(15,1)`. We have seen something similar in lists.

The good news from Pandas is that we can operate with columns as if they were 1D arrays, but now we can add the result as an new column:

```
In [19]: bio['bmi'] = bio['weight']/bio['height']**2
    ...: bio
Out[19]: 
    height  weight gender        bmi
0     1.65    61.6      M  22.626263
1     1.73    59.5      M  19.880384
2     1.51    46.5      F  20.393842
3     1.63    75.3      F  28.341300
4     1.69    47.6      M  16.666083
5     1.70    80.2      F  27.750865
6     1.81    67.5      M  20.603767
7     1.66    64.1      F  23.261722
8     1.58    69.5      F  27.840090
9     1.66    57.0      M  20.685150
10    1.62    68.6      F  26.139308
11    1.81    69.3      M  21.153200
12    1.75    53.2      F  17.371429
13    1.65    66.1      M  24.279155
14    1.65    50.6      M  18.585859
```

In practical data analysis, rows are typically filtered by means of expressions. A Boolean mask can be created with an expression involving columns of a data frame just as for NumPy arrays. A simple example follows. 

```
In [20]: male = (bio['gender'] == 'M')
    ...: male
Out[20]: 
0      True
1      True
2     False
3     False
4      True
5     False
6      True
7     False
8     False
9      True
10    False
11     True
12    False
13     True
14     True
Name: gender, dtype: bool
```

Note that `male` is a (separate) series of data type `bool`. We could also add it to `bio` as a column, or make it a 1/0 **dummy** (just add `+ 0` at the end of the definition). Also, note that the parenthesis in the definition is not needed, though it is good practice to enclose expressions for readability. 

```
In [21]: bio[male]
Out[21]: 
    height  weight gender        bmi
0     1.65    61.6      M  22.626263
1     1.73    59.5      M  19.880384
4     1.69    47.6      M  16.666083
6     1.81    67.5      M  20.603767
9     1.66    57.0      M  20.685150
11    1.81    69.3      M  21.153200
13    1.65    66.1      M  24.279155
14    1.65    50.6      M  18.585859
```

See next how to combine a row filter and a column selection. You can change the order, selecting first the columns and then filtering the rows. 

```
In [22]: bio[male][['height', 'weight']]
Out[22]: 
    height  weight
0     1.65    61.6
1     1.73    59.5
4     1.69    47.6
6     1.81    67.5
9     1.66    57.0
11    1.81    69.3
13    1.65    66.1
14    1.65    50.6
```

Besides this, there are two additional ways to carry out a selection, specifying rows and columns in one shot:

* **Selection by label** is specified by adding  `.loc` after the name of the data frame. The selection of the rows is based on the index, and that of the columns is based on the column names.

* **Selection by position** uses `.iloc`, which works exactly as in 2D array, based on the row and column indexes. 

In both cases, if you enter a single specification inside the brackets, it refers to the rows. If you enter two specifications, the first one refers to the rows and the second one to the columns. We don't use `loc` and `iloc` in this course, since you can live in Pandas without that, first filtering the rows and then selecting the columns (or vice versa). Sticking to this simple approach, you save the time wasted learning too many methods.

## Homework

1. Replace the first item of the list `weight` by `None` and recalculate the data frame `bio`. Can you explain all the changes?

2. In this new version, split the data in two parts, using `bio['weight'] <= 67` and `bio['weight'] > 67`. What happened with the first row?
