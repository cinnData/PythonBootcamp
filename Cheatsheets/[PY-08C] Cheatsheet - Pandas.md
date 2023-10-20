# [PY-08C] Cheatsheet - Pandas

## Attributes of a Pandas series

* `.dtype`: the data type.

* `.index`: the index, an object of type `Index` (not just a single type, but a family of types). 

* `.shape`: the shape. The same as for a 1D array.

* `.values`: a 1D array containing the values of the series.


## Methods for Pandas series

* `.astype()`: converts a series to a specified data type. Takes one positional argument, specifying the new data type, plus some some keyword arguments whose default you will never change. The same as the NumPy method.

* `.count()`: counts the non-missing terms of a series. It takes a keyword argument whose default you will never change.

* `.cumsum()`: calculates a series containing the cumulative sums of the terms of the original series. It takes some keyword arguments whose default you will never change. The same as the NumPy method. 

* `.describe()`: extracts a statistical summary, ignoring the `NaN` values. It applies to both numeric and string series, adapting the summary to the data type. It takes some keyword arguments whose default you will never change. 

* `.diff()`: calculates the differences between consecutive terms of a numeric series, inserting a `NaN` value on top. It takes a keyword argument whose default you will never change.

* `.drop_duplicates()`: removes the duplicated values. It takes some keyword arguments whose default you will rarely change. 

* `.dropna()`: removes the missing values. It takes a keyword argument whose default you will never change.

* `.drop(labels)`: removes the terms whose index value are included in the list `labels`. Besides this parameter, it has other parameters whose default you will never change. 

* `.duplicated()`: returns a Boolean series indicating duplicated values. It also takes an argument whose default you will never change.

* `.fillna(value)`: fills missing values. The parameter `value`, besides a single value, can also be a dictionary, a series or a data frame, allowing for sophistication in the filling process. Other parameters allow for even more sophistication. Don't use them unless you have a clear idea of what you are doing.

* `.head(n)`: returns the first terms of a series. The default is `n=5`. If `n`is negative, it returns all rows except the last ones.

* `.isna()`: returns a Boolean series indicating missing values. It takes zero arguments.

* `.max()`: returns the maximum of the terms of a series. It takes some keyword arguments whose default you will never change.

* `.mean()`: returns the mean of the terms of a numeric series. It takes some keyword arguments whose default you will never change.

* `.min()`: returns the minimum of the terms of a series. It takes some keyword arguments whose default you will never change.

* `.pct_change()`: returns a series with the proportion changes between consecutive terms, with a `NaN` on top. It takes some keyword arguments whose default you will never change.

* `.plot()`: the same as `s.plot.line()`.

* `.plot.hist()`: displays a histogram of a numeric series. It takes a keyword argument specifying the number of bins (default `bin=10`) and a collection of keyword arguments with graphical specifications (`title`, `xlabel`, `color`, etc).

* `.plot.line()`: displays a line plot of a numeric series. It takes a collection of keyword arguments with graphical specifications (`title`, `xlabel`, `color`, etc).

* `.sample(n)`: extracts a random sample of size `n` of a series. For sampling with replacement, use `replace=True`. Other parameters allow for more sophistication. 

* `.shift(periods)`: shifts the terms of a series as many places as specified by the parameter `periods`, filling the holes with `NaN` values. `periods` can be negative.

* `.sort_index()`: sorts a series by the index labels. It takes a collection of keyword arguments whose default you will not change, except `ascending=True`, that you may will to change to get descending order.

* `.sort_values()`: sorts a series by its values. It takes a collection of keyword arguments whose default you will not change, except `ascending=True`, that you may will to change to get descending order.

* `.tail(n)`: returns the last terms `n` of a series. The default is `n=5`. If `n`is negative, it returns all rows except the first ones.

* `.to_frame()`: converts a series to a data frame with one column. It takes a keyword argument whose default you will never change.

* `.sum()`: returns the sum of the terms of a numeric series. It takes some keyword arguments whose default you will never change.

* `.value_counts()`: counts the unique values of a series. The defaults are `normalize=False` (you change this to get proportions instead of counts), `sort=True` (you change this to sort by index instead of by value), `ascending=False` (you change this to get ascending order), `dropna=True` (you change this to get `NaN` also counted). There is another parameter that you will never use.

## Functions for Pandas series

* `pd.crosstab(index, columns)`: cross tabulation of two or more vector-like objects of the same length. In the simplest version, the entries of the table are counts. Counts can be replaced by aggregate values, such as means or totals, by specifying a numeric vector-like object of the same length as the parameter `values` and an aggregating function as `aggfunc`. They can also normalized in various ways, dividing by either row totals (`normalize=index`), column totals (`normalize=columns`) or the grand total (`normalize=all`). Margins can be added with `margins=True`. Other parameters have less interest.

* `pd.Series()`: converts a vector-like object to a Pandas series. The parameter `index` allows you to specify the index. The default `index=None` creates a `RangeIndex`. It takes some other keyword arguments whose default you will never change.

## Attributes of a Pandas data frame

* `.columns`: an Index object containing the names of the columns.

* `.dtypes`: a Pandas series containing the data types of the columns.

* `.index`: the index, an object of type `Index` (not just a single type, but a family of types). 

* `.shape`: the shape. The same as for a 1D array.

* `.values`: a 1D array containing the values of the series.

## Pandas methods for data frames

* `.apply(func)`: the default (`axis=0`) applies the function `func` by columns. With `axis=1`, the function is applied by rows. It has other parameters whose defaults you will not change.

