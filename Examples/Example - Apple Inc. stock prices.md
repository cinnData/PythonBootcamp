# Example - Apple Inc. stock prices

## Introduction

This example is based on data on the Apple Inc. stock prices in the Nasdaq stock market, for the year 2022, as published by Yahoo Finance. These data are used to illustrate the time series methods provided by the Python package Pandas.

## The data set

The data set (file `aapl.csv`) covers 251 trading days. The data come in the typical OHLC format (Open/High/Low/Close).

The variables are:

* `date`, the date, as 'yyyy-mm-dd'.

* `open`, the price (US dollars) of the stock at the beginning of the trading day. It can be different from the closing price of the previous trading day.

* `high`, the highest price (US dollars) of the stock on that trading day.

* `low`, the lowest price (US dollars) of the stock on that day.

* `close`, the price (US dollars) of the stock at closing time.

* `adj_close`, the closing price adjusted for factors in corporate actions, such as stock splits, dividends, and rights offerings.

* `volume`, the amount of Apple stock that has been traded on that day.

Source: `finance.yahoo.com/quote/AAPL/history?p=AAPL`.

## Questions

Q1. Import this data set to a Pandas data frame.

Q2. Check the content of the data set.	

Q3. Extract the data for the trading days previous to January 15th. 

Q4. Use a **line plot** to see whether there is a **trend** in the opening price.

Q5. Use a line plot and a **histogram** to visualize the trading volume. What do you conclude?

Q6. A direct measure of **volatility** can be obtained as the difference of the highest price minus the lowest price in a given trading day. This is called the **daily price variation**. Add the daily variation of the Apple stock prices as a new column. Do you see a trend in the daily price variation? How is the distribution?

Q7. Use a **scatter plot** to examine the association between the daily price variation and the trading volume. What is the **correlation**?

## Homework

The **daily return** is the percentage change in the price with respect to the preceding trading day. If $p(t)$ is the price on day $t$, the corresponding return would be

$$r(t) =\frac{p(t) - p(t-1)}{p(t-1)}=\frac{p(t)}{p(t-1)}-1,$$

which can multiplied by 100 to get percentage scale. Use the Pandas function `pct_change` to calculate the daily returns of the opening price.

How is the distribution of the daily return of the opening price? Is there an association between the daily returns and the trading volume?
