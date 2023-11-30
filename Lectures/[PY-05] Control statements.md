# [PY-05] Control statements

## If statements

You have probably found **conditional logic** in your computer experience. An example is the Excel function `IF()`. Conditional logic can shows up in certain code chunks, which programmers call **if-then-else commands**. Different languages have various syntax rules for these commands. This section explains the Python rules. 

The simplest version of this is the **if conditional** is the made of a single `if` statement that specifies a condition and an action that must be executed when the condition is satisfied. The Python syntax is as follows.

```
if condition:
    action
```

As in the definition of a function, indentation follows the colon, and indicates that the indented line is part of the `if` statement. The condition in this statement can be any expression that the Python kernel evaluates as a Bolean `True`/`False`. The action can be of various types, typically defining (or redefining) a variable or printing a message. A simple example follows.

```
In [1]: grade = 9
   ...: if grade >= 5:
   ...:     print('Congratulations!')
Congratulations!
```

A bit more complex is the **if-else conditional**, which is made of an `if` statement followed by an `else` statement specifying an alternative action in case the `if` condition is false. The syntax is as follows.

```
if condition:
    action1
else:
    action2
```

In Excel, this would be `IF(condition, action1, action2)`. An example follows.

```
In [2]: if grade >= 5:
   ...:     print('PASS')
   ...: else:
   ...:     print('FAIL')
PASS
```

Note that the `else` line is not indented, meaning that it starts a new statement, even if this new statement must be included in the same input as the `if`statement to make sense.

A further refinement, the **if-elif-else conditional**, admits more than two actions. In Python, `elif` means 'else if'. The syntax, for a conditional with a single `elif` statement, would be as follows.

```
if condition1:
    action1
elif condition2:
    action2
else:
    action3
```

You can add as many `elif` statements as needed. Note tha the `elif` and `else` lines are not indented. An example, with one `elif` statement, follows.

```
In [3]: if grade >= 8:
   ...:    print('A')
   ...: elif grade >= 5:
   ...:    print('B')
   ...: else:
   ...:    print('C')
A
```

The conditions are evaluated by order, so they don't need to be exclusive. In this example, the Python first evaluates the expression. Since the outcome is `True`, it stops there.

If the `else` statement is omitted (this would be an if-elif conditional), no acion is taken when the `if` and `elif` conditions are false. An example follows.

```
In [4]: grade = 3
   ...: if grade >= 8:
   ...:    print('Good!')
   ...: elif grade >= 5:
   ...:    print('Keep working!')
```

## While loops

**Loops** are part also common in computer languages. In particular, a `while` loop executes a code chunk until a stopping condition is met. The syntax is:

`while condition:
    action`

Indentation after the colon works as in other cases. A simple example of a `while` loop follows. Suppose that we wish to find the first integer whose square is higher than 1,000. We start with 1, and keep increasing the number until the square exceeds 1,000. 
```
In [5]: x = 1
   ...: while x**2 <= 1000:
   ...:     x = x + 1
   ...: x
Out[5]: 32
```

Indeed, the solution is 32, whose square is 1,024. Note that only the third line is indented, to indicate that it is part of the loop.

What happens when the `while` condition is never met? Then the loop will go on until we interrupt the process (*Ctrl+C*) or restart the kernel (*Ctrl+.*). An example follows. After entering the input, we have  allowed the process to run for a few seconds.

```
In [6]: x = 1
   ...: while x > 0:
   ...:     x = x + 1
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
Cell In[6], line 2
      1 x = 1
----> 2 while x > 0:
      3     x = x + 1

KeyboardInterrupt: 
```
Now, depending on the time the process has been allowed to run, we get a higher or lower result.

```
In [7]: x
Out[7]: 277583313
```

## For loops

As the `while` loops, the `for` loops are used to control the repeated execution of a code chunk. But, instead of repeating an action while a condition holds, in the `for` loop the number of repetitions is fixed. The process is controlled by extracting items from a data container, such as a list or a range. The syntax is as follows.

```
for i in list:
    action
```

The colon works as other cases. A first example:

```
In [8]: for i in range(3):
   ...:     print('Hello world!')
Hello world!
Hello world!
Hello world!
```

