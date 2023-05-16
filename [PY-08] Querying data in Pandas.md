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

```
In [2]: path = 'https://raw.githubusercontent.com/cinnData/PythonBootcamp/main/Data/'
   ...: filename = path + 'airbnb.csv'
```

```
In [3]: df = pd.read_csv(filename, index_col=0)
```

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

## Questions

Q1. How many duplicates do you find in this data set? Drop them.

Q2. What is the proportion of listings whose rating is missing?

Q3. Use a histogram to explore the distribution of the price. 

Q4. What is the average price per room type? Given that the distribution of the price is quite skewed, is it better to use the median?

Q5. In which neighbourhoods do we find more listings? Are they more expensive?

## Q1. Duplicates in this data set

```
In [6]: df.index.duplicated().sum()
Out[6]: 0
```

```
In [7]: df.duplicated().sum()
Out[7]: 28
```

```
In [8]: df = df.drop_duplicates()
```

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

# Q3. Distribution of the price

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
