# [PY-08] Querying data in Pandas

## Sorting

Thsi last lecture presents a collection of basic procedures for cleaning, exploring and summarizing data stored in Pandas data frames. We start with **sorting** methods. Pandas series can be sorted by the index or by the values, with the methods `.sort_index()` and `.sort_values()`, respectively. Both work for data frames, but, for the second one, you have to specify either the name of a column or a list of column names, which will then be used in the order that you wrote them.

The parameter `ascending` allows you to choose between ascending and descending ways. The default (in Python as in other languages) is `ascending=True`.

## Missing values

**Missing values** are denoted by `NaN` in Pandas. When a Pandas object is built, both Python's `None` and NumPy's `nan` are taken as `NaN`. Since `np.nan` has type `float`, numeric columns containing `NaN` values get type `float`. 

Three useful Pandas methods related to missing values, which can be applied to both series and data frames, are: 

* `.isna()` returns a Boolean mask indicating which terms are missing.

* `.fillna()` is used for replacing `NaN`'s by a fixed value, set by the user.

* `.dropna()` returns the same data set minus the rows that contain at least one missing value. 

## Duplicates

There are two useful Pandas methods for managing **duplicates**:

* `.duplicated()` returns a Boolean series indicating the rows which are duplicated. The default is `keep=first`, meaning that, when a row is repeated, all the appearances except the first one are considered duplicated.

* `.drop_duplicates()` drops the duplicated entries rows. It is based on the Boolean mask created by `.duplicated()`. 

## Grouping and aggregation

When exploring data, we often use tables for discovering patterns. They can be produced in various ways in Pandas:

* The method `.value_counts()` extracts a **frequency table** as a series. The table contains the counts of the occurrences of every value of a given series. It does not include the missing values.

* The function `crosstab()` extracts a **cross tabulation** as a Pandas data frame. For two series of the same length `s1` and `s2`, the syntax is `pd.crosstab(s1, s2)`. Then `s1` will be placed on the rows and `s2` on the columns. By default, `crosstab()` extracts a frequency table, unless an array of values and an **aggregation function** are passed, *e.g*. as `values=s3` and `aggfunc=fname`.

* The function `pivot_table()` extracts a **spreadsheet-style pivot table** as a data frame. For a Pandas data frame `df`, the syntax is `pd.pivot_table(df, values=cname1, index=cname2)`. This returns a one-way table containing the average value of the column `cname1` for the groups defined by the column `cname2`. Instead of the average, you can get a different summary by adding an argument `aggfunc=[fname1, fname2, ...]`. With an additional argument `columns=cname3`, you get a two-way table. For two-way tables, it works the same as `crosstab()`, but it only applies to columns from the same data frame.

* The method `groupby()` groups the rows of a data frame so that an **aggregation function** can be applied to every group, extracting a **SQL-like table** as a data frame. The syntax is `df.groupby(by=cname).fname()`. To apply more than one aggregation function, use `df.groupby(by=cname).agg([fname1, fname2, ...])`.

## Joins and unions

**Joins** and **unions** are typical operations for combinaing tables in SQL databases, available in Pandas: 

* The method `.merge()` joins two dataframes based on common columns. When the name of the shared columns is the same in both data frames, an inner join can be performed with the basic syntax `df1.merge(df2)`. This is called a **natural join** in SQL. Additional arguments make room for variations, like outer joins or different names for common columns.

* The function `concat()` takes a list of data frames with the same names (but not necessarily in the same order) and returns their union, that is, a data frame containing all the rows from the original data frames. If the names of the columns of the data frames being concatenated do not coincide, it fill the holes with `NaN` values. Contrary to the SQL unions, it does not drop the duplicates, and it uses the names of the columns, not the their order, for coupling the components of the union.
