# [PY-04] Functions and control statements

## Functions

A **function** takes a collection of **arguments** and performs an action. The functions that appear in this course will **return** a value and, sometimes, **print** a message. Besides the built-in functions like `type` and those coming in the packages that you may import, you can define your own functions. The definition will be forgotten when the session is closed, so you have to include it in your code.

A simple example of a user-defined function follows. Note the indentation after the colon, which is created automatically by the Jupyter interface (either console or notebook).

```
In [31]: def f(x):
    ...:     y = 1/(1 - x**2)
    ...:     return y
```

When you define a function, Python just takes note of the definition, accepting it when it is syntactically correct (parentheses, commas, etc). The function can be applied later to different arguments (during the same session).

```
In [32]: f(2)
Out[32]: -0.3333333333333333
```

If you apply the function to an argument for which it does not make sense, Python will return an error message which depends on the values supplied for the argument.

```
In [33]: f(1)
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
In [34]: f('Mary')
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

Functions can have more than one argument, as in:

```
In [35]: def g(x, y): return x*y/(x**2 + y**2)
````

```
In [36]: g(1, 1)
Out[36]: 0.5
```

Note that, in the definition of `g`, I have used a shorter way. Many programmers would prefer to make it longer, with more than one line, as I did previously for `f`.

## If statements

**Conditional logic**, operationalized through **if-then-else** commands, is ubiquitous in programming. You also have this in Python. The shortest version has the following syntax:

```
if condition: action
```

A simple example follows.

```
In [37]: if 3 < 5: print('Minor')
Minor
```

When the action is specified in a different line (or lines), that line has to be indented, as in a `def` statement. A longer version with two possible actions:

```
if condition: action1
else: action2
```

An example:

```
In [38]: if 3 == 5: print('Equal')
    ...: else: print('Not equal')
Not equal
```

This looks like Excel, right? The Excel version would be `IF(condition, action1, action2)`. An even longer version includes an `elif` (else if) clause:

```
if condition: action1
elif: action2
else: action3
```

You can add as many `elif` clauses as needed. Example:

```
In [39]: if math.sqrt(1) < 1: print('Minor')
    ...: elif math.sqrt(1) == 1: print('Equal')
    ...: else: print('Major')
Equal
```

## While loops

**Loops** are used in practically all programming languages. So, you are already familiar with them if you have programming experience. With loops, you avoid repeating code chunks. In particular, a `while` loop executes a code chunk until a stopping condition is met. The syntax is:

`while condition: action`

Again, if the action is specified in separate lines, these have to be indented. A simple example follows. Suppose that you wish to find the first integer whose square is higher than 1,000. You start with:

```
In [40]: x = 1
```

Then, you increase `x` until `x**2` exceeds the threshold value:

```
In [41]: while x**2 <= 1000: x = x + 1
```

Indeed, you got 32, whose square is 1,024:

```
In [42]: x
Out[42]: 32
```

What if the condition is never met? Then, the loop will go on until you interrupt the process (*Ctrl+C*) or restart the kernel (*Ctrl+.*). An example follows, in which I have allowed the process to run for a few seconds:

```
In [43]: x = 1
    ...: while x > 0: x = x + 1
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_40368/2854391691.py in <module>
      1 x = 1
----> 2 while x > 0: x = x + 1

KeyboardInterrupt: 
````

```
In [44]: x
Out[44]: 277583313
```

## For loops

As `while` loops, `for` loops are used to control the repeated execution of a code chunk. But, instead of repeating an action while a condition holds, in the `for` loop the number of repetitions is fixed. The process is controlled by extracting items from a data container, such as a list or a range. A typical syntax would be 

```
for i in list: action
```

An example:

```
In [18]: for i in range(3): print('Hello world!')
Hello world!
Hello world!
Hello world!
```

If the action is specified in one or several separate lines, these have to be indented. Frequently, every execution involves extracting an item from a data container and using it in calculation. A trivial example:

```
In [19]: squares = []
    ...: for i in range(1, 5):
    ...:     squares = squares + [i**2]
    ...: squares
Out[19]: [1, 4, 9, 16]
```

## List comprehensions

When the purpose of the `for` loop is to transform a list into another list by means of an expression, you can pack everything in a single formula with a **list comprehension**. For instance, you can create the list of squares in a one shot with:

```
In [20]: [i**2 for i in range(1, 5)]
Out[20]: [1, 4, 9, 16]
```
If you wish to filter out some items from the original list, you can do it with an `if` expression. For instance, suppose that you wish to get a list with the squares of the numbers which are not divisible by 3, up to 20. Taking advantage of the operator `%`, which returns the remainder of the division of two integers, you can use:

```{r eval=FALSE}
In [21]: [i**2 for i in range(1, 21) if i % 3 != 0]
Out[21]: [1, 4, 16, 25, 49, 64, 100, 121, 169, 196, 256, 289, 361, 400]
```

## Other data container types

This course only uses lists and ranges, though Python provides other built-in types of data containers. A **tuple** is like a list, but represented with parentheses instead of square brackets:

```
mytuple = ('Messi', 'Cristiano', 'Neymar', 'Coutinho')`
```

A **dictionary** is a set of pairs **key/value**. For instance, the following dictionary contains three features of an individual:

```
mydict = {'name': 'Joan', 'gender': 'F', 'age': 32}`
```

## Homework

1. A **nested list** is a list of lists, that is, a list whose items are lists. For instance, `[[1, 2], [], ['a']]`. Write a function which *flattens* a nested list, transforming it into a new list whose items are the items contained in the items of the original list. Given the above example, that function would return `[1, 2, 'a']`.

2. The **Fibonacci numbers** are 1, 1, 2, 3, 5, 8, 13, 21, etc. Except for the first two terms of this sequence, both equal to 1, every term is the sum of the two preceding terms. Use a loop to calculate the first 10 Fibonacci numbers. Based on that loop, write a function which, given a number, returns a list of Fibonacci numbers of that length.
