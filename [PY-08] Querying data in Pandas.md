# [PY-08] Querying data in Pandas

## Sorting

This last lecture presents a collection of basic procedures for cleaning, exploring and summarizing data stored in Pandas data frames. We start with **sorting** methods. Pandas series can be sorted by the index or by the values, with the methods `.sort_index()` and `.sort_values()`, respectively. Both work for data frames, but, for the second one, you have to specify either the name of a column or a list of column names, which will then be used in the order that you wrote them.

The parameter `ascending` allows you to choose between ascending and descending ways. The default (in Python as in other languages) is `ascending=True`.

## Missing values

**Missing values** are denoted by `NaN` in Pandas. When a Pandas object is built, both Python's `None` and NumPy's `nan` are taken as `NaN`. Since `np.nan` has type `float`, numeric columns containing `NaN` values get type `float`. 

Three useful Pandas methods related to missing values, which can be applied to both series and data frames, are: 

* `.isna()` returns a Boolean mask indicating which terms are missing.

* `.fillna()` is used for replacing `NaN`'s by a fixed value, set by the user.

* `.dropna()` returns the same data set minus the rows that contain at least one missing value. 

## Duplicates

There are two useful Pandas methods for managing **duplicates**:

* `.duplicated()` returns a Boolean series indicating the rows which are duplicated. The default is `keep=first`, meaning that, the data are read top-down, returning `False` for the values occurring for the first time, and `True` for those having occurred before. 

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

## Example - Barcelona Airbnb listings

**Airbnb** is a peer-to-peer online marketplace and homestay network, which enables people to list or rent short-term lodging in residential properties, with the cost of such accommodation set by the property owner, called the **host** at Airbnb. The company receives percentage service fees from both guests and hosts in conjunction with every booking. Starting in 2008, it has grown exponentially, and it currently has over 6 million listings in about 200 countries.

Airbnb currently releases and updates data at the **Inside Airbnb** site (`www.insideairbnb.com`). The updates posted in March 2023 cover 116 areas, most of them in US and Europe. This example uses data from Barcelona. In Barcelona, vacation apartments are subject to the highest rate of property tax, and platforms must share data with regulators.

The file `airbnb.csv` contains data on 15,655 Airbnb **listings** in Barcelona. The language in the descriptions is typically English or Spanish (with exceptions). The text comes in **UTF-8 encoding**, so special characters may not be correctly shown (in Spanish words such as 'habitación') in some applications like Excel.

The variables are:

* `listing_id`, a unique listing's ID. An active listing is a property listed on Airbnb. Listings may include entire homes or apartments, private rooms or shared spaces.

* `host_id`, a unique host's ID.

* `host_since`, the date of the host's first listing in Airbnb, as yyyy-mm-dd.

* `name`, the listing's name. A minimal description (maximum 35 characters) of the place, intended to be appealing, such as 'Centric Bohemian next Ramblas & Macba'.

* `neighbourhood`, the **neighbourhood** (barrio) of the listing. The neighbourhoods are sourced from the city.

* `district`, the district of the listing. The districts, called **neighbourhood groups** at Airbnb, are sourced from the city. There are 10 districts in Barcelona, each grouping several neighbourhoods.

* `property_type`, the type of property listed. 75% of the listings come as 'Entire rental unit', or 'Private room in rental unit', but Airbnb admits many other possibilities.

* `room_type`, taking values 'Entire home/apt', 'Private room', 'Shared room' and 'Hotel room'.

* `bedrooms`, the number of available bedrooms.

* `price`, the daily listing's price on that date, in euros. The price shown is for the listing as a whole, not per person. The price that you see when you search Airbnb (with dates selected) is the total price divided by the number of nights you selected. When a listing has been booked for several days, the price can be lower, since the host can apply different prices depending on the number of days booked.

* `number_of_reviews`, the number of reviews of that listing that have been posted.

* `review_scores_rating`, the average reviewers' rating of overall experience (*What was your guest’s overall experience?*). Listings are rated in the range 1-100.

