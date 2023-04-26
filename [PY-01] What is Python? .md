# [PY-01] What is Python? 

## What is Python?

**Python** is a programming language, introduced in 1991. The latest stable version (when this is being written) is Python 3.11. To work with Python, you will pick an interface to a **Python interpreter** among the many available choices. You can have several instances of the interpreter, called **kernels**, running independently in your computer.

Warning: Python is **case sensitive**. For instance, `type` is a Python function which returns the type of an object, but `Type` is not recognized (unless you create a new object with this name), and will return an error message.

## Python modules and packages

Many additional resources have been added to Python in the form of **modules**. A module is just a text file containing Python code. Modules are grouped in **libraries**. The **Python Standard Library**, which is distributed with Python, contains **built-in modules** providing standardized solutions for many problems that occur in everyday programming. For instance, `math` provides mathematical functions, and `datetime` functions for manipulating dates and times.

Other libraries are typically called **packages**, because their elements are packed according to some specific rules which allow you to install and call them together. Python can be extended by more than 300,000 packages. Some big packages are not single modules, but collections of modules, which are then called **subpackages**.

Since the basic Python toolkit (without any module) is quite limited, you will need to **import** additional resources for practically everything. Once the module has been imported, all its functions are available. Modules are imported just for the current kernel. You can only import from the standard library or from packages which are already **installed** in your computer. 

Mind that, since Python is an open source project, packages are contributed by various agents, such as university professors, freelance programmers, or industry behemoths like Google. Any package has different versions and it can have dependencies on other packages.

## Python distributions

A **Python distribution** is a software bundle, which contains a Python interpreter and the standard library. Python distributions also have package managers for installing, uninstalling or updating packages. All distributions have a **package manager** called `pip`, and some distributions have a specific manager.

Python distributions provide various interfaces to the Python interpreter All include a **command line interface** (CLI), which may be a shell-like application or an **integrated development environment** (IDE). A Python IDE provides a Python-aware code editor integrated with the ability to run code from that editor.

## The Anaconda distribution

In the data science community, **Anaconda** (`anaconda.com`) is the favorite distribution. The current Anaconda distribution comes with Python 3.10. Anaconda provides all the packages used in this course, so no extra installation is needed. Anyway, Anaconda has a specific package manager, called `conda`. You may need `conda` for more advanced work, because it reviews the packages that are already installed in our computer, keeping track of the dependencies, and solving version conflicts between packages.

Downloading and installing Anaconda leaves you with the **Anaconda Navigator**, which opens in the browser and allows you to choose among different interfaces to the Python interpreter. First, we have **Jupyter Qt Console**, which is a shell-like app with some extra features. Jupyter (Julia/Python/R) is a new name for an older project called **IPython** (Interactive Python). IPython's contribution was the IPython shell, which added some features to the mere Python language. Qt Console is the result of adding a graphical interface (GUI), with drop-down menus, mouse-clicking, etc, to the IPython shell, by means of a toolkit called Qt.

Part of the popularity of the IPython shell was due to the **magic commands**, which were extra commands written as `%cmd`. For instance, `%cd` allowed you to change the **working directory**. These commands are not part of Python. Some textbooks and tutorials are still very keen on magic commands, which are occasionally mentioned in this course. To get more information about them, enter `%quickref` in the console. Although, in practice, you can omit the percentage sign (so `%cd` works exactly the same as `cd`), it is always safer to keep using it to distinguish the magic commands, which are NOT Python, from the Python code.

Jupyter provides an alternative approach, based on the **notebook** concept. In a notebook, you can combine input, output and ordinary text. In the notebook arena, **Jupyter Notebook** is the leading choice. Notebooks are multilingual, that is, they can be used, not only with Python, but also with other languages like R. Most data scientists prefer the console for developing their code, but use notebooks for diffusion, specially for posting their work on platforms like GitHub.

Besides the Jupyter tools, Anaconda also provides a Python IDE called **Spyder**, where you can manage a console and an text editor for your code. If you have previous experience with this type of interface, for instance from working with R in RStudio, you may prefer Spyder to Qt Console.

Once Anaconda is installed, you can bypass the navigator by calling your preferred interface from a shell app (meaning Terminal in Mac computers and Anaconda Prompt in Windows computers). To start Qt Console, enter `jupyter qtconsole`. To get access to the notebooks in the default browser, enter `jupyter notebook`. To start Spyder, enter `spyder`.

*Note*. Use *Anaconda Prompt* in Windows, instead of the standard Windows prompt, which will not find the Anaconda apps unless you change the path.


## The main packages

This course does not look at Python as a programming language, but from a very specific perspective. Our approach is mainly based on the **package Pandas**.

In the data science context, the main Python packages are:

* **NumPy** adds support for large vectors and matrices, called there **arrays**.

* Based on NumPy, the library **Matplotlib** is Python's plotting workhorse.

* Pandas is a popular library for data management, used in all the examples of this course. Pandas is built on top of NumPy and Matplotlib.


## Google Colab

**Google Colab**, also known as Colaboratory, allows you to write and executing Python code in a browser, with some advantages: (a) it does not require any installation nor configurations, (b) it gives you access to GPU's (meaning more computing power) for free, and (c) it allows you an easy way to share content. In Colab, you can work with notebooks just as you do with the Anaconda notebooks.

The only thing you need to start working on Colab is a Google account, meaning a `gmail.com` address and its password. Colab work happens in **Google Drive**. In your debout in Colab, you have to install the Colaboratory app in your drive. To do this, click on the *Settings* button, select *Settings >> Manage apps* button and click on *Connect more apps*. 
