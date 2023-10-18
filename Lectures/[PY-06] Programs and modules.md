# [PY-06] Programs and modules

## The working directory

The **working directory** is just a file path on your computer that sets the default location of any files you read into Python. It is easy to change the working directory, as we will see below. Jupyter Qt Console starts always with the same working directory, while the working directory for a Jupyter notebook is the folder where the notebook is. 

Assuming that you are working in Qt Console with a Mac computer, the working directory will be `/Users/username` (the username is the one you use in that computer). The **magic command** `%pwd` (not part of Python) provides this information.

```
In [1]: %pwd
Out[1]: '/Users/username'
```
In a Windows computer, the Python kernel would have printed `C:\\Users\\username`. The double backslash is a trick that Python uses to differentiate between the role that this symbol plays in Python and its role as part of a string.

We can easily change the working directory with another magic command. Let us suppose that, for this course, you have created the folder `py_course` in the initial working directory. Then you can set this folder as the working directory as follows.

```
In [2]: %cd py_course
/Users/miguel/py_course
```

```
In [3]: %pwd
Out[3]: '/Users/miguel/py_course'
```

So, right now, in the Mac computer where this is prepared, in Qt Console, the **working directory** is `/Users/miguel`. In a Windows computer, the Python kernel would have printed `C:\\Users\\miguel`. Note that, if the source file is somewhere inside the working directory, this part of the path can be omitted. This is called a **relative path**.

## Program 1

A **computer program** is a sequence or set of instructions in a programming language for a computer to execute. Python programs can be executed in many ways, not only in isolated way, as we will do here, but also being called from an app. Under this perspective, Python programs are easy to associate to various apps and computer processes (this may be the reason why you're learning Python).

When you are learning Python, you can run a program from the shell, which is what most books and tutorials assume that you will do but we will not use this approach here, using instead the console. So, we will have a unique way that works in both Mac and Windows computers. 

First of all, we write our program, that would be the simplest program in the world, one that greets you. The program will be just the string:

```
print('\nHi, there!\nThis is the Python Course!')
```

We can execute this first in the usual way:

```
In [4]: print('\nHi, there!\nThis is the Python Course!')

Hi, there!
This is the Python Course!

```

Note the **line feed** control character `\n`, which, when printed, opens a new line. It is inserted here for aesthetic reasons. We write our string in a text file, saving it with the name `program1.py` in the folder `py_course`, which is our current working directory. So the Python kernel will not have any problem finding that file.

We can execute the program in the console with the function `runfile()`. This function is not part of Python, but a function that can be used in certain environments like the Jupyter apps or Spyder

```
In [5]: runfile('program1.py')

Hi, there!
This is the Python Course!
```

## input statements

After this supersimple example, we see now how to create an interactive program, allowing for the user to provide inputs. In Python, this can be done in easy way, with the built-in function `input`. Let us see a first example. 

```
In [6]: input('\nDo you know Python? (y/n) ')

Do you know Python? (y/n) y
Out[6]: 'y'
```

This function takes an argument wich is printed on the screen as a **prompt**. Then, the input entered by the user is returned so it can be processed by your program. Before doing that, let us reamrk that `input()` always returns a string, so if we need a number for some calculation, we have to change the data type. See a new example below.

```
In [7]: int(input('\nWhat is your age? '))

What is your age? 25
Out[7]: 25
```

## Program 2

We write now an interactive program involving the function `input()`:

```
answer = input('\nDo you know Python? (y/n) ')

if answer == 'y':
    print('\nCool!!')
else:
    print('\nSorry about that.')
```

The flow is clear. First, the user input 'y' or 'n'. Based on the input, the program prints a sentence. We write our program in the file `program2.py`, which we put in the folder `py_course`. Now, we can execute it with `runfile()`.

```
In [8]: runfile('program2.py')

Do you know Python? (y/n) n

Sorry about that.
```

## Modules

Python modules store additional resources. Though they can contain more complex stuff, we restrict ourselves to modules that contr¡tain function definitions. These modules can be imported with an `import` statement. Modules can be downloaded from Internet sources and installed as packages with a `pip install`statement. 

Though this may seem very technical, it is not that difficult, at least for small modules. We illustrate the concept here by creating a very small module, containing a single function definition (from the homework of lecture PY-05).

```
def has_zero(x, y, z):
    if x == 0 or y == 0 or z == 0:
        return True
    else:
        return False
```

We write this definition in the file `myfuncs.py`, which we put in the folder `py_course`. Now, we can import it.

```
In [9]: import myfuncs
```

Since the module is in the working directory, the Python kernel can find it. Of course this is not what the package manager of a Python distribution does. It puts them in a special folder and modifies the path of the shell so the files can be found. But this is just a technicality.

Note that now, we can use our function, calling it as `myfuncs.has_zero()`. This is no news for you. 

```
In [10]: myfuncs.has_zero(1, -2, 0)
Out[10]: True
```

We can also import this function with a specific `import` statement.

```
In [11]: from myfuncs import has_zero
```

Now the function can be called without specifying the module:

```
In [12]: has_zero(1, -2, 3)
Out[12]: False
```

## Homework

1. The first question of the homework of lecture PY-05 was concerned with calculating the body mass index (BMI), in numeric and categorical scales. Write a program thats asks the user his/her height and weight, specifying the units, and prints *Your BMI is ---, so you are classified as ---*.
