# [PY-04] Functions and control statements

## Functions

A **function** takes a collection of **arguments** and performs an action. For instance, a function can **return** a value, and another function can **print** a message. Besides the built-in functions like `type()` or `len()` and those coming in the packages that you may import, you can define your own functions. The definition of your function will be valid only for the current kernel.

A simple example of a user-defined function follows. Note the indentation after the colon, which is created automatically by the console (or notebook).

```
In [1]: def f(x):
    ...:     y = 1/(1 - x**2)
    ...:     return y
```

Here, the `return` line signals the end of the definition. If you continue the input, the new lines will not be indented, and will not be read as part of the definition of the function.

*Note*. This course follows the common practice in Python learning materials of writing functions as `fname()`. The parentheses remind you that this is an object that takes arguments. 

When you define a function, Python just takes note of the definition, accepting it when it is syntactically correct (parentheses, commas, etc). The function can be applied later to different arguments (during the same session).

```
In [2]: f(2)
Out[2]: -0.3333333333333333
```

If you apply the function to an argument for which it does not make sense, Python will return an error message. The following two examples illustrate this. 

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

## If statements

**Conditional logic**, operationalized through **if-then-else** commands, is ubiquitous in computer languages. We will also find this in Python. The shortest version has the following syntax:

```
if condition: action
```

A simple example follows.

```
In [7]: if 3 < 5: print('Minor')
Minor
```

When the action is specified in a different line (or lines), that line has to be indented, as in a `def` statement. See now the syntax for a longer version, with two possible actions:

```
if condition: action1
else: action2
```

An example follows.

```
In [8]: if 3 == 5: print('Equal')
   ...: else: print('Not equal')
Not equal
```

This looks like Excel, right? The Excel version would be `IF(condition, action1, action2)`. An even longer version includes an `elif` (else if) clause:

```
if condition1: action1
elif condition2: action2
else: action3
```

You can add as many `elif` clauses as needed. The foll example follows, with one `elif` clause.

```
In [9]: import math
   ...: if math.sqrt(1) < 1: print('Minor')
   ...: elif math.sqrt(1) == 1: print('Equal')
   ...: else: print('Major')
Equal
```

## While loops

**Loops** are part also common in computer languages. In particular, a `while` loop executes a code chunk until a stopping condition is met. The syntax is:

`while condition: action`

Again, if the action is specified in separate lines, these have to be indented. A simple example follows. Suppose that we wish to find the first integer whose square is higher than 1,000. We start with:

```
In [10]: x = 1
```

Then, we increase `x` until `x**2` exceeds the threshold value:

```
In [11]: while x**2 <= 1000: x = x + 1
```

```
In [12]: x
Out[12]: 32
```

Indeed, we got 32, whose square is 1,024. What if the condition that rules the `while` loop is never met? Then, the loop will go on until you interrupt the process (*Ctrl+C*) or restart the kernel (*Ctrl+.*). An example follows. After entering the input, we have  allowed the process to run for a few seconds.

```
In [13]: x = 1
    ...: while x > 0: x = x + 1
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_40368/2854391691.py in <module>
      1 x = 1
----> 2 while x > 0: x = x + 1

KeyboardInterrupt: 
````

```
In [14]: x
Out[14]: 277583313
```

## For loops

As `while` loops, `for` loops are used to control the repeated execution of a code chunk. But, instead of repeating an action while a condition holds, in the `for` loop the number of repetitions is fixed. The process is controlled by extracting items from a data container, such as a list or a range. A typical syntax would be 

```
for i in list: action
```

A first example follows.

```
In [15]: for i in range(3): print('Hello world!')
Hello world!
Hello world!
Hello world!
```

If the action is specified in one or several separate lines, these have to be indented. Frequently, every execution involves extracting an item from a data container and using it in calculation, as we see in the following example.

```
In [16]: squares = []
    ...: for i in range(1, 5):
    ...:     squares = squares + [i**2]
    ...: squares
Out[16]: [1, 4, 9, 16]
```

## List comprehensions

When the purpose of the `for` loop is to transform a list into another list by means of an expression, you can pack everything in a single formula with a **list comprehension**. For instance, you can create the list of squares in a one shot with:

```
In [17]: [i**2 for i in range(1, 5)]
Out[17]: [1, 4, 9, 16]
```
If you wish to filter out some items from the original list, you can do it with an `if` expression. For instance, suppose that you wish to get a list with the squares of the numbers which are not divisible by 3, up to 20. Taking advantage of the operator `%`, which returns the remainder of the division of two integers, you can use:

```{r eval=FALSE}
In [18]: [i**2 for i in range(1, 21) if i % 3 != 0]
Out[18]: [1, 4, 16, 25, 49, 64, 100, 121, 169, 196, 256, 289, 361, 400]
```
## Homework

1. A **nested list** is a list of lists, that is, a list whose items are lists. For instance, `[[1, 2], [], ['a']]`. Write a function that *flattens* a nested list, transforming it into a new list whose items are the items contained in the items of the original list. Given the above example, that function would return `[1, 2, 'a']`.

2. The **Fibonacci numbers** are 1, 1, 2, 3, 5, 8, 13, 21, etc. Except for the first two terms of this sequence, both equal to 1, every term is the sum of the two preceding terms. Use a loop to calculate the first 10 Fibonacci numbers. Based on that loop, write a function which, given a number, returns a list of Fibonacci numbers of that length.

3. Write a function for **date conversion** that takes '1954-04-30' and returns 'April 30, 1954'. 

4. Write a function that combines strings from two lists, pasting every string from the second list after every string from the first list. For instance, given the lists `['A', 'B']` and `['X', 'Y']`, that function would return the list `['AX', 'AY', 'BX', 'BY']`.

5. Write a function that drops the duplicate items from a list, keeping the order. For instance, given the list `['a'. 'f', 'a', 'b']`, that function would return `['a'. 'f', 'b']`.

6. A year is a **leap year** if it is divisible by 4, unless it is a century year that is not divisible by 400. So, 1800 and 1900 are not leap years while 1600 and 2000 are. Write a function that tells you whether a year is a leap year.

7. The **body mass index** (BMI) is defined as the body mass (kg) divided by the square of the body height (m2). It is used to broadly categorize a major adult person as underweight (under 18.5 kg/m2), normal weight (18.5 to 24.9), overweight (25 to 29.9), or obese (30 or more), or obese. Write a function that takes the heigh and weight of a person, in the adequate units, and returns the categorization underweight/normal weight/overweight/obese.