```
In [1]: import pandas as pd
```
In this example, we use a remote data source. In Pandas, this works the same as with a local file, the only difference is in the path. The data files of this course can be found in the same GitHub repository as the document that you're reading. The path for these files can be inputted as follows.

```
In [2]: path = 'https://raw.githubusercontent.com/cinnData/PythonBootcamp/main/Data/'
```

We import the data to a Pandas data frame with the function `read_csv`. In this example, we use the parameter `index_col` to specify the column `listing_id` as the index. 

```
In [3]: df = pd.read_csv(path + 'airbnb.csv', index_col=0)
```

You will see in the report extracted by the method `.info()` that the index is an `Int64Index`, meaning that all the entries are integers, but not consecutive integers generated automatically as in a `RangeIndex`. Note that `listring_id` is not included in the column list.

```
In [4]: df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 15655 entries, 13977576 to 52874282
Data columns (total 11 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   host_id               15655 non-null  int64  
 1   host_since            15653 non-null  object 
 2   name                  15646 non-null  object 
 3   neighbourhood         15655 non-null  object 
 4   district              15655 non-null  object 
 5   property_type         15655 non-null  object 
 6   room_type             15655 non-null  object 
 7   bedrooms              15098 non-null  float64
 8   price                 15655 non-null  float64
 9   number_of_reviews     15655 non-null  int64  
 10  review_scores_rating  12176 non-null  float64
dtypes: float64(3), int64(2), object(6)
memory usage: 1.4+ MB
```

The first rows can be displayed with the method `.head()`.

```
In [5]: df.head()
Out[5]: 
            host_id  host_since  \
id                                
13977576   64903899  2016-03-29   
42105584  333969184  2020-02-06   
33727898  251710733  2019-03-28   
44995311  363074093  2020-08-18   
15763812  101927904  2016-10-31   

                                                       name  \
id                                                            
13977576                 Habitación individual es Barcelona   
42105584                                     Habitación M&D   
33727898  Spacious and bright apartment next to Plaza Es...   
44995311         Single Room, City Center, Private Bathroom   
15763812                            HABITACIÓN PLAZA ESPAÑA   

                   neighbourhood        district                property_type  \
id                                                                              
13977576             Hostafrancs  Sants-Montjuïc  Private room in rental unit   
42105584          la Prosperitat      Nou Barris  Private room in rental unit   
33727898             Sant Antoni        Eixample           Entire rental unit   
44995311  la Dreta de l'Eixample        Eixample       Private room in hostel   
15763812            el Poble Sec  Sants-Montjuïc  Private room in rental unit   

                room_type  bedrooms  price  number_of_reviews  \
id                                                              
13977576     Private room       1.0   12.0                  1   
42105584     Private room       NaN   25.0                  0   
33727898  Entire home/apt       3.0  300.0                 30   
44995311     Private room       1.0   83.0                 11   
15763812     Private room       1.0   38.0                 70   

          review_scores_rating  
id                              
13977576                  0.00  
42105584                   NaN  
33727898                  5.00  
44995311                  4.82  
15763812                  4.75  
```

We are ready now to set up a few questions for practice with Pandas.

## Questions

Q1. How many duplicates do you find in this data set? Drop them.

Q2. What is the proportion of listings whose rating is missing?

Q3. Use a histogram to explore the distribution of the price. 

Q4. What is the average price per room type? 

Q5. In which neighbourhoods do we find more listings? Are they more expensive?

## Q1. Duplicates in this data set

Duplicates can be detected with the method `.duplicated()`, which returns a Boolean object of the same shape of the object to which it is applied. In this example, it makes sense to apply it to the index, to check whether there are duplicated listing ID's. Note that Pandas has no rule against duplicated indexes, though in most applications to real data, in which we take the index as an identifier of the row, duplicated indexes are *wrong*.

In this data set, the listing's ID in this data set is never duplicated, as we see next. This is an example that illustrates how computers count the times an expression is true. The method `.duplicated()` checks whether a particular index value is duplicated (meaning that it has already appeared), returning a `True`/`False` value. These Booleans are stored in the series `df.index.duplicated()`. By applying `.sum()`, we convert the Booleans to integers (1/0), so the sum is equal to the number of `True` values, that is, the number of duplicates. Note that, if an index value appears $n$ times, it is counted as $n - 1$ duplicates.

