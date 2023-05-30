# Cheatsheet - Pandas

## Methods for series

* `s.astype()`: changes the data type, if possible.

* `s.count()`: counts the non-missing terms of `s`.

* `s.cumsum()`: returns a series containing the cumulative sums of the terms of `s`.

* `s.describe()`: returns a series containing summary statistics. The `NaN` values are ignored.

* `s.diff()`: returns a series containing the differences between consecutive terms, with a `NaN` value on top.

* `s.drop_duplicates()`: removes the duplicated values `s`.

* `s.dropna()`: removes the missing values of `s`.

* `s.drop(lst)`: removes from `s` the values of a list.

* `s.dtype`: returns the data type.

* `s.duplicated()`: returns a Boolean series indicating duplicated values.

* `s.fillna(value)`: fills missing values with `value`.

* `s.head()`: returns the first terms of `s`

* `s.index`: returns the index of  `s`, as an object of type `Index` (not just one type, but a family). 

* `s.isna()`: returns a Boolean series indicating missing values.

* `s.max()`: returns the maximum of the terms of `s`.

* `s.mean()`: returns the mean of the terms of a numeric series.

* `s.min()`: returns the minimum of the terms of `s`.

* `s.pct_change()`: returns a series containing the proportion change between consecutive terms, with a `NaN` on top.

* `s.plot()`: the same as `s.plot.line()`.

* `s.plot.hist()`: histogram.

* `s.plot.line()`: line plot.

* `s.sample(n)`: extracts a random sample of size `n` of `s`, as a series. 

* `s.shape`: returns the length of the `s`.

* `s.shift(k)`: shifts `k` places the terms of `s`, filling the holes with `NaN`'s. `k` can be negative.

* `s.sort_index()`: sorts `s` by the index.

* `s.sort_values()`: sorts `s` by the values.

* `s.tail()`: returns the last terms of `s`.

* `s.to_frame()`: converts `s` to a data frame with one column.

* `s.sum()`: returns the sum of the terms of a numeric series.

* `s.value_counts()`: counts the unique values of `s`.

* `s.values`: returns an array with the same values as `s`.

### Methods for data frames

* `df1.append(df2)`: appends `df2` after the last row of `df1`. 

* `df.apply(func)`: aggregates the columns of `df` with the aggregation function `func`. It returns a series.

* `df.columns`: returns the column names of the data frame.

* `df.count()`: counts the rows that have a t least a non-missin term.

* `df.cumsum()`: retruns a data franme of the same shape as `df`, whose columns are the cumulative sums of those of `df`. For the string columns the sum is interpreted as concatenation.

* `df.describe()`: returns a data frame containing summary statistics of the numeric columns of `df`.

* `df.drop(lst)`: drops from  `df` the columns listed.

* `df.drop_duplicates()`: removes the duplicated rows of `df`.

* `df.dropna()`: removes the rows of `df` with missing values.

* `df.dtypes`: returns a series containing the column data types.

* `df.duplicated()`: returns a Boolean series indicating the duplicated rows.

* `df.fillna(value)`: fills the missing values of `df` with `value`.

* `df.head()`: returns the first rows of `df`.

* `df.index`: returns the index of  `df`, as an object of type `Index` (not just one type, but a family). 

* `df.info()`: returns a report of the contents of `df`.

* `df.isna()`: returns a Boolean data frame indicating missing values.

* `df.mean()`: returns the means of the numeric columns of `df`, as a series.

* `df.plot.bar(x, y)`: bar plot of (numeric) column `y` by (categorical) column `x`.

* `df.plot.scatter(x, y)`: scatter plot. The first column specified goes to the horizontal axis and rthe second one to the vertical axis. 

* `df.sample(n)`: extracts a random sample of `n` rowsof `df`, as a data frame.

* `df.set_index(col)`: sets the column `col` as the index. Returns a new data frame.

* `df.shape`: returns the numbers or rows and columns as a tuple.

* `df.sort_index()`: sorts the rows of `df` by the index.

* `df.sort_values(by=col)`: sorts the rows of `df` by the column `col`.

* `df.squeeze()`: converts a data frame with one column to a series.

* `df.sum()`: returns the column totals of `df`, as a series. For the string columns, it concatenates the values of the column entries.

* `df.tail()`: returns the last rows of `df`.

* `df.to_csv(file)`: exports data from `df` to CSV file `file`. If the file already exists, it overwrites the previous version.

* `df.values`: returns an array with the same values, coercing data types if needed.

## Pandas functions

* `pd.crosstab()`}: returns the cross tabulation of two or more data vectors, as a data frame.

* `pd.DataFrame(dict)`: returns a data frame whose columns are the elements of the dictionary `dict`.

* `pd.pivot_table()`: returns a 1-way or 2-way pivot table as a data frame.

* `pd.read_csv(file)`: imports data from the CSV file `file` to a data frame. 

* `pd.Series(v)`: returns a series terms are those of a vector-like object `v`.