Frequently, every execution involves extracting an item from a data container and using it in calculation, as we see in the following example.

```
In [9]: squares = []
   ...: for i in range(1, 5):
   ...:     squares = squares + [i**2]
   ...: squares
Out[9]: [1, 4, 9, 16]
```

## List comprehensions

When the purpose of the `for` loop is to transform a list into another list by means of an expression, you can pack everything in a single formula with a **list comprehension**. For instance, you can create the list of squares in one shot with:

```
In [10]: [i**2 for i in range(1, 5)]
    ...: squares
Out[10]: [1, 4, 9, 16]
```
If you wish to filter out some items from the original list, you can do it by including an `if` statement inside the brackets. For instance, suppose that you wish to get a list with the squares of the numbers which are not divisible by 3, up to 20. Taking advantage of the operator `%`, which returns the remainder of the division of two integers, you can use the following list comprehension.

```
In [11]: my_squares = [i**2 for i in range(1, 21) if i%3 != 0]
    ...: my_squares
Out[11]: [1, 4, 16, 25, 49, 64, 100, 121, 169, 196, 256, 289, 361, 400]
```

## Homework

1. The **body mass index** (BMI) is defined as the body mass (kg) divided by the square of the body height (m2). It is used to broadly categorize a major adult person as underweight (under 18.5 kg/m2), normal weight (18.5 to 24.9), overweight (25 to 29.9), or obese (30 or more), or obese. Write a function that takes the heigh and weight of a person, in the adequate units, and returns the categorization underweight/normal weight/overweight/obese.

2. In databases, names are usually split in two or more columns. In US, we usually find three columns, such as `firstname`, `midname` and `lastname`. When the name has to be printed, the three pieces are pasted together. Write a function for this job. If the arguments supplied are `firstname='Donald'`, `midname='John'` and `lastname='Trump'`, the function would return `'Donald John Trump'`. But it should work also for the cases in which the middle name is omitted, which is not rare, in particular for foreign people.

3. Write a function that, given a list of integers, returns the number of positive terms and the number of negative terms. Modify the definition so the your function returns a dictionary with keys '`positive` and `negative`. So, given the list `[2, 3, -7, 0]`, your function must return `{'positive': 2, 'negative': 1}`.

4. Suppose that you are given an interest rate *r*% for your capital, so that at the end of every year your capital gets a *r*% increase. For instance if the capital is $1 and the interest rate is 10% (`r=0.1`), after one year you have $1.10, after two years $1.21, etc. Write a function that, by using a loop, takes *r* and returns the number of years needed to double it. The solution does not depend on the actual value of the capital, so you set it at $1 (this can also be solved mathematically, by using logarithms).

5. The **Fibonacci numbers** are 1, 1, 2, 3, 5, 8, 13, 21, etc. Except for the first two terms of this sequence, both equal to 1, every term is the sum of the two preceding terms. Use a loop to calculate the first 10 Fibonacci numbers. Based on that loop, write a function which, given a number, returns a list of Fibonacci numbers of that length.

6. A **prime** is a positive integer greater than 1 that is not a product of two smaller positive integers. Starting with a list `primes = 2]`, use a loop for building the list of primes lower than 100. The number 100 of course can be replaced ny any other number, so you would probably be able to write a function that takes an integer `n` and returns the numer of primes lower than `n`.

7. Going back to exercise 4 of lecture PY-03, create a list containing the leap years of the 20th century.

8. Write a function that drops the duplicate items from a list, keeping the order. For instance, given the list `['a', 'f', 'a', 'b']`, that function would return `['a', 'f', 'b']`.

9. A **nested list** is a list of lists, that is, a list whose items are lists. For instance, `[[1, 2], [], ['a']]`. Write a function that *flattens* a nested list, transforming it into a new list whose items are the items contained in the items of the original list. Given the above example, that function would return `[1, 2, 'a']`.

10. Write a function that combines strings from two lists of the same length, pasting every string from the second list after every string from the first list. For instance, given the lists `['A', 'B']` and `['X', 'Y']`, that function would return the list `['AX', 'AY', 'BX', 'BY']`.
