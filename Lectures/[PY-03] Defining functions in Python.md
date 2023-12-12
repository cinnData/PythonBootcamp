# [PY-03] Defining functions in Python

## A first example

This lecture is a short introduction to **Python functions**. Besides the **built-in functions** like `type()` or `len()` and those coming in the packages that you may import, you can define your own functions. That definition will be valid only for the current kernel.

A simple example of a user-defined function follows. Note the indentation after the colon. Jupyter apps (console and notebook) automatically insert an indentation when you strike *Return* after the colon.

```
In [1]: def f(x):
   ...:     y = 1/(1 - x**2)
   ...:     return y
```

Here, the `return` statement signals the end of the definition. If you continue the input, the new lines will not be indented, and will not be read as part of the definition of the function.

When you define a function, Python just takes note of the definition, accepting it when it is syntactically correct (parentheses, commas, etc). The function can be applied later to different arguments (by the same kernel).

```
In [2]: f(2)
Out[2]: -0.3333333333333333
```

If you apply the function to an argument for which it does not make sense, the Python kernel will return an error message. The following two examples illustrate this. 

```
In [3]: f(1)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_40368/1567560659.py in <module>
----> 1 f(1)

/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_40368/1722558193.py in f(x)
      1 def f(x):
----> 2     y = 1/(1 - x**2)
      3     return y

ZeroDivisionError: division by zero
```

```
In [4]: f('Mary')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_40368/2381081837.py in <module>
----> 1 f('Mary')

/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_40368/1722558193.py in f(x)
      1 def f(x):
----> 2     y = 1/(1 - x**2)
      3     return y

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
```

Beginners find Python error messages, though accurate, not precisely friendly. But, if you pay attention to them, you will discover that they can be very useful for correcting your mistakes. In the two examples above, the error message indicates the nature of the error. The first one is a `ZeroDivisionError`, while the second one is a `TypeError` (the argument has not the adequate data type). Other errors can be `SyntaxError`, `ValueError`, etc. 

You can write the definition of a function in a shorter way, as the following example shows. But this is not considered good programming' style (more about this later), so we will not take this type of shortcut in this course.

```
In [5]: def f(x): return 1/(1 - x**2)
```

## More about functions

In general, a function takes a collection of arguments and performs an action. We typically specify that action in a separate line, like the `return` statement of the preceding example. A mathematical function, like that example, returns a value. But Python function have a wider scope. They can print a text, or save a file, etc. Examples of printing functions will appear in this course. 

Let us take a closer look at our definition, considering three parts. In the first line, the `def` statement declares many things:

* It provides a **name** for the function (`f`). Since this an example of a mathematical function, a simple name like `f` was appropriate, but, in general, it is recommended to use names that remind us of the action performed by the function. 

* It names the **parameters**. The example of the preceding section was an example of a **one-parameter function**. `x` was the parameter name. The values provided for the parameter are called **arguments**. 

* It may contain additional information about the parameters, such as default values, which will be explained below.

After the `def` statament, we write some lines specifying a sequence operations to be performed on the arguments in order to prepare the final action, described in the last line. In this case, this was a `return` statement.

We are going to see few examples in which the defintion follows different paths. First, an example of a function with zero parameters (yes, this is possible) and a `print` statement.

```
In [6]: def hello():
   ...:     print('Hello, world!!')
```

```
In [7]: hello()
Hello, world!!
```

Now, an example of a two-parameter function.

```
In [8]: def g(x, y): 
   ...:     z = (x - y)/(x**2 + y**2)
   ...:     return z
````

```
In [9]: g(2, 1)
Out[9]: 0.2
```

## Positional arguments and keyword arguments

The distinction between positional and keyword arguments is better understood in an example. In `In [9]`, the Python kernel took the argument 2 as the value of the parameter `x` and 1 as the value of the parameter `y`. They were taken as **positional arguments**, so that input was read exactly the same as the following one.

```
In [10]: g(x=2, y=1)
Out[10]: 0.2
```

Now, the arguments were taken as **keyword arguments**. The order of keyword arguments does not matter, so there is no difference between `In [10]` and the following one.

```
In [11]: g(y=1, x=2)
Out[11]: 0.2
```

On the other hand, for positional arguments, the order matters, and one has to be careful. In the following input, the first argument will be taken as `x` and the second argument as `y`.

```
In [12]: g(1, 2)
Out[12]: -0.2
```

Note that the parameters themselves are not positional nor keyword. It is the way we submit their values (the arguments), that makes them to be read in this or that way. You can mix positional and keyword arguments, as in the following example.

```
In [13]: g(2, y=1)
Out[13]: 0.2
```

But the positional arguments must go first:

```
In [14]: g(x=2, 1)
  Cell In[12], line 1
    g(x=2, 1)
            ^
