# [PY-03] Python data containers

## Lists

Python has many **data container** types. The most versatile is the **list**, which is represented as a sequence of comma-separated values inside square brackets. A list can contain items of different type, although this is not frequent. A simple example of a list, of **length** 4, is:

```
In [1]: mylist = ['Messi', 'Cristiano', 'Neymar', 'Haaland']
```

The function `len` returns the length of the list, that is, the number of items contained:

```
In [2]: len(mylist)
Out[2]: 4
```

Empty data containers play a role in Python programming. In particular, the **empty list** `[]`  will appear in the examples of this course. It has zero length:

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

Now, the length of `newlist` is 6:

```
In [5]: len(newlist)
Out[5]: 6
```

## Extracting items from a list

Every item of a list has an **index**. The first item has index 0, the second item has index 1, and so on. An item can be extracted from the list by indicating its index between square brackets. For instance, to extract the first item:

```
In [6]: mylist[0]
Out[6]: 'Messi'
```

The second item is extracted as `mylist[1]`, the third one as `mylist[2]`, etc. Negative indexes mean that we start counting backwards from the end. In particular, the last item can be extracted as `mylist[-1]`:

```
In [7]: mylist[-1]
Out[7]: 'Haaland'
```

Sublists can be extracted with a range of indexes, as in:

```
In [8]: mylist[0:2]
Out[8]: ['Messi', 'Cristiano']
```

Note that `0:2` includes `0` but not `2`. This is a general rule of indexing in Python, the left limit is included but the right limit is not. Other examples:

```
In [9]: mylist[2:]
Out[9]: ['Neymar', 'Haaland']
```

```
In [10]: mylist[:3]
Out[10]: ['Messi', 'Cristiano', 'Neymar']
```

If a third index is specified, it stands for the **step**:

```
In [11]: mylist[0::2]
Out[11]: ['Messi', 'Neymar']
```

In particular, we can reverse a list with a step `-1`:

```
In [12]: mylist[::-1]
Out[12]: ['Haaland', 'Neymar', 'Cristiano', 'Messi']
```

## Membership operators

The **membership operators** `in` and `not in` can be used to check whether an object is contained in a list. Examples:

```
In [13]: yourlist = [4, 7]
    ...: 2 in yourlist
Out[13]: False
```

```
In [14]: 2 not in yourlist
Out[14]: True
```

*Note*. These operators work in the same way for other data containers like ranges or tuples (see below), or NumPy arrays (see lecture Py-05).

## Ranges

A **range** is like a sequence of integers, but the terms of the sequence are not saved as in a list. Instead, only the procedure to create the sequence is saved. The syntax is `myrange = range(start, end, step)`. Example:

```
In [15]: myrange = range(0, 10, 2)
    ...: list(myrange)
Out[15]: [0, 2, 4, 6, 8]
```

Note that the items from a range cannot printed directly. So, I have converted the range to a list here with the function `list`. If, in the specification of a range, the step is omitted, it is assumed to be 1:

```
In [16]: list(range(5, 12))
Out[16]: [5, 6, 7, 8, 9, 10, 11]
```

If the start is also omitted, it is assumed to be 0:

```
In [17]: list(range(10))
Out[17]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Other data container types

This course only uses lists and ranges, though Python provides other built-in types of data containers. A **tuple** is like a list, but represented with parentheses instead of square brackets:

```
In [18]: mytuple = ('Messi', 'Cristiano', 'Neymar', 'Coutinho')
```

```
In [18]: mytuple[-2:]
Out[18]: ('Neymar', 'Coutinho')
```

A **dictionary** is a set of pairs **key/value**. For instance, the following dictionary contains three features of an individual:

```
In [19]: mydict = {'name': 'Joan', 'gender': 'F', 'age': 32}
```

The keys and the values can be extracted as:

```
In [19]: mydict.keys()
Out[19]: dict_keys(['name', 'gender', 'age'])
```
```
In [20]: mydict.values()
Out[20]: dict_values(['Joan', 'F', 32])
```

Or you can extract the value for a certain key as:

```
In [21]: mydict['name']
Out[21]: 'Joan'
```
