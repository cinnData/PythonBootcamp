# [PY-07] Basic stats in Pandas

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

## Example - Apple Inc. stock prices

This example is based on data on the Apple Inc. stock prices in the Nasdaq stock market, for the year 2022, as published by Yahoo Finance (`finance.yahoo.com/quote/AAPL/history?p=AAPL`). The data source is the file `aapl.csv`, which covers 251 trading days. The data come in the typical OHLC format (Open/High/Low/Close).

The variables are:

* `date`, the date, as 'yyyy-mm-dd'.

* `open`, the price (US dollars) of the stock at the beginning of the trading day. It can be different from the closing price of the previous trading day.

* `high`, the highest price (US dollars) of the stock on that trading day.

* `low`, the lowest price (US dollars) of the stock on that day.

* `close`, the price (US dollars) of the stock at closing time.

* `adj_close`, the closing price adjusted for factors in corporate actions, such as stock splits, dividends, and rights offerings.

* `volume`, the amount of Apple stock that has been traded on that day.

We import Pandas in the usual way:

```
In [1]: import pandas as pd
```

Let us suppose for this example, that the source file is in our computer. To import the data with `pd.read_csv`, we have to where to find it. The magic command `%pwd` prints the path of working directory (you don't need to this in practice, it is done here for pedagogical purposes). 

```
In [2]: %pwd
Out[2]: '/Users/miguel'
```

So, right now, in the Mac computer where this is prepared, in Qt Console, the working directory is `/Users/miguel`. If it were a Windows computer, the Python kernel would have printed `C:\\Users\\miguel`. If the source file is somewhere inside this folder, this part of the path can be omitted. So, the input in this setting is:

```
In [3]: df = pd.read_csv('Dropbox/py_course/data/aapl.csv')
```

This creates the data frame `df`. Since nothing has been specified about the index, a `RangeIndex` has been assigned. The methof `info()` is probably the best weay to start exploring this data frame.

```
In [4]: df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 251 entries, 0 to 250
Data columns (total 7 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   date       251 non-null    object 
 1   open       251 non-null    float64
 2   high       251 non-null    float64
 3   low        251 non-null    float64
 4   close      251 non-null    float64
 5   adj_close  251 non-null    float64
 6   volume     251 non-null    int64  
dtypes: float64(5), int64(1), object(1)
memory usage: 13.9+ KB
```

The dimensions and the column names are what we expected. Since there are 251 entries in the index and 251 non-null entries in every column, there are no missing values. The distinction between `int` and `float` columns is not relevant for a statistical description. The column `date` has been read as type `str` (reporting it as `object` does change this fact). 

We can take a look at the first rows with the method `.head()`. 

```
In [5]: df.head()
Out[5]: 
         date        open        high         low       close   adj_close  \
0  2022-01-03  177.830002  182.880005  177.710007  182.009995  180.683884   
1  2022-01-04  182.630005  182.940002  179.119995  179.699997  178.390701   
2  2022-01-05  179.610001  180.169998  174.639999  174.919998  173.645538   
3  2022-01-06  172.699997  175.300003  171.639999  172.000000  170.746796   
4  2022-01-07  172.889999  174.139999  171.029999  172.169998  170.915573   

      volume  
0  104487900  
1   99310400  
2   94537600  
3   96904000  
4   86709100  
```

A statistical summary can be printed with the method `.describe()`:

```
In [6]: df.describe()
Out[6]: 
             open        high         low       close   adj_close  \
count  251.000000  251.000000  251.000000  251.000000  251.000000   
mean   154.802709  156.907809  152.691315  154.835060  154.146562   
std     13.063034   12.937389   13.108058   13.056081   12.825977   
min    127.989998  129.949997  125.870003  126.040001  125.847855   
25%    144.330002  146.709999  142.324997  144.645004  144.239502   
50%    154.009995  155.830002  151.940002  154.089996  153.387222   
75%    166.189995  167.989998  164.044998  165.915001  165.019608   
max    182.630005  182.940002  179.119995  182.009995  180.683884   

             volume  
count  2.510000e+02  
mean   8.791038e+07  
std    2.365699e+07  
min    3.519590e+07  
25%    7.229740e+07  
50%    8.373720e+07  
75%    9.693705e+07  
max    1.826020e+08  
```

We are ready now to set up a few questions for practice with Pandas.

## Questions

Q1. Data for the trading days previous to January 15th.

Q2. Use a line plot to see whether there is a **trend** in the opening price.

Q3. Use a line plot and a histogram to visualize the trading volume. What do you conclude?

Q4. A direct measure of **volatility** can be obtained as the difference of the highest price minus the lowest price in a given trading day. This is called the **daily price variation**. Add the daily variation of the Apple stock prices as a new column. Do you see a trend in the daily price variation? How is the distribution?

## Q1. Extract the data for the trading days previous to January 15th

```
In [7]: df[df['date'] < '2022-01-15']
Out[7]: 
         date        open        high         low       close   adj_close  \
0  2022-01-03  177.830002  182.880005  177.710007  182.009995  180.683884   
1  2022-01-04  182.630005  182.940002  179.119995  179.699997  178.390701   
2  2022-01-05  179.610001  180.169998  174.639999  174.919998  173.645538   
3  2022-01-06  172.699997  175.300003  171.639999  172.000000  170.746796   
4  2022-01-07  172.889999  174.139999  171.029999  172.169998  170.915573   
5  2022-01-10  169.080002  172.500000  168.169998  172.190002  170.935425   
6  2022-01-11  172.320007  175.179993  170.820007  175.080002  173.804367   
7  2022-01-12  176.119995  177.179993  174.820007  175.529999  174.251083   
8  2022-01-13  175.779999  176.619995  171.789993  172.190002  170.935425   
9  2022-01-14  171.339996  173.779999  171.089996  173.070007  171.809036   

      volume  
0  104487900  
1   99310400  
2   94537600  
3   96904000  
4   86709100  
5  106765600  
6   76138300  
7   74805200  
8   84505800  
9   80440800  
```

## Q2. Line plot for the opening price

```
In [8]: df['open'].plot(figsize=(10,6), color='black', linewidth=1);
```

![](https://github.com/cinnData/PythonBootcamp/blob/main/Figures/fig_7.1.png)

## Q3. Line plot and histogram for the trading volume

```
In [9]: df['volume'] = df['volume']/10**6
```

```
In [10]: df['volume'].plot(figsize=(10,6), color='black', linewidth=1);
```

![](https://github.com/cinnData/PythonBootcamp/blob/main/Figures/fig_7.2.png)

```
In [11]: df['volume'].plot.hist(figsize=(8,6), color='gray', rwidth=0.98);
```

![](https://github.com/cinnData/PythonBootcamp/blob/main/Figures/fig_7.3.png)

## Q4. Trend and distribution for the daily price variation

```
In [12]: df['dvar'] = df['high'] - df['low']
```

```
In [13]: df.head()
Out[13]: 
         date        open        high         low       close   adj_close   
0  2022-01-03  177.830002  182.880005  177.710007  182.009995  180.683884  \
1  2022-01-04  182.630005  182.940002  179.119995  179.699997  178.390701   
2  2022-01-05  179.610001  180.169998  174.639999  174.919998  173.645538   
3  2022-01-06  172.699997  175.300003  171.639999  172.000000  170.746796   
4  2022-01-07  172.889999  174.139999  171.029999  172.169998  170.915573   

     volume      dvar  
0  104.4879  5.169998  
1   99.3104  3.820007  
2   94.5376  5.529999  
3   96.9040  3.660004  
4   86.7091  3.110001  
```

```
In [14]: df['dvar'].plot(figsize=(10,6), color='black', linewidth=1);
```

![](https://github.com/cinnData/PythonBootcamp/blob/main/Figures/fig_7.4.png)

```
In [15]: df['dvar'].plot.hist(figsize=(8,6), color='gray', rwidth=0.98);
```

![](https://github.com/cinnData/PythonBootcamp/blob/main/Figures/fig_7.5.png)

## Q5. Scatter plot and correlation for the daily price variation and the trading volume

```
In [16]: df.plot.scatter(x='volume', y='dvar', figsize=(6,6), color='gray');
```

![](https://github.com/cinnData/PythonBootcamp/blob/main/Figures/fig_7.6.png)


```
In [17]: df['volume'].corr(df['dvar'])
Out[17]: 0.6461533889925506
```

```
In [18]: df['volume'].corr(df['dvar']).round(2)
Out[18]: 0.65
```

## Homework

The **daily return** is the percentage change in the price with respect to the preceding trading day. If $p(t)$ is the price on day $t$, the corresponding return would be

$$r(t) =\frac{p(t) - p(t-1)}{p(t-1)}=\frac{p(t)}{p(t-1)}-1,$$

which can multiplied by 100 to get percentage scale. Use the Pandas function `pct_change` to calculate the daily returns of the opening price. How is the distribution of the daily return of the opening price? Is there an association between the daily returns and the trading volume?
