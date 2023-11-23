# [PY-02] Starting with Python 

## Typing Python code

This lecture is a tutorial whose objective is to get familiar with the way in which users interact with a Python kernel. This section comments how to type Python code. Before starting, a reminder: Python is **case sensitive**. 

Let us assume that you are working on Jupyter Qt Console. The console produces **input prompts** (such as `In[1]:`), where you can type a command and press *Return*. The console responds with either the corresponding **output** (preceded by `Out[1]:`), an **error message** or no answer at all. Error messages are typically long and unfriendly. 

A simple example follows. Note the white space in the input, around the *plus* sign (`+`), which is ignored by the Python interpreter, but improves the **readability** of our code.

```
In [1]: 2 + 2
Out[1]: 4
```

So, if you enter `2 + 2`, the output will be the result of this calculation. But, if you want to store this result for later use (in the same session), you will enter it with a name, as follows:

```
In [2]: a = 2 + 2
```

This creates the **variable** `a`, whose **value** is 4. Note that the result of `2 + 2` is not outputted now. But you can call it:

```
In [3]: a
Out[3]: 4
```

In Pyhton, you can assign a new value to an existing variable. The previous value is then forgotten:

```
In [4]: a = 7 - 2

In [5]: a
Out[5]: 5
```

Suppose that you copypaste in the console code chunks from a text editor. This is what you would do if you were working in the console, so you could readily save your code. You can so input several code lines at once. In that case, the console only shows the output for the last line of the input. An example follows.

```
In [6]: b = 2 * 3
   ...: b - 1
   ...: b**2
Out[6]: 36
```

*Note*. You would probably have written `b^2` for the square of 2, but the caret symbol (`^`) plays a different role in Python.

If you are typing the code in the console, you can open a new line within the same input with *Ctrl+Return*. You can then finish the input, calling for the output, by pressing *Return*. If the cursor is not at the end of the last line, you have to press *Shift+Return* to finish the input. 

Typing in a notebook is just a bit different. The notebook is a sequence of **cells**. There two type of cells, the Markdown cells and the code cells. In the **Markdown cells**, you write comments, while in the **code cells** you write the Python commands. Every code cell of the notebook corresponds to an input of the console. When you are typing in a cell, pressing *Return* starts a new line *within the same cell*, without ending the input. With *Shift+Return*, you finish the the input, so you get the ouput, opening a new cell. To finish the input without opening a new cell, use *Cmd+Return* in Mac or *Ctrl+Return* in Windows.   

## Python packages

Additional Python resources come in **packages**. For instance, suppose that you want to do some math, calculating the square root of 2. You will then **import** the package `math`, whose resources include the square root and many other mathematical functions. Once the package has been imported, all its functions are available, so you can call the function as `math.sqrt()`. This notation indicates that `sqrt()` is a function of the module `math`.

In the console, the square root calculation appears as:

```
In [7]: import math
   ...: math.sqrt(2)
Out[7]: 1.4142135623730951
```

Alternatively, you can import only the functions that you plan to use, and call them without specifying the package:

```
In [8]: from math import sqrt
   ...: sqrt(2)
Out[8]: 1.4142135623730951
```

Packages are imported just for the current kernel. You can import a package only if it is already **installed** in your computer. 

*Note*. This course follows the common practice in Python learning materials of writing functions as *func()*. The parentheses remind you that this is an object that takes arguments.

## Numeric data types

As in other languages and applications, data can have different **data types** in Python. The data type can be learned with the function `type()`. Let us start with the numeric types. First, the **integers** have type `int`:

```
In [9]: type(2)
Out[9]: int
```

Another numeric type is that of **floating-point** numbers (`float`):

```
In [10]: type(2.4)
Out[10]: float
```

Note that, in Python, integers are not, as in the mathematics textbook, a subset of the real numbers, but a different type. We also have **Boolean** (`bool`) data, which are either `True` or `False`:

```
In [11]: type(True)
Out[11]: bool
```

