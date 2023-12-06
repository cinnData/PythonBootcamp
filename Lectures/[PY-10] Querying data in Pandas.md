# [PY-10] Querying data in Pandas

## Sorting

This last lecture presents a collection of basic procedures for cleaning, exploring and summarizing data stored in Pandas data frames. We start with **sorting** methods. A Pandas series can be sorted by the index or by the values, with the methods `.sort_index()` and `.sort_values()`, respectively. Both methods work for data frames, but, for the second one, you have to specify either the name of a column or a list of column names, which will then be used in the order that you wrote them.

The parameter `ascending` allows you to choose between ascending and descending ways. The default is `ascending=True`.

## Missing values

**Missing values** are denoted by `NaN` in Pandas. When a Pandas object is built, both Python's `None` and NumPy's `nan` are taken as `NaN`. Since `np.nan` has type `float`, numeric columns containing `NaN` values get type `float`. 

Three useful Pandas methods related to missing values, which can be applied to both series and data frames, are: 

* `.isna()` returns a Boolean Pandas object of the same shape, indicating which terms are missing.

* `.fillna(value)` fills missing values. 

* `.dropna()` removes the rows that contain at least one missing value. 

## Duplicates

There are two useful Pandas methods for managing **duplicates**:

* `.duplicated()` returns a Boolean series indicating the rows that are duplicated. The default of this method performs a top-down check of the data, returning `False` for the values occurring for the first time, and `True` for those having occurred before. You can reverse this with the argument `keep=last`.

* `.drop_duplicates()` drops the duplicated rows. It is based on the Boolean mask created by `.duplicated()`. 

## Grouping and aggregation

When exploring data, we often use tables for discovering patterns. They can be produced in various ways in Pandas:

* The method `.value_counts()` extracts a **frequency table**. The table contains the counts of the occurrences of every value of a given series. It does not include the missing values.

* The function `crosstab()` extracts a **cross tabulation**. For two series of the same length `s1` and `s2`, the syntax is `pd.crosstab(s1, s2)`. Then `s1` will be placed on the rows and `s2` on the columns. By default, `crosstab()` extracts a frequency table, unless an array of values (parameter `values`) and an **aggregate function** (parameter `aggfunc`) are passed.

* The function `pivot_table()` extracts a **spreadsheet-style pivot table**. For a Pandas data frame `df`, the syntax is `pd.pivot_table(df, values=col1, index=col2)`. This returns a **one-way table** containing the average value of the column `col1` for the groups defined by the column `col2`. Instead of the average, you can get a different summary by adding an argument `aggfunc=[f1, f2, ...]`. With an additional argument `columns=col3`, you get a **two-way table**. For two-way tables, this function works the same as `crosstab()`, but it can only be applied to columns from the same data frame.

* The method `.groupby()` groups the rows of a data frame so that an aggregate function can be applied to every group, extracting a **SQL-like table** as a data frame. The syntax is `df.groupby(by=col).f()`. To apply more than one function, use `df.groupby(by=col).agg([f1, f2, ...])`.