```
In [6]: df.index.duplicated().sum()
Out[6]: 0
```

The number of duplicated rows is found using the same logic. The index is not checked now. Note that `df.duplicated()` returns `True` when the whole row (all entries) is duplicated. 

```
In [7]: df.duplicated().sum()
Out[7]: 28
```

We find 28 cases. They correspond to listings which have exactly the same data. This may happen, *e.g*. when they refer to beds in a shared bedroom. Neverthless, following the instructions, we drop the duplicates.

```
In [8]: df = df.drop_duplicates()
```

We are left with a slightly smaller data set.

```
In [9]: df.shape
Out[9]: (15627, 11)
```

## Q2. Proportion of listings with missing ratings

```
In [10]: df.isna().sum()
Out[10]: 
host_id                    0
host_since                 2
name                       9
neighbourhood              0
district                   0
property_type              0
room_type                  0
bedrooms                 557
price                      0
number_of_reviews          0
review_scores_rating    3452
dtype: int64
```

```
In [11]: df['review_scores_rating'].isna().mean().round(3)
Out[11]: 0.221
```

## Q3. Distribution of the price

```
In [12]: df['price'].plot.hist(figsize=(8,6), color='gray', rwidth=0.98);
```

![](https://github.com/cinnData/PythonBootcamp/blob/main/Figures/fig_8.1.png)

Is this histogram useful? Not much, since some very expensive listings distort the whole picture. Can we trim the data, to get a better picture?

```
In [13]: df['price'].describe()
Out[13]: 
count    15627.000000
mean       155.743137
std        966.968387
min          0.000000
25%         50.000000
50%         99.000000
75%        164.000000
max      90000.000000
Name: price, dtype: float64
```

```
In [14]: df['price'][df['price'].between(25,175)].plot.hist(figsize=(8,6), color='gray', rwidth=0.94, bins=30);
```

![](https://github.com/cinnData/PythonBootcamp/blob/main/Figures/fig_8.2.png)

## Q4. Average price per room type

```
In [15]: pd.pivot_table(df, values='price', index='room_type', aggfunc='mean').round()
Out[15]: 
                 price
room_type             
Entire home/apt  181.0
Hotel room       206.0
Private room     117.0
Shared room       48.0
```

Given that the distribution of the price is quite skewed, is it better to use the median?

```
In [16]: pd.pivot_table(df, values='price', index='room_type', aggfunc='median')
Out[16]: 
                 price
room_type             
Entire home/apt  135.0
Hotel room       174.0
Private room      48.0
Shared room       32.0
```

## Q5. Top-10 neighbourhoods

```
In [17]: df['neighbourhood'].value_counts().head(10)
Out[17]: 
neighbourhood
la Dreta de l'Eixample                   2029
el Raval                                 1251
el Barri Gòtic                           1064
Sant Pere, Santa Caterina i la Ribera     979
la Vila de Gràcia                         943
la Sagrada Família                        942
l'Antiga Esquerra de l'Eixample           892
Sant Antoni                               781
el Poble Sec                              738
la Nova Esquerra de l'Eixample            612
Name: count, dtype: int64
```

```
In [18]: df.groupby(by='neighbourhood')['price'].agg(['count', 'median']).sort_values(by='count', ascending=False).head(10)
Out[18]: 
                                       count  median
neighbourhood                                       
la Dreta de l'Eixample                  2029   159.0
el Raval                                1251    69.0
el Barri Gòtic                          1064    77.0
Sant Pere, Santa Caterina i la Ribera    979    82.0
la Vila de Gràcia                        943   111.0
la Sagrada Família                       942   125.5
l'Antiga Esquerra de l'Eixample          892   127.0
Sant Antoni                              781   122.0
el Poble Sec                             738    94.5
la Nova Esquerra de l'Eixample           612    90.0
```

## Homework

Use the `groupby` approach to extract the pivot tables of inputs 15 and 16.
