# [PY-09] Basic stats in Pandas

## Import/export data using CSV files

Data sets in tabular form can be imported as Pandas data frames from many file formats. In particular, **CSV files** are text files that store data using the comma as the column separator. The names of the columns typically come in the first row, and every other row corresponds to a data point. If Excel is installed in your computer, the files with the extension `.csv` are associated to Excel (with a specific Excel icon) and can be displayed in an Excel sheet by double clicking on the file icon. 

Depending on the configuration of your computer, it may be that a standard CSV file is not displayed in the right way. This happens because Excel does not recognize the comma (`,`) as the column separator, using instead the semicolon (`;`) (the comma is playing the role of decimal separator). This will not affect what you do in Python, which uses the "English" separators.

Data from a CSV file can be imported to a Pandas data frame with the Pandas function `read_csv()`. The (default) syntax is `dfname = pd.read_csv(filename)`. The data frame name is chosen by the user. You have to complete the name of the file with the corresponding path, unless it is in the **working directory**. Files which are not in the working directory can be local or remote, as we will see in the examples of this course. `read_csv()` works the same way for CSV files and for **zipped CSV files**.

Although default options work in most cases satisfactorily, it is worth to comment a few things about some keyword arguments of `read_csv()`. The list is not complete, but enough to give you an idea of the extent to which you can customize this function.

* The parameter `sep` specifies the column separator. The default is `sep=','`, but CSV files created with Excel may need `sep=';'`.

* The parameters `header` and `names` specify the row where the data to be imported start and the column names, respectively. The default is `header=0, names=None`, which makes the Python kernel to start reading from the first row and take it as the column names. When the data come without names, you can use `header=None, names=namelist` to provide a list of names. With a positive value for `header`, you can skip some rows.

* The parameter `index_col` specifies the column to be used as the index, if that were the case. The default is `index_col=None`. For instance, if the intended index comes in the first column, as it frequently happens, you would use `index_col=0`.

* The parameter `usecols` specifies the columns to be read. You can specify them in a list, either by name or by position. The default is `usecols=None`, which means that all the columns will be included.

* The parameter `dtype` specifies the data types of the columns of the data frame. This saves time with big data sets. The default is `dtype=None`, which means that the Python kernel will guess the data type, based on what it reads. When all the entries in a column are numbers, that column is imported as numeric. If there is, at least, one entry that is not numeric, all the entries are read as strings, and the data type `object` is assigned to that column.

* The parameter `encoding`. If the string data contained in a CSV file contain special characters (such as ñ, or á), which can make trouble, you may need to control this. The default encoding in Python is UTF-8 (`encoding='utf-8'`). So, if you are reading a CSV file created in Excel, you may need setting `encoding='latin'` to read the special characters in the right way.

The data contained in a data frame can be exported to a CSV file with the method `.to_csv()`. The basic syntax is `dfname.to_csv(filename)`. The default arguments worth to be mentioned are `sep=','`, of obvious meaning, and `index=True'`, which means that the index will be included in the output file as the first column. If the index is a `RangeIndex`, this may not have any interest, so you would use then `index=False`.

## Summary statistics

The method `.describe()` returns a statistical summary. Basic statistics can also be calculated separately, either for a single series or for a data frame. For instance, for a data frame, the method `.mean()` returns a series containing the column means (only for the numeric columns). 

Correlations are also easy to get:

* `s1.corr(s2)` returns the **correlation** of two numeric series  `s1` and `s2`.

* The method `.corr()` returns the **correlation matrix** for the numeric columns of a data frame.

## Plotting

We typically visualize the data with bar plots, histograms, scatter plots and line plots. How to choose among them is better understood in the examples, so we are very brief here, just displaying the options. The plots can be obtained directly from a Pandas object, without (explicitly) calling Matplotlib. 

Suppose that you set one column of a data frame as *x* and another column as *y* (numeric). To explore the dependence of the *y*-column on the *x*-column, we use: (a) a **bar plot** when the *x*-column is a categorical variable like gender, or (b) a **scatter plot**, when it is a numeric variable like price:

* The method `.plot.bar(x, y)` displays a bar plot. The bars represent the values of `y` for the different values of `x`. If you do not specify the `x`, the index is used instead.

* The method `.plot.scatter(x, y)` displays a scatter plot.

To explore the distribution of numeric series, you use a **histogram**. Alternatively, to explore a time trend, you use a **line plot**. This is pretty easy in Pandas:

* The method `.plot.hist()` displays a histogram of a series.

* The method `.plot.line()` displays a line plot of a series or a collection of columns of a data frame. `.plot()` is the same.
