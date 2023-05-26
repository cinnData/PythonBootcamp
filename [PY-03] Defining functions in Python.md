# [PY-03] Defining functions in Python

## Functions

A **function** takes a collection of **arguments** and performs an action. For instance, a function can **return** a value, and another function can **print** a message. Besides the built-in functions like `type()` or `len()` and those coming in the packages that you may import, you can define your own functions. The definition of your function will be valid only for the current kernel.

A simple example of a user-defined function follows. Note the indentation after the colon, which is created automatically by the console (or notebook).

```
In [1]: def f(x):
    ...:     y = 1/(1 - x**2)
    ...:     return y
```

Here, the `return` line signals the end of the definition. If you continue the input, the new lines will not be indented, and will not be read as part of the definition of the function.

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

Beginners find Python error messages, though accurate, not precisely friendly. But, if you pay attention to them, you will discover that they can be very useful for correctiong your mistakes. In the two examples above, the error message indicates the nature of the error. The first one is a `ZeroDivisionError`, while the second one is a `TypeError` (the argument has not the adequate data type). Other errors can be `SyntaxError`, `ValueError`, etc. 

Now, an example of a two-parameter function.

```
In [5]: def g(x, y): return x*y/(x**2 + y**2)
````

```
In [6]: g(1, 1)
Out[6]: 0.5
```

Note that, in the definition of `g()`, we have used a shorter way. Many programmers would prefer to make it longer, with more than one line, as we did previously for `f()`.

## Functions and methods

Something that confuses Python beginners is the distinction between functions and methods. A **method** is a function that belongs to a particular type of objects. Some types don't have methods, but other types have plenty of them. Take, for instance strings. The function `len` takes a string and returns the number of characters.

```
In [7]: len('Bruce Sprinsgteen')
Out[7]: 17
```

The syntax is `fname(args)`. But strings have also many methods. For instance, to replace all the occurrences of a substring by a new string (the *Replace* function of Word, with option *Replace All*), we use the method `.replace()`. Let us see an example.

```
In [8]: 'Bruce Sprinsgteen'.replace('Bruce', 'The Boss')
Out[8]: 'The Boss Sprinsgteen'
```

The syntax is `object.mname(args)`. Another example: to convert all the cased characters to lowercase, we use the method `.lower()`. 

```
In [9]: 'Bruce Sprinsgteen'.lower()
Out[9]: 'bruce sprinsgteen'
```

An advantage of methods is that you can apply a sequence of methods one after the other, without getting into a mess with the parentheses. You may have fought with this in Excel. But sometimes the reason for defining some functions is unclear, and may be a source of confusion. Moreover, some functions can appear as functions here and as methods there. An example is the function `round`, which is used to limit the number of decimals retained. As built-in Python function the syntax as shown in the following example:

```
In [10]: round(1/3, 2)
Out[10]: 0.33
```

The same as in Excel. But, when rounding in one shot a whole column of a data set in the package Pandas, we would use a method, `.round(2)`. The package Pandas uses methods almost everywhere. Since this is data-oriented course, which makes frequent use of Pandas, this is worth to remember. When in doubt, check which the right approach by googling, or use the cheatsheets of this course.

## Homework

1. Write a Python function which, given three integers, returns `True` if any of them is zero, and `False` otherwise.

2. Write a Python function which, given three integers, returns `True` if they are in order from smallest to largest, and `False` otherwise. Modify your function so that it returns `1`/`0` instead of `True`/`False`.

3. Given two positive integers `a` and `b`, you can get the remainder of the integer division of `a` by `b` with `a%b`. So `7%3` returns `1`, and `9%5` returns `4`. Write a function which, given an integer, returns `True` if that integer is a multiple of 7, and `False` otherwise.

4. A year is a **leap year** if it is divisible by 4, unless it is a century year that is not divisible by 400. So, 1800 and 1900 are not leap years while 1600 and 2000 are. Write a function that tells you whether a year is a leap year.

5. Write a function which anonymizes credit card numbers, turning, for instance, '2875765488882745' into 'Credit card ****745'. 
