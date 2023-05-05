# [PY-05] NumPy and Matplotlib

## NumPy arrays

In mathematics, a **vector** is a sequence of numbers, and a **matrix** a rectangular arrangement of numbers. Operations with vectors and matrices are the subject of a branch of mathematics called linear algebra. In the library NumPy (and in many other places), vectors are called one-dimensional (1D) arrays, while matrices are called two-dimensional (2D) arrays. AWith NumPy, arrays of more than two dimensions can be managed in Python without pain.

NumPy arrays are not necessarily numeric. All the terms of an array must have the same type, so the array itself can have a type. In order to cope with the complexities of the data analysis, NumPy provides additional data types, like the type `object`, but this sophistication will not appear in this course.  

The usual way to import NumPy is:

```
In [1]: import numpy as np
```

Arrays can be created directly from lists with the NumPy function `array`. A simple example follows.

```
In [2]: arr1 = np.array(range(10))
   ...: arr1
Out[2]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

Numeric and string arrays are created in the same way. The terms of a 1D array can be extracted from a list, a range, or another data container. The elements of that data container can have different type, but they are converted to a common type when creating the array. The following examples illustrate this. What is the logic of these conversions?

```
In [3]: np.array([2, 'a', True])
Out[3]: array(['2', 'a', 'True'], dtype='<U21')

In [4]: np.array([2, True])
Out[4]: array([2, 1])

In [5]: np.array([2, 3.2])
Out[5]: array([2. , 3.2])
```

*Note*. The data type is not shown for numeric arrays, only for string type. The notation `dtype='<U21'` will look exotic to you. Don't pay attention for the time being.

A 2D array can be directly created from a list of lists of equal length. The terms are entered row-by-row, as in the following example.

```
In [6]: arr2 = np.array([[0, 7, 2, 3], [3, 9, -5, 1]])
   ...: arr2
Out[6]: 
array([[ 0,  7,  2,  3],
       [ 3,  9, -5,  1]])
```

Although we visualize a vector as a column (or as a row) and a matrix as a rectangular arrangement, with rows and columns, it is not so in the computer. A 1D array is just a sequence of elements of the same type, neither horizontal nor vertical. It has one **axis**, the 0-axis. In a similar way, a 2D array is a sequence of 1D arrays of the same length and type. It has two axes. When we visualize it as rows and columns, `axis=0` means across rows, while `axis=1` means across columns.

The number of terms stored along an axis is the **dimension** of that axis. The dimensions are collected in the attribute **shape**.

```
In [7]: arr1.shape
Out[7]: (10,)

In [8]: arr2.shape
Out[8]: (2, 4)
```

## NumPy functions

NumPy incorporates vectorized forms of the mathematical functions of the package `math`. A **vectorized function** is one that, when applied to an array, returns an array with same shape, whose terms are the values of the function on the corresponding terms of the original array. The NumPy square root function is an example.

```
In [9]: np.sqrt(arr1)
Out[9]: 
array([0.        , 1.        , 1.41421356, 1.73205081, 2.        ,
       2.23606798, 2.44948974, 2.64575131, 2.82842712, 3.        ])
```

The functions that are defined in terms of vectorized functions are automatically vectorized. An example follows.

```
In [10]: def f(t): return 1/(1 + np.exp(t))
   ...: f(arr2)
Out[10]: 
array([[5.00000000e-01, 9.11051194e-04, 1.19202922e-01, 4.74258732e-02],
       [4.74258732e-02, 1.23394576e-04, 9.93307149e-01, 2.68941421e-01]])
```

NumPy also provides common statistical functions, such as `mean`, `max`, `sum`, etc.

## Subsetting arrays

Subsetting a 1D array is done as in a list:

```
In [11]: arr1[:3]
Out[11]: array([0, 1, 2])
```

The same applies to 2D arrays, but we need two indexes within the square brackets. The first index selects the rows (`axis=0`), and the second index the columns (`axis=1`):

```
In [12]: arr2[:1, 1:]
Out[12]: array([[7, 2, 3]])
```

Subarrays can also be extracted by means of an **expression**. When you input the expression formed by an array, a comparison operator (such as `>`) and a **literal** (such as 3), the expression is evaluated, and the Python interpreter returns a Boolean array with the same shape:

```
In [13]: arr1 > 3
Out[13]: 
array([False, False, False, False,  True,  True,  True,  True,  True,
        True])

