# [PY-09] Basic stats in Pandas

## Import/export data using CSV files

Data sets in tabular form can be imported as Pandas data frames from many file formats. In particular, **CSV files** are text files which store data using the comma as the column separator. The names of the columns typically come in the first row, and every other row corresponds to a data point. If Excel is installed in your computer, the files with the extension `.csv` are associated to Excel (with a specific Excel icon) and can be displayed in an Excel sheet by double clicking on the file icon. 

Depending on the configuration of your computer, it may be that a standard CSV file is not displayed in the right way. This happens because Excel does not recognize the comma (`,`) as the column separator, using instead the semicolon (`;`) (the comma is playing the role of decimal separator). This will not affect what you in Python, which follows the "English" style.

Data from a CSV file can be imported to a Pandas data frame with the Pandas function `read_csv`. The (default) syntax is `dfname = pd.read_csv(fname)`. The data frame name is chosen by the user. You have to complete the name of the file with the corresponding path, unless it is in the **working directory**. In Jupyter Qt Console, this is `/Users/username` in Mac computers and `C:/Users/username` in Windows computers. In a Jupyter notebook, the working directory is the folder where the notebook is. Take care of using the slash (`/`), not the backslash, (`\`) to separate the folders in the path. Files which are not in the working directory can be local or remote. For local files whose path would include the path of the working directory, the part of the path can be omitted. `read_csv` works the same way for CSV files and for **zipped ZIP files**. Some of these variations will appear in the examples of this course.

Although defaults work in most cases satisfactorily, it is worth to comment a few things about some optional parameters of `read_csv`. The list is not complete, but enough to give you an idea of the extent to which you can customize this function.

* `sep` specifies the column separator. The default is `sep=','`, but CSV files created with Excel may need `sep=';'`.

* `header` and `names` specify the row where the data to be imported start and the column names, respectively. The default is `header=0, names=None`, which makes Pandas start reading from the first row and take it as the column names. When the data come without names, you can use `header=None, names=namelist` to provide a list of names. With a positive value for `header`, you can skip some rows.

* `index_col` specifies the column that you wish to use as the index, if that were the case. The default is `index_col=None`. If the intended index comes in the first column, as it frequently happens, you will use `index_col=0`.

* `usecols` specifies the columns to be read. You can specify them in a list, either by name or by position. The default is `usecols=None`, which means that you wish to read all the columns.

* `dtype` specifies the data types of the columns of the data frame. This saves time with big data sets. The default is `dtype=None`, which means that Python will guess the data type, based on what it reads. When all the entries in a column are numbers, that column is imported as numeric. If there is, at least, one entry that is not numeric, all the entries are read as strings, and the data type `object` is assigned to that column.

* `encoding`. If the string data contained in a CSV file can contain special characters (such as ñ, or á), which can make trouble, you may need to control this. The default in Python is `encoding='utf-8'`. So, if you are reading a CSV file created in Excel, you may need to set `encoding='latin'` to read the special characters in the right way.

The data contained in a data frame can exported to a CSV file with the method `.to_csv()`. The basic syntax is `dfname.to_csv(fname)`. The deafult for the separator is `sep=','`. That of the index is `index=True'`, meaning that the index will be included in the output file as the first column. If the index is a `RangeIndex`, this may not have any interest, and then yould use `index=False`.

## Summary statistics

The method `describe` prints a statistical summary. Basic statistics can also be calculated separately, either for a single series or for a data frame. For instance, for a data frame `df`, `df.mean()` returns a series containing the column means (only for the numeric columns). 

Correlations are also easy to get:

* `s1.corr(s2)` returns the **correlation** of two numeric series  `s1` and `s2`.

* `df.corr()` returns the **correlation matrix** for the numeric columns of `df`.

## Plotting

We typically visualize the data with bar plots, histograms, scatter plots and line plots. Why use one or another is better understood in the examples, so we are very brief here, just displaying the options. The plots can be obtained directly from a Pandas object, without (explicitly) calling Matplotlib. 

Suppose that `df` is a Pandas data frame and set `cname1` as the *x*-column and `cname2` as the *y*-column (numeric). To explore the dependence of the *y*-column on the *x*-column, we use: (a) a **bar plot** when the *x*-column is a categorical variable like gender, or (b) a **scatter plot**, when it is a numeric variable like price:

* `df.plot.bar(x=cname1, y=cname2)` returns a bar plot. The bars represent the values of `cname2` for the different values of `cname1`. If you do not specify the *x*-column, the index is used instead.

* `df.plot.scatter(x=cname1, y=cname2)` returns a scatter plot.

Suppose now that `s` is a numeric series. To explore the distribution of `s`, you use a **histogram**. Alternatively, to explore a time trend, you use a **line plot**. This is pretty easy in Pandas:

* `s.plot.hist()` returns a histogram.

* `s.plot.line()` returns a line plot.

Pandas uses Matplotlib functions, but not explicitly. If you are satisfied with a basic functionality, you can skip Matplotlib in your code. If you want to add labels, titles, or other features, you can import `matplotlib.pyplot` and add code lines for labels, title, legends, etc.