Some languages, like Python and Java, have Booleans, but others, like C++, don't. The same with applications, Excel has Booleans but MySQL doesn't. When there are no Booleans, they are replaced by 1 and 0. In Python, `True` and `False` are the same as 1 and 0 for many purposes, as we will see below.

*Note*. It is `True` and `False` in Python, not `TRUE` and `FALSE` (as in R), nor `true` and `false` (as in Java). Python is case sensitive.

## Strings

Besides numbers, we can also manage **strings** with type `str`:

```
In [12]: type('Messi')
Out[12]: str
```

Strings are always enclosed by quote marks, either single or double (but same way on both sides). In Python, a string is a sequence of **characters**. The number of characters is the **length** of the string, which can be obtained with the function `len()`. A string can have any length. This includes the **empty string**, which has zero length.

```
In [13]: len('Messi')
Out[13]: 5
```


Strings can be concatenated in a straightforward way:

```
In [14]: myplayer = 'Leo ' + 'Messi'
    ...: myplayer
Out[14]: 'Leo Messi'
```

## Characters 

The characters contained in a string can be the (English) alphanumeric characters, but also **special characters** like white space, punctuation, etc. Other symbols, like emoticons, can also appear in your data, specially in social networks data. Besides that, you can also manage letters from other languages (Spanish, Portuguese, etc) or alphabets (Cyrillic, hiragana, etc), and even ideographs (such as Han characters). 

There is a basic set of 128 characters, called the **ASCII characters**, which are encoded as numbers (from 0 to 127) in the same way by all the computers. They include the English letters (without accents), the numbers, basic punctuation (but not curly quote marks or long dashes), white space, **control characters** such as the new line, represented in many computer languages (including Python) as `\n`, and other symbols familiar to you, such as the dollar (`$`) and the hash (`#`) symbols. The complete list can be easily found in Internet.

Non-ASCII characters can be encoded by different computers or different text editors in different ways. If you capture string data on your own, you will probably find some of these characters in your data. Even when the documents are expected to be in English, they can be contaminated by other languages: Han characters, German dieresis, Spanish eñe, etc.

The preferred **encoding** is **UTF-8**, used by Python. UTF-8 is the default encoding in Mac computers, but not in Windows computers, which use a region-specific system. In US and Western Europe, this is **Windows-1252**. The UTF-8 encoding can be easily learned from the Python interpreter. For instance, for the lowercase 'a':

```
In [15]: ord('a')
Out[15]: 97
```
The uppercase 'A' is:

```
In [16]: ord('A')
Out[16]: 65
```

And the Spanish 'ñ' is:

```
In [17]: ord('ñ')
Out[17]: 241
```

This goes beyond 127, so 'ñ' is not an ASCII character. If you include it in a document, it may look wrong in another computer.

## Substrings

Let us see how we can extract a **substring** from a string. Every character in a string has an index. Starting from the left, the indexes are 0, 1, 2, 3, $\dots$, so the first character has index 0 (not 1), the second character has index 1, etc. Starting from the right the indexes are -1, -2, -3, $\dots$, so the last character has index -1, the penultimate character has index -2, etc. You can extract any character (as a substring of length 1). Let us see some examples.

```
In [18]: myplayer[2]
Out[18]: 'o'
```

```
In [19]: myplayer[-3]
Out[19]: 's'
```

Longer substrings can be extracted by specifying a **slice** of indexes, as we see in the following example. Note that a slice `start:end` includes `start`, but not `end`. This is a Python notational convention that may confound you.

```
In [20]: myplayer[4:7]
Out[20]: 'Mes'
```

If `start` is missing, the substring starts at the first character. If `end` is missing, the substring ends at the last character (included). This is illustrated in the examples below.

```
In [21]: myplayer[:3]
Out[21]: 'Leo'
```

```
In [22]: myplayer[4:]
Out[22]: 'Messi'
```

## Type conversions

The functions `int()` and `float()` can be used to convert numbers from one type to another type (occasionally at a loss):

```
In [23]: float(2)
Out[23]: 2.0
```

```
In [24]: int(2.3)
Out[24]: 2
```