In [14]: arr2 > 2
Out[14]: 
array([[False,  True, False,  True],
       [ True,  True, False, False]])
```

A Boolean array that is used to extract a subarray is called a **Boolean mask**. The terms for which the mask has value `True` are those selected: 

```
In [15]: arr1[arr1 > 3]
Out[15]: array([4, 5, 6, 7, 8, 9])
```

Boolean masks can also be used to filter out rows or columns of a 2D array. For instance, you can select the rows of `arr2` for which the first column is positive, as we see next.

```
In [16]: arr2[arr2[:, 0] > 0, 1:]
Out[16]: array([[ 9, -5,  1]])
```

## Plotting with Matplotlib

Inspired in MATLAB, a classic of numeric computing, **Matplotlib** is a Python library containing an impressive range of graphical methods, including image processing. As some other libraries in the Python world, Matplotlib has several API's, which makes it a bit confusing for the beginners. In this context, an **application programming interface** (API) is like an idiom that you use for calling the functions of the library. It defines the kinds of requests that can be made and how to make them. 

Matplotlib offers you a choice between two API's, the **pyplot API**, used in this course, and the **object-oriented API**. This course uses the pyplot API. Beware that, if you search in the Internet information about plotting in Matplotlib, the solutions found can come in any of the two API's. So Matplotlib may look more difficult than it really is.

The subpackage `matplotlib.pyplot` is a collection of command style functions that make Matplotlib work like MATLAB. It is typically imported as:

```
In [17]: import matplotlib.pyplot as plt
```

To create a figure with `pyplot`, we call in a single input one or several functions. Each `pyplot` function makes some change to the figure, such as changing the default size, adding a title, plotting lines, decorating the plot with labels, etc. This is illustrated by the following example, in which we plot together three curves, a linear, a quadratic and a cubic curve. 

First, we fill a 1D array with linearly spaced values, tightly close, so we can create a smooth curve.

```
In [18]: t = np.linspace(0, 2, 100)
```

Next, we ask for the plot:

```
In [19]: plt.figure(figsize=(6,6))
    ...: plt.title('Figure. Three curves')
    ...: plt.plot(t, t, label='linear', color='black')
    ...: plt.plot(t, t**2, label='quadratic', color='black', linestyle='dashed')
    ...: plt.plot(t, t**3, label='cubic', color='black', linestyle='dotted')
    ...: plt.legend();
```

![](https://github.com/cinnData/PythonBootcamp/blob/main/Figures/fig_5.1.png)

Take care of running these lines of code together. The semicolon in the last line stops the Python output showing up. That output would correspond to `plt.legend` and would not say much to you. 

`plt.figure` allows you to change some default specifications. Here, we have changed the size. If you are satisfied with the default size `figsize=(6,4)`, you do not need this line of code. Here, `figsize=(6,6)` has been set so that the figure looks fine on the screen. The units for the width and height and are inches.

`plt.plot` creates a line chart (which can be turned into a scatter plot, although it is better to use `plt.scatter` for that). If two vectors are entered, the first one is taken as $x$ (horizontal axis) and the second one as $y$ (vertical axis). If there is only one vector, it is taken as $x$, and the index is used as $y$. Here, we get a multiple line chart by calling `plt.plot` multiple times. Note that, even if you see the three components plotted here as three curves, they are really line plots without markers.

`plt.plot` admits other arguments, allowing a minute edition of your visualization, down to the smallest detail. As a default, it uses solid lines, with different colors for the different lines. The **line style** has been specified by the argument `linestyle`, and the **color** by the argument `color`. The default is `color='blue'`.

## Homework

1. For `x = np.array([True, False])` and `y = np.array([True, True])`, calculate `~x`, `x & y` and `x | y`. What is the meaning of these operations?

2. Plot together the curves $y = x^3 + x^2 - 3^x +1$ and $y = -x^3 + 0.5\hbox{\thinspace}x^2 + x + 1$ in the interval $-2 \le x \le 2$.
