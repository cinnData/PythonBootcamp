# [PY-04] Python data containers

## Lists

Python has many **data container** types. The most versatile is the **list**, which is represented as a sequence of comma-separated values inside square brackets. A list can contain items of different type, although this is not frequent. A short example follows.

```
In [1]: mylist = ['Messi', 'Cristiano', 'Neymar', 'Haaland']
```

The function `len` returns the **length** of the list, that is, the number of items it contains:

```
In [2]: len(mylist)
Out[2]: 4
```

Empty data containers play a role in Python programming. In particular, the **empty list** `[]`  has zero length:

```
In [3]: len([])
Out[3]: 0
```

Lists can be concatenated in a very simple way in Python:

```
In [4]: newlist = mylist + [2, 3]
   ...: newlist
Out[4]: ['Messi', 'Cristiano', 'Neymar', 'Haaland', 2, 3]
```

```
In [5]: len(newlist)
Out[5]: 6
```

## Extracting items from a list

Indexing items in a list works the same as indexing characters in a string. See two examples below.

```
In [6]: mylist[0]
Out[6]: 'Messi'
```

```
In [7]: mylist[-1]
Out[7]: 'Haaland'
```

Sublists can be extracted with an interval of indexes, in the same way as we extract substrings from a string. Here, this is called **slicing**. Some examples follow.

```
In [8]: mylist[1:3]
Out[8]: ['Cristiano', 'Neymar']
```

```
In [9]: mylist[2:]
Out[9]: ['Neymar', 'Haaland']
```

```
In [10]: mylist[:3]
Out[10]: ['Messi', 'Cristiano', 'Neymar']
```

Sometimes a third index is specified, which stands for the **step**:

```
In [11]: mylist[0::2]
Out[11]: ['Messi', 'Neymar']
```

In particular, we can reverse a list with a step `-1`:

```
In [12]: mylist[::-1]
Out[12]: ['Haaland', 'Neymar', 'Cristiano', 'Messi']
```

Steps can also be used fro strings, although this is not frequent. 

## Membership operators

The **membership operators** `in` and `not in` are used to check whether an object is contained in a list. Examples:

```
In [13]: yourlist = [4, 7]
    ...: 2 in yourlist
Out[13]: False
```

```
In [14]: 2 not in yourlist
Out[14]: True
```

*Note*. These operators work in the same way for other data containers like ranges or tuples (see below), or NumPy arrays (see lecture PY-06).

## Strings as sequences

In Python, strings and lists are two types of **sequences** and, indeed, a string is managed as a list of characters. Nevertheless, there are some differences which rae worth to be mentioned. First, using the square brackets with a string produces always a substring. But slicing a list produces a sublist, and it is not the same as extracting items from the list. The following examples illustrate this.

```
In [15]: mylist[2:3]
Out[15]: ['Neymar']
```

```
In [16]: mylist[2]
Out[16]: 'Neymar'
```

Another difference is found in the use of `in`. For a stringl, it indicates that a string is contained in another string. But, fora list, it indicates that an object is among the items of that list:

```
In [17]: 'Neymar' in mylist
Out[17]: True
```

Finally, though lists and strings share some functions like `len()`, they have different methods. We have mentioned `.replace()` and `.lower()` as examples of string methods. An example of **list method** is `.append()`, which adds an item at the end of a list, *in place*, that is without returning the new version). This is iullustrated by the following example.

```
In [18]: mylist.append('Vinicius')
    ...: mylist
Out[18]: ['Messi', 'Cristiano', 'Neymar', 'Haaland', 'Vinicius']
```

Note that we get the same output with the input `mylist = mylist + ['Vinicius']`.

## Ranges

A **range** is like a sequence of integers, but the terms of the sequence are not stored in the virtual memory of your computer. Instead, only the procedure to create the sequence is retained. The syntax is `myrange = range(start, stop, step)`. An example follows.

```
In [19]: myrange = range(0, 10, 2)
    ...: list(myrange)
Out[19]: [0, 2, 4, 6, 8]
```

Note that the terms of a range cannot printed directly. So, we have converted the range to a list here with the function `list()`. If, in the specification of a range, the parameter `step` is omitted, it is assumed to be 1:

```
In [20]: list(range(5, 12))
Out[20]: [5, 6, 7, 8, 9, 10, 11]
```

If `start` is also omitted, it is assumed to be 0:

```
In [21]: list(range(10))
Out[21]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Other data container types

Python provides other built-in types of data containers, which are less relevent for this course. A **tuple** is like a list, but represented with parentheses instead of square brackets:

```
In [22]: mytuple = ('Messi', 'Cristiano', 'Neymar', 'Coutinho')
```

```
In [23]: mytuple[-2:]
Out[23]: ('Neymar', 'Coutinho')
```

A **dictionary** is a set of pairs **key/value**. For instance, the following dictionary contains three features of an individual:

```
In [24]: mydict = {'name': 'Joan', 'gender': 'F', 'age': 32}
```

The keys and the values can be extracted as:

```
In [25]: mydict.keys()
Out[25]: dict_keys(['name', 'gender', 'age'])
```
```
In [26]: mydict.values()
Out[26]: dict_values(['Joan', 'F', 32])
```

Or you can extract the value for a certain key as:

```
In [27]: mydict['name']
Out[27]: 'Joan'
```

## Mutability

You may wonder what is the benefit of having both lists and tuples in Python. The difference is that lists are **mutable**, while tuples are not, and this is useful to programmers. Mutating a list allows us to update the content, as we see in the following example.

```
In [27]: mylist[1] = 'Benzema'
    ...: mylist
Out[27]: ['Messi', 'Benzema', 'Neymar', 'Haaland', 'Vinicius']

```

So, Python programmers can use tuples as data containers whose content is not going to change. Tuples also appear in the output returned by the Python kernel, as you will see in many examples. 

The content of a dictionary can also be updated. Two examples follow.

```
In [28]: mydict['job'] = 'Engineer'
    ...: mydict
Out[28]: {'name': 'Martha', 'gender': 'F', 'age': 32, 'job': 'Engineer'}
```

```
In [29]: mydict['name'] = 'Martha'
    ...: mydict
Out[29]: {'name': 'Martha', 'gender': 'F', 'age': 32, 'job': 'Engineer'}
```

## Homework

Write a list containing the month names and use it to create a function for **date conversion** that takes '1954-04-30' and returns 'April 30, 1954'.
