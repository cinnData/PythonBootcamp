# [PY-06] Introduction to Pandas

## The package Pandas

**Pandas** is a library for managing data in tabular format, inspired in the language R, used by statisticians. There is a function in Pandas for practically everything that you may wish to do with your data. 

Pandas is typically imported as

```
In [1]: import pandas as pd
```

Pandas provides two data container classes, the series (one-dimensional) and the data frames (two-dimensional). A **series** can be understood as the combination of a 1D array containing the **values** and a list containing the names of the values, called the **index**. These components can be extracted as the attributes `values` and `index`.

A **data frame** can be seen as formed by one or several series with the same index (hence, with the same length). It can also be seen as a table for which the index provides the row names. In a Pandas data frame, each column has its own data type. The numeric types work as usual, but Pandas uses the data type `object` for many things, in particular for strings.

## Pandas series

Although it is not frequent in the real world practice, where the data are imported from external data files, a Pandas series can be created directly, for instance from an array, with the Pandas function `Series`:

```
In [2]: s1 = pd.Series(arr1)
    ...: s1
Out[2]:
0     2
1     7
2    14
3     5
4     9
dtype: int64
```

Now, the values of the series are extracted as:

```
In [3]: s1.values
Out[3]: array([ 2,  7, 14,  5,  9])
```

As shown above, when a series is printed, the index appears on the left. Since the index of `s1` has not been specified, a range of consecutive integers has been assigned as the index.

```
In [4]: s1.index
Out[4]: RangeIndex(start=0, stop=5, step=1)
```

Instead of an array, a list can be used to provide the values of a series. In the list, the items can have different type, but Pandas converts them to a common type, as shown in the following example. Here, instead of letting the Python kernel to create an index automatically, as a `RangeIndex`, we specify an index directly:

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

Indexes are useful for combining, filtering and joining data sets. There are many types of indexes, which allow for specific operations. So, do not look at the index as an embarrassment, which is what it seems at first sight, but as a tool for data management.

## Pandas data frames

A Pandas **data frame** can be built in many ways with the Pandas function `DataFrame`. For instance, from a dictionary of vector-like objects of the same length, as in the following example.

```
In [7]: df = pd.DataFrame({'v1': range(1, 6), 'v2': ['a', 'b', 'c', 'd', 'e'], 'v3': [-1.3, None, 2, 7, 0]})
   ...: df
Out[7]: 
   v1 v2   v3
0   1  a -1.3
1   2  b  NaN
2   3  c  2.0
3   4  d  7.0
4   5  e  0.0
```

As the series, the data frames have the attributes `values` and `index`.

```
In [8]: df.values
Out[8]: 
array([[1, 'a', -1.3],
       [2, 'b', nan],
       [3, 'c', 2.0],
       [4, 'd', 7.0],
       [5, 'e', 0.0]], dtype=object)
```

```
In [9]: df.index
Out[9]: RangeIndex(start=0, stop=5, step=1)
```

Note that all the terms in the data column have been converted to data type `float`. A column of a data frame must have a unique data type for all its terms. The data type reported for the whole data frame is a compromise among the data types of the columns, and does not matter in practice. Also, since the columns have different data types, `df.values` takes `object` type. Without a explicit specification, the index is automatically created as a `RangeIndex`. 

The third component of the data frame is a list with the column names, which can be extracted as the attribute `columns`.

```
In [10]: df.columns
Out[10]: Index(['v1', 'v2', 'v3'], dtype='object')
```

A data frame has the same shape of the array of values. Having rows and columns, a data frame looks like a 2D array with row and column names. Indeed, we can also create data frames in this way:

```
In [11]: import numpy as np

In [12]: arr = np.array([range(4), [9, 2.3, 7, 0]])

In [13]: pd.DataFrame(arr)
Out[13]: 
     0    1    2    3
0  0.0  1.0  2.0  3.0
1  9.0  2.3  7.0  0.0
```

Data frames can also be extracted from a data source (local or remote), such as a CSV file, an Excel sheet, or a table from a relational database. As for the series, a range index is automatically created unless an alternative specification is provided. The same is true for column names, so, in the above example, the column names are a range of integers. It is recommended to choose a column name which suggests the content of the column.

## Exploring Pandas objects

The methods `head` and `tail` extract the first and the last rows of a data frame, respectively. The default number of rows extracted is 5, but you can pass a custom number.

```
In [14]: df.head(2)
Out[14]: 
   v1 v2   v3
0   1  a -1.3
1   2  b  NaN
```

The content of a data frame can also be explored with the method `info`. It reports the dimensions, the data type and the number of non-missing values of every column of the data frame. Note that the data type of the second column, for which you would have expected `str`, is reported as `object`. Don't worry about this, you can apply the string methods to this column, as will be seen later in this course.

```

In [15]: df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   v1      5 non-null      int64  
 1   v2      5 non-null      object 
 2   v3      4 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 248.0+ bytes
```

The method `describe` extracts a conventional statistical summary of a Pandas object. The columns of type `object` are omitted, except when all the columns have that type. In that case, the report contains only counts. 

```
In [16]: df.describe()
Out[16]: 
             v1        v3
count  5.000000  4.000000
mean   3.000000  1.925000
std    1.581139  3.645431
min    1.000000 -1.300000
25%    2.000000 -0.325000
50%    3.000000  1.000000
75%    4.000000  3.250000
max    5.000000  7.000000
```

## Subsetting data frames

Pandas offers multiple ways for subsetting data frames. First, you can extract a column, as a series:

```
In [17]: df['v2']
Out[17]:
0    a
1    b
2    c
3    d
4    e
Name: v2, dtype: object
````

Note that the syntax is the same as for extracting the value of a key from a dictionary (not by chance). You can also extract a **data subaframe** containing a subset of complete columns from a data frame. You can specify this with a list containing the names of those columns:

```
In [18]: df[['v1', 'v2']]
Out[18]:
   v1 v2
0   0  a
1   1  b
2   2  c
3   3  d
4   4  e
```

*Note*. You can extract a subframe with a single column. Beware that this is not the same as a series. `df['v2']`is a series with shape `(5,)`, and `df[['v2']]` is a data frame with shape `(5,1)`.

In practical data analysis, rows are typically filtered by expressions. Boolean masks can be created with the columns of a data frame just as if they were 1D arrays. A simple example follows. 

```
In [19]: df[df['v1'] > 2]
Out[19]: 
   v1 v2   v3
2   3  c  2.0
3   4  d  7.0
4   5  e  0.0
```

Note that `df['v1'] > 2`  is a series of data type `bool`:

```
In [20]: df['v1'] > 2
Out[20]: 
0    False
1    False
2     True
3     True
4     True
Name: v1, dtype: bool
```

See next how to combine a row filter and a column selection. Yopu can change the order, selecting first the columns and then filtering the rows. 

```
In [21]: df[df['v1'] > 2][['v1', 'v2']]
Out[21]: 
   v1 v2
2   3  c
3   4  d
4   5  e
```

Besides this, there are two additional ways to carry out a selection, specifying rows and columns in one shot:

* **Selection by label** is specified by adding  `.loc` after the name of the data frame. The selection of the rows is based on the index, and that of the columns is based on the column names.

* **Selection by position** uses `.iloc`. The selection of the rows is based on the row number and that of the columns on the column number.

In both cases, if you enter a single specification inside the brackets, it refers to the rows. If you enter two specifications, the first one refers to the rows and the second one to the columns. We don't use `loc` and `iloc` in this course, since you can live in Pandas without that, first filtering the rows and then selecting the columns. Sticking to this simple approach, you will save the time wasted learning too many methods.
