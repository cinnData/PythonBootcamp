# [PY-05] Control statements

## If statements

**Conditional logic**, operationalized through **if-then-else** commands, is ubiquitous in computer languages. We will also find this in Python. The shortest version has the following syntax:

```
if condition: action
```

A simple example follows.

```
In [1]: if 3 < 5: print('Minor')
Minor
```

When the action is specified in a different line (or lines), that line has to be indented, as in a `def` statement. See now the syntax for a longer version, with two possible actions:

```
if condition: action1
else: action2
```

An example follows.

```
In [2]: if 3 == 5: print('Equal')
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
In [3]: import math
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
In [4]: x = 1
```

Then, we increase `x` until `x**2` exceeds the threshold value:

```
In [5]: while x**2 <= 1000: x = x + 1
```

After these calculations, we finally get:

```
In [6]: x
Out[6]: 32
```

Indeed, the solution is 32, whose square is 1,024. What if the condition that rules the `while` loop is never met? Then, the loop will go on until you interrupt the process (*Ctrl+C*) or restart the kernel (*Ctrl+.*). An example follows. After entering the input, we have  allowed the process to run for a few seconds.

```
In [7]: x = 1
   ...: while x > 0: x = x + 1
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
/var/folders/40/fkkkv7qd7zj634br7rfl46qh0000gn/T/ipykernel_40368/2854391691.py in <module>
      1 x = 1
----> 2 while x > 0: x = x + 1

KeyboardInterrupt: 
````

```
In [8]: x
Out[8]: 277583313
```

## For loops

As `while` loops, `for` loops are used to control the repeated execution of a code chunk. But, instead of repeating an action while a condition holds, in the `for` loop the number of repetitions is fixed. The process is controlled by extracting items from a data container, such as a list or a range. A typical syntax would be 

```
for i in list: action
```

A first example follows.

```
In [9]: for i in range(3): print('Hello world!')
Hello world!
Hello world!
Hello world!
```

If the action is specified in one or several separate lines, these have to be indented. Frequently, every execution involves extracting an item from a data container and using it in calculation, as we see in the following example.

```
In [10]: squares = []
    ...: for i in range(1, 5):
    ...:     squares = squares + [i**2]
    ...: squares
Out[10]: [1, 4, 9, 16]
```

## List comprehensions

When the purpose of the `for` loop is to transform a list into another list by means of an expression, you can pack everything in a single formula with a **list comprehension**. For instance, you can create the list of squares in one shot with:

```
In [11]: [i**2 for i in range(1, 5)]
Out[11]: [1, 4, 9, 16]
```
If you wish to filter out some items from the original list, you can do it with an `if` expression. For instance, suppose that you wish to get a list with the squares of the numbers which are not divisible by 3, up to 20. Taking advantage of the operator `%`, which returns the remainder of the division of two integers, you can use:

```
In [12]: [i**2 for i in range(1, 21) if i % 3 != 0]
Out[12]: [1, 4, 16, 25, 49, 64, 100, 121, 169, 196, 256, 289, 361, 400]
```
## Homework

1. The **body mass index** (BMI) is defined as the body mass (kg) divided by the square of the body height (m2). It is used to broadly categorize a major adult person as underweight (under 18.5 kg/m2), normal weight (18.5 to 24.9), overweight (25 to 29.9), or obese (30 or more), or obese. Write a function that takes the heigh and weight of a person, in the adequate units, and returns the categorization underweight/normal weight/overweight/obese.

2. To write a function that returns two results  `result1` and `result2`, write `return result1, result2` in the last line of the `def` statement (don't forget the comma). Then the two results will be returned togeteher as a tuple. Write a function that, given a list of integers, returns the number of positive terms and the number of negative terms. Modify the definition so the your function returns a dictionary with keys '`pos` and `neg`.

3. Suppose that you are given an interest rate *r*% for your capital, so that every year your capital gets a *r*% increase. Write a function that, by using a loop, takes *r* and returns the number of years needed to double it. The solution does not depend on the actual value of the capital, so you set it at $1 (this can also be solved mathematically, by using logarithms).

4. The **Fibonacci numbers** are 1, 1, 2, 3, 5, 8, 13, 21, etc. Except for the first two terms of this sequence, both equal to 1, every term is the sum of the two preceding terms. Use a loop to calculate the first 10 Fibonacci numbers. Based on that loop, write a function which, given a number, returns a list of Fibonacci numbers of that length.

5. Write a function that drops the duplicate items from a list, keeping the order. For instance, given the list `['a'. 'f', 'a', 'b']`, that function would return `['a'. 'f', 'b']`.

6. A **nested list** is a list of lists, that is, a list whose items are lists. For instance, `[[1, 2], [], ['a']]`. Write a function that *flattens* a nested list, transforming it into a new list whose items are the items contained in the items of the original list. Given the above example, that function would return `[1, 2, 'a']`.

7. Write a function that combines strings from two lists of the same length, pasting every string from the second list after every string from the first list. For instance, given the lists `['A', 'B']` and `['X', 'Y']`, that function would return the list `['AX', 'AY', 'BX', 'BY']`.
