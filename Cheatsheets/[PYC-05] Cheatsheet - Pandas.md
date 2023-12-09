# [PYC-05] Cheatsheet - Pandas

## Attributes of a Pandas series

* `.dtype`: the data type.

* `.index`: the index, an object of type `Index` (not just a single type, but a family of types). 

* `.shape`: the shape. The same as for a 1D array.

* `.values`: a 1D array containing the values of the series.


## Methods for Pandas series

* `.astype()`: converts a series to a specified data type. Takes one positional argument, specifying the new data type, plus some some keyword arguments with less interest. The same as the NumPy method.

* `.count()`: counts the non-missing terms of a series. It has an uninteresting parameter.

* `.cumsum()`: calculates a series containing the cumulative sums of the terms of the original series. It takes some keyword arguments without interest. The same as the NumPy method. 

* `.describe()`: extracts a statistical summary, ignoring the `NaN` values. It applies to both numeric and string series, adapting the summary to the data type. It has some uninteresting parameters. 

* `.diff()`: calculates the differences between consecutive terms of a numeric series, inserting a `NaN` value on top. It has an uninteresting parameter.

* `.drop_duplicates()`: removes the duplicated values. It has some uninteresting parameter. 

* `.dropna()`: removes the missing values. It has an uninteresting parameter.

* `.drop(labels)`: removes terms of series. The parameter `labels` is a list of index labels. It has other parameters with less interest. 

* `.duplicated()`: returns a Boolean series indicating duplicated values. It has an uninteresting parameter.

* `.fillna(value)`: fills missing values. The parameter `value`, can be a single value, a dictionary, a series or a data frame. Other parameters allow for more sophistication. Don't use them unless you have a clear idea of what you are doing.

* `.head(n)`: returns the first terms of a series. The default is `n=5`. If `n`is negative, it returns all rows except the last ones.

* `.isna()`: returns a Boolean series indicating missing values. It takes zero arguments.

* `.max()`: returns the maximum of the terms of a series. It has some uninteresting parameters.

* `.mean()`: returns the mean of the terms of a numeric series. It has some uninteresting parameters.

* `.min()`: returns the minimum of the terms of a series. It has some uninteresting parameters.

* `.pct_change()`: returns a series with the proportion changes between consecutive terms, with a `NaN` on top. It has some uninteresting parameters.

* `.plot()`: the same as `s.plot.line()`.

* `.plot.hist()`: displays a histogram of a numeric series. It takes a keyword argument specifying the number of bins (default `bin=10`) and a collection of keyword arguments with graphical specifications (`title`, `xlabel`, `color`, etc).

* `.plot.line()`: displays a line plot of a numeric series. It takes a collection of keyword arguments with graphical specifications (`title`, `xlabel`, `color`, etc).

* `.sample(n)`: extracts a random sample of size `n` of a series. For sampling with replacement, use `replace=True`. Other parameters allow for more sophistication. 

* `.shift(periods)`: shifts the terms of a series as many places as specified by the parameter `periods`, filling the holes with `NaN` values. The parameter `periods` is an integer that can be negative. The default is `periods=1`.

* `.sort_index()`: sorts a series by the index labels. With `ascending=True`, switches to descending order. It has other parameters with less interest. 

* `.sort_values()`: sorts a series by its values. With `ascending=True`, switches to descending order. It has other parameters with less interest.

* `.tail(n)`: returns the last terms `n` of a series. The default is `n=5`. If `n`is negative, it returns all rows except the first ones.

* `.to_frame()`: converts a series to a data frame with one column. It has an uninteresting parameter.

* `.sum()`: returns the sum of the terms of a numeric series. It has some uninteresting parameters.

* `.value_counts()`: counts the unique values of a series. The defaults are `normalize=False` (change it to get proportions instead of counts), `sort=True` (change it to sort by index instead of by value), `ascending=False` (change it to get ascending order), `dropna=True` (change it to get `NaN` values also counted). There is another parameter with no interest.

## Functions for Pandas series

* `pd.crosstab(index, columns)`: cross tabulation of two or more vector-like objects of the same length. In the simplest version, the entries of the table are counts. Counts can be replaced by aggregate values, such as means or totals, by means of two additional parameters: `values`, a numeric vector-like object of the same length, and `aggfunc`, an aggregate function. They can also normalized in various ways, dividing by either row totals (`normalize=index`), column totals (`normalize=columns`) or the grand total (`normalize=all`). Margins can be added with `margins=True`. Other parameters have less interest.

* `pd.Series()`: converts a vector-like object to a Pandas series. The parameter `index` allows you to specify the index. The default `index=None` creates a `RangeIndex`. It has other parameters with less interest.

## Attributes of a Pandas data frame

* `.columns`: an Index object containing the names of the columns.

* `.dtypes`: a Pandas series containing the data types of the columns.

* `.index`: the index, an object of type `Index` (not just a single type, but a family of types). 

* `.shape`: the shape. The same as for a 1D array.

