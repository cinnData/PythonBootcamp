# [PY-03] Python data containers

## Lists

Python has many **data container** types. The most versatile is the **list**, which is represented as a sequence of comma-separated values inside square brackets. A list can contain items of different type, although this is not frequent. A short example follows.

```
In [1]: mylist = ['Messi', 'Cristiano', 'Neymar', 'Haaland']
```

The function `len` returns the **length** of the list, that is, the number of items contained:

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

Extracting a sublist in this way is called **slicing**. Slicing a list produces a sublist, and it is not the same as extracting items from the list. The following examples illustrate this.

```
In [13]: mylist[2:2]
Out[13]: []
```

```
In [14]: mylist[2:3]
Out[14]: ['Neymar']
```

```
In [15]: mylist[2]
Out[15]: 'Neymar'
```

## Membership operators

The **membership operators** `in` and `not in` are used to check whether an object is contained in a list. Examples:

```
In [16]: yourlist = [4, 7]
    ...: 2 in yourlist
Out[16]: False
```

```
In [17]: 2 not in yourlist
Out[17]: True
```

*Note*. These operators work in the same way for other data containers like ranges or tuples (see below), or NumPy arrays (see lecture PY-05).

## Strings as sequences

In Python, strings and lists are two types of **sequences**, and, in some sense, a string is manged as a list of characters. Take, for instance, the following string.

```
In [18]: myplayer = 'Leo Messi'
```

The function `len` gives us the number of characters.

```
In [19]: len(myplayer)
Out[19]: 9
```

Slicing a string produces a **substring**:

```
In [20]: myplayer[:3]
Out[20]: 'Leo'
```

We concatenate strings with the plus sign (`+`):

```
In [21]: myplayer[4:] + ', the best player in the world'
Out[21]: 'Messi, the best player in the world'
```

A difference between strings and lists is found in the use of `in`. For a list, it indicates that an object is among the elements of that list. For strings, that a string is contained in another string, as we see here:

```
In [22]: 'Leo' in myplayer
Out[22]: True
```

## Ranges

A **range** is like a sequence of integers, but the terms of the sequence are not stored in the virtual memory of your computer. Instead, only the procedure to create the sequence is retained. The syntax is `myrange = range(start, stop, step)`. An example follows.

```
In [23]: myrange = range(0, 10, 2)
    ...: list(myrange)
Out[23]: [0, 2, 4, 6, 8]
```

Note that the terms of a range cannot printed directly. So, we have converted the range to a list here with the function `list`. If, in the specification of a range, the parameter `step` is omitted, it is assumed to be 1:

```
In [24]: list(range(5, 12))
Out[24]: [5, 6, 7, 8, 9, 10, 11]
```

If `start` is also omitted, it is assumed to be 0:

```
In [25]: list(range(10))
Out[25]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Other data container types

Python provides other built-in types of data containers, which are less relevent for this course. A **tuple** is like a list, but represented with parentheses instead of square brackets:

```
In [26]: mytuple = ('Messi', 'Cristiano', 'Neymar', 'Coutinho')
```

```
In [27]: mytuple[-2:]
Out[27]: ('Neymar', 'Coutinho')
```

A **dictionary** is a set of pairs **key/value**. For instance, the following dictionary contains three features of an individual:

```
In [28]: mydict = {'name': 'Joan', 'gender': 'F', 'age': 32}
```

The keys and the values can be extracted as:

```
In [29]: mydict.keys()
Out[29]: dict_keys(['name', 'gender', 'age'])
```
```
In [30]: mydict.values()
Out[30]: dict_values(['Joan', 'F', 32])
```

Or you can extract the value for a certain key as:

```
In [31]: mydict['name']
Out[31]: 'Joan'
```

## Mutability

You may wonder what is the benefit of having both lists and tuples in Python. The difference is that lists are **mutable**, while tuples are not, and this is useful to programmers. Mutating a list allows us to update the content, as we see in the following example.

```
In [32]: mylist[1] = 'Benzema'
    ...: mylist
Out[32]: ['Messi', 'Benzema', 'Neymar', 'Haaland']

```

So, Python programmers can use tuples as data containers whose content is not going to change. Tuples also appear in the output returned by the Python kernel, as you will see in many examples. 

The content of a dictionary can also be updated. Two examples follow.

```
In [33]: mydict['job'] = 'Engineer'
    ...: mydict
Out[33]: {'name': 'Martha', 'gender': 'F', 'age': 32, 'job': 'Engineer'}
```

```
In [34]: mydict['name'] = 'Martha'
    ...: mydict
Out[34]: {'name': 'Martha', 'gender': 'F', 'age': 32, 'job': 'Engineer'}
```

Strings are changed in a completely different way, with the ?find and replace' approach that we use in word processors.

```
In [35]: myplayer.replace('Leo', 'Lionel')
Out[35]: 'Lionel Messi'
```