SyntaxError: positional argument follows keyword argument
```

*Note*. Not everybody is so strict with the terminology, and the terms "parameter" and "argument" are sometimes confounded.

## Default arguments

Sometimes, there is a typical, or preferred, value for a parameter. We can specify this value in the definition, so the users can omit the corresponding arguments when using the function. **Default arguments** are the rule for most functions that admit large collections of parameters. They make your code shorter and cleaner.

How to specify a default value for a parameter is clear in the following example. Suppose that you wish to have a function called `root()` such that by default is the square root, but may be used also for other roots. Let us define it as follows. We can define it as follows.

```
In [15]: def root(x, n=2):
    ...:    y = x**(1/n)
    ...:    return y
```

Now:

```
In [16]: root(2)
Out[16]: 1.4142135623730951
```

```
In [17]: root(2, 3)
Out[17]: 1.2599210498948732
```

An example we often meet frequently, working with data, is the Pandas function `read.csv()`, used to import data from a CSV file. It allows for various separators, but a default argument is `sep=','`, which makes sense because most CSV files use the comma as the column separator. This function will appear in the last lectures of this course.

## Functions and methods

Something that confuses Python beginners is the distinction between functions and methods. A **method** is a function that belongs to a particular type of objects. Some types don't have methods, but other types have plenty of them. Take, for instance, strings. The function `len` takes a string and returns the number of characters.

```
In [18]: len('Bruce Sprinsgteen')
Out[18]: 17
```

But strings have also many methods. For instance, to replace all the occurrences of a substring by a new string (the *Replace* function of Word, with option *Replace All*), we use the method `.replace()`. Let us see an example.

```
In [19]: 'Bruce Sprinsgteen'.replace(old='Bruce', new='The Boss')
Out[19]: 'The Boss Sprinsgteen'
```

Another example: to convert all the cased characters to lowercase, we use the method `.lower()` (zero parameters). 

```
In [20]: 'Bruce Sprinsgteen'.lower()
Out[20]: 'bruce sprinsgteen'
```

An advantage of methods is that you can apply a sequence of methods one after the other, without getting into a mess with the parentheses. You may have fought with this in Excel. But sometimes the reason for defining some functions is unclear, and may be a source of confusion. Moreover, some functions can appear as functions here and as methods there. An example is the function `round`, which is used to limit the number of decimals retained. As built-in Python function the syntax as shown in the following example:

```
In [21]: round(x=1/3, n=2)
Out[21]: 0.33
```

The same as in Excel. But, when rounding in one shot a whole column of a data set in the package Pandas, we would use a method, `.round(decimals=2)`. Pandas uses methods almost everywhere. Since this is data-oriented course, which makes frequent use of Pandas, this is worth to remember. When in doubt, check which the right approach by googling, or use the cheatsheets of this course.

## Homework

1. Write a Python function which, given three integers, returns `True` if any of them is zero, and `False` otherwise.

2. Write a Python function which, given three integers, returns `True` if they are in order from smallest to largest, and `False` otherwise. Modify your function so that it returns `1`/`0` instead of `True`/`False`.

3. Given two positive integers `a` and `b`, you can get the **remainder** of the integer division of `a` by `b` with `a%b`. So `7%3` returns `1`, and `9%5` returns `4`. Write a function which, given an integer, returns `True` if that integer is a multiple of 7, and `False` otherwise.

4. A year is a **leap year** if it is divisible by 4, unless it is a century year that is not divisible by 400. So, 1800 and 1900 are not leap years while 1600 and 2000 are. Write a function that tells you whether a year is a leap year.

5. Write a function which anonymizes credit card numbers, turning, for instance, `'2875765488882745'` into `'Credit card ****745'`.