* `.values`: a 1D array containing the values of the series.

## Pandas methods for data frames

* `.apply(func, axis)`: applies a function by rows or by columns. The default is `axis=0` (by column). It has other parameters with less interest.

* `.count()`: the same as `.apply('count')`.

* `.cumsum()`: the same as `.apply('cumsum')`.

* `.describe()`: the default returns a statistical summary of the numeric columns. The parameter `include` allows you to include other types. It has two other parameters with less interest.

* `.drop(columns)`: drops a list of columns. It has other parameters that allow you to drop different parts of the data frame.

* `.drop_duplicates()`: removes duplicated rows. It has some ininteresting parameters.

* `.dropna()`: removes the rows with at least on missing value. It has some ininteresting parameters.

* `.duplicated()`: returns a Boolean series indicating the duplicated rows. It has some ininteresting parameters.

* `.groupby(by)`: splits a data frame based on the one column or a list of columns specified by the parameter `by`. Typically followed by an aggregation method, such as `.mean()` or `agg(['mean', 'count'])`. Other parameters have less interest.

* `.head(n)`: returns the first rows. The default is `n=5`. If `n`is negative, it returns all rows except the last ones.

* `.info()`: prints a concise summary of a data frame, including the index type, the number of index labels, the column names and the number of non-null entries in every column.

* `.isna()`: returns a Boolean data frame indicating missing values. It takes zero arguments.

* `.join(other)`: a simplified version of the method `.merge()`. The default is an left join based on the index. It is very practical in that case, because the parameter `other` can be a data frame, a series, or a list containing any combination of them. 

* `.mean()`: the same as `.apply('mean')`.

* `.merge(right)`: merges two data frames. The default is an inner join (to include the rows common to both tables) based on the columns that have the same name in the two data frames. A collection of parameters allow for various options.

* `.plot.bar(x, y)`: displays a vertical bar plot of a numeric column (`y`) by a categorical column (`x`). It takes a collection of keyword arguments with graphical specifications (`title`, `xlabel`, `color`, etc).

* `.plot.barh(x, y)`: displays a horizontal bar plot of a numeric column (`y`) by a categorical column (`x`). It takes a collection of keyword arguments with graphical specifications (`title`, `xlabel`, `color`, etc).

* `.plot.scatter(x, y)`: displays a scatter plot, with `x` in the horizontal axis and `y` in the vertical axis. It takes a collection of keyword arguments with graphical specifications (`title`, `xlabel`, `color`, etc).

* `.sample(n)`: extracts a random sample of `n` rows. For sampling with replacement, use `replace=True`. Other parameters allow for more sophistication. 

* `.set_index(keys)`: sets `keys` as the index. Typically, `keys` is the name of a column, which stops being a column, becoming the index. But Pandas makes room for more complexity. Also, other parameters allow for variations on the typical scheme.

* `.sort_index()`: sorts the rows by the index labels. With `ascending=True`, switches to descending order. It has other parameters with less interest.

* `.sort_values(by)`: sorts the rows by one column or a list of columns. With `ascending=True`, switches to descending order. It has other parameters with less interest.

* `.squeeze()`: converts a data frame with one column (or with one row, though this rare) to a series.

* `.sum()`: the same as `.apply('sum')`.

* `.tail(n)`: returns the last rows of a data frame. The default is `n=5`. If `n`is negative, it returns all rows except the first ones.

* `.to_csv(path_or_buf)`: exports data to a CSV file. Typically, `path_or_buf` is a string containing the path and the filename (except for files in the working directory). If the file already exists, the previous version is overwritten. The default is `index=True`, which includes the index as the first column of the file. You will often wish to avoid this.

## Other Pandas functions

* `pd.concat(objs)`: concatenates matching data frames. The parameter `objs` is a list of data frames. Pandas concatenation is not just pasting matrices.With `axis=0` (the default), the frames are concatenated vertically, based on the column names, inserting `NaN` to get a rectangular shape. With `axis=1`, it concatenates horizontally, which means a left join based on the index (the same as `.join()`).

* `pd.DataFrame(data)`: creates a data frame containing the data specified by the parameter `data`, which, in the most common version, is a dictionary whose values are the vector-like objects of the same length, which is converted to a data frame. The keys of the dictionary are taken as the column names. The parameters `index` and `columns` can be used to specify the index and the column names, respectively. Other parameters have less interest.

* `pd.merge()`: the same as `.merge()`. 

* `pd.pivot_table(data, values, index, columns, aggfunc)`: returns a spreadsheet-like pivot table. The same as `pd.crosstabs()`, but `values`, `index`, and `columns` are names of columns of the data frame `data`.

* `pd.read_csv(filepath_or_buffer)`: imports data from a CSV file to a data frame. Typically, `filepath_or_buffer` is a string containing the path and the filename (except for files in the working directory). Some of the many parameters of this function (`sep`, `header`, `names`, etc). The most relevant one is `index_col`, which specifies the column that you wish to use as the index, if that were the case (default `index_col=None`).