Sometimes, you can convert strings to numbers:

```
In [25]: int('27')
Out[25]: 27
```

```
In [26]: float('27')
Out[26]: 27.0
```

On the other hand, numbers can always be converted to strings:

```
In [27]: str(27)
Out[27]: '27'
```

Booleans can be converted to `int` and `float` type with the functions mentioned above. Also, to make operations with numbers possible when they have different types, they are automatically converted to common type. In the following examples Booleans are converted on the fly.

```
In [28]: 1 + True
Out[28]: 2
```

```
In [29]: math.sqrt(False)
Out[29]: 0.0
```

## Comparison operators

Let us see how the **comparison operators** work in Python. For instance, the *lower than* symbol (`<`):

```
In [30]: 5 < a
Out[30]: False
```

When you input an expression involving a comparison operator, Python evaluates it, returning either `True` or `False`. The following example uses the **equality operator**, which is denoted in Python by a double equal sign (`==`)).

```
In [31]: a == 7
Out[31]: True
```

Why two equal signs? The reason is that a single equal sign is used to assign names. So `a = 7` would be interpreted by the Python kernel, not as asking whether `a` is equal to `7`, but as creating a variable named `a` whose value is `7`. 

The *not equal* operator is denoted by an equal sign preceded by an admiration symbol (`!`):

```
In [32]: a != 4
Out[32]: False
```

Strings can also be compared (though not to numbers):

```
In [33]: 'a' >= 'A'
Out[33]: True
```

Why is this? Because this inequality is true for the numbers that encode these characters, which we have learned above. Finally, numbers and booleans can be compared irrespective of their types:

```
In [34]: 3 == 3.0
Out[34]: True
````

```
In [35]: 0.7 < True
Out[35]: True
```

## Logical operators

The **logical operators** allow operations between booleans. They are `and`, `or` a `not`. They work in the same way as in other languages: 

* `x and y` is true when both `x` and `y` are true. 

* `x or y` is true when at least one of them is true

* `not x` is true when `x` is false. 

Some examples follow.

```
In [36]: True and False
Out[36]: False
```

```
In [37]: True or False
Out[37]: True
```

```
In [38]: not True
Out[38]: False
```

Since expressions involving comparison operators are evaluated by the Python kernel and turned into either `True` or `False`, we can combine them by means of logical operators. Example:

```
In [39]: 5 < 7 and ' ' <= '6'
Out[39]: True
```

## Homework

1. Calculate the square root of 2 and take the square of it. Do you get 2? Why?

2. Evaluate the expressions `1/3 + 1/3 + 1/3 + 1/3 == 4/3` and `1/3 + 1/3 + 1/3 + 1/3 + 1/3 == 5/3`. One is true and the other one is false. Is Python crazy?

3. Write a string that is lower than any other string.

4. You will probably agree that $3 + (4 \times 5) = 23$ and $(3 + 4) \times 5 = 35$, and that the first identity can be written as $3 + 4 \times 5 = 23$, so the parenthesis is not needed, because it is understood that the product takes **precedence** over the sum. Now, what is `True or True and False`? Which operator has precedence, `and` or `or`? Another one: what is `not False or True`?

5. Which type have `True*True` and `True/True?` What is the rule?

6. Is `1 == True` true or false? What is the rule? 

7. Print the following strings with the function `print()`. Some of them will work and some will not. Can you explain the differences?

```
"Donald Trump and Joe Biden'

'''Donald Trump and Joe Biden'''

'Donald Trump 
and Joe Biden'

'Donald Trump\nand Joe Biden'

'Donald Trump \
and Joe Biden'

'''Donald Trump
and Joe Biden'''
```

8. The package `langid` is one of them many options for **language detection** in Python. You can install it entering `pip install langid` in either the shell or the console. Once it has been installed, you can import it and use the function `langid.classify()` to "detect" the language. Try this with a few sentences in different languages. Please, note that `langid` gets better with longer strings, but often fails with very short ones. Though it may look like a dwarf when compared to a giant like GPT-4, it is a nice example of **machine learning**.