* `.count()`: the default (`axis=0`) counts the non-missing term for each column. With `axis=1`, the counts are done for each row. The same as `.apply('count')`. It has another parameter which you will not use.

* `.cumsum()`: the default (`axis=0`) replaces each columns by the corresponding cumulative sums. For the string columns the sum is interpreted as concatenation. With `axis=1`, the cumulative sums are calculated by row, but this rarely works, because columns have different data types. Missing values are ignored, unless you specify `skipna=False`.

* `.describe()`: the default returns a statistical summary of the numeric columns. The parameter `include` allows you to include other types. It has two other parameters with less interest.

* `.drop(columns)`: drops a list of columns. It has other parameters that allow you to drop different parts of the data frame.

* `.drop_duplicates()`: removes duplicated rows. It takes some keyword arguments whose defaults you will rarely change.

* `.dropna()`: removes the rows with at least on missing value. It takes some keyword arguments whose defaults you will rarely change.

* `.duplicated()`: returns a Boolean series indicating the duplicated rows. It takes some keyword arguments whose defaults you will rarely change.

* `.fillna(value)`: fills missing values. The parameter `value`, besides a single value, can also be a dictionary, a series or a data frame, allowing for sophistication in the filling process. Other parameters allow for even more sophistication. Don't use them unless you have a clear idea of what you are doing.

* `.head(n)`: returns the first rows. The default is `n=5`. If `n`is negative, it returns all rows except the last ones.

* `.info()`: prints a concise summary of a data frame, including the index dtype and columns, non-null values and memory usage.

* `.isna()`: returns a Boolean data frame indicating missing values. It takes zero arguments.

* `.join(other)`: a simplified version of the method `.merge()`. The merger is based on the index. It is very practical in that case, because the parameter `other` camn be a data frame, a series, or a list containing any combination of them. 

* `.mean()`: returns the means of the columns (the default, with `axis=0`), of the rows (with `axis=1`) or of the whole data frame (`axis=None`). Missing values are ignored, unless you specify `skipna=False`. What to do with the non-numeric columns is specified by the parameter `numeric_only`, whose default has recently changed.

* `.merge(right)`: merges two data frames. The default is an inner join (to include the rows common to both tables) based on the columns that have the same name in the two data frames. A collection of parameters allow for various options.

* `.plot.bar(x, y)`: displays a vertical bar plot of a numeric column (`y`) by a categorical column (`x`). It takes a collection of keyword arguments with graphical specifications (`title`, `xlabel`, `color`, etc).

* `.plot.barh(x, y)`: displays a horizontal bar plot of a numeric column (`y`) by a categorical column (`x`). It takes a collection of keyword arguments with graphical specifications (`title`, `xlabel`, `color`, etc).

* `.plot.scatter(x, y)`: displays a scatter plot, with `x` in the horizontal axis and `y` in the vertical axis. It takes a collection of keyword arguments with graphical specifications (`title`, `xlabel`, `color`, etc).

* `.sample(n)`: extracts a random sample of `n` rows. For sampling with replacement, use `replace=True`. Other parameters allow for more sophistication. 

* `.set_index(keys)`: sets `keys` as the index. Typically, `keys` is the name of a column, which stops being a column, becoming the index. But Pandas makes room for more complexity. Also, other parameters allow for variations on the typical scheme.

* `.sort_index()`: sorts the rows by the index labels. It takes a collection of keyword arguments whose default you will not change, except `ascending=True`, that you may will to change to get descending order.

* `.sort_values(by)`: sorts the rows by one column or a list of columns. It takes a collection of keyword arguments whose default you will not change, except `ascending=True`, that you may will to change to get descending order.

* `.squeeze()`: converts a data frame with one column (or with one row, though this rare) to a series.

* `.sum()`: returns the column totals (the default, with `axis=0`), the row totals (with `axis=1`) or the grand total (`axis=None`). Missing values are ignored, unless you specify `skipna=False`. For the string columns the sum is interpreted as concatenation. Summing by rows, you probably have to specify what to do with non-numeric columns. The parameter `numeric_only`, whose default has recently changed, allows you manage that.

* `.tail(n)`: returns the last rows of a data frame. The default is `n=5`. If `n`is negative, it returns all rows except the first ones.

* `.to_csv(path_or_buf)`: exports data to a CSV file. Typically, `path_or_buf` is a string containing the path and the filename (except for files in the working directory). If the file already exists, the previous version is overwritten. The default is `index=True`, which includes the index as the first column of the file. You will often wish to avoid this.

## Other Pandas functions

* `pd.concat(lst)`: concatenates the data frames specified. With `axis=0` (the default), the frames are concatenated vertically. With `axis=1`, horizontally. Horizontal concatenation is not just pasting the two matrices together, but a join based on the index (the same as `.join()`).

* `pd.DataFrame(data)`: in the most common version, `data` is a dictionary whose values are the vector-like objects of the same length, which is converted to a data frame. The keys of the dictionary are taken as the column names. The parameters `index` and `columns` can be used to specify the index and the column names, respectively. Other parameters have less interest.

* `pd.pivot_table(data, values, index, columns, aggfunc)`: returns a spreadsheet pivot table. The same as `pd.crosstabs()`, but `values`, `index`, and `columns` are names of columns of the data frame `data`.

* `pd.read_csv(filepath_or_buffer)`: imports data from a CSV file to a data frame. Typically, `filepath_or_buffer` is a string containing the path and the filename (except for files in the working directory). Some of the many parameters of this function (`sep`, `header`, `names`, etc). The most relevant one is `index_col`, which specifies the column that you wish to use as the index, if that were the case (default `index_col=None`).

