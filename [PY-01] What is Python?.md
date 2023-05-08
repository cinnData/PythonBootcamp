# [PY-01] What is Python? 

## What is Python?

**Python** is a programming language, introduced in 1991. The latest stable version (when this is being written) is Python 3.11. To work with Python, you will use an interface to a **Python interpreter** among the many available choices (see below). You can have several instances of the interpreter, called **kernels**, running independently in your computer.

Warning: Python is **case sensitive**. For instance, `type` is a Python function which returns the type of an object, but `Type` is not recognized (unless you create a new function with this name), and will return an error message.

## Python modules and packages

Many additional resources have been added to Python in the form of **modules**. A module is just a text file containing Python code. Modules are grouped in **libraries**. The **Python Standard Library**, which is distributed with Python, contains **built-in modules** providing standardized solutions for many problems that occur in everyday programming. For instance, `math` provides mathematical functions, while `datetime` provides functions for manipulating dates and times.

Other libraries are typically called **packages**, because their elements are packed according to some specific rules which allow you to install and call them together. Python can be extended by more than 300,000 packages. Some big packages like scikit-learn (a machine learning toolkit) have **subpackages**.

Since the basic Python toolkit (without any module) is quite limited, you will need to **import** additional resources for practically everything. Once a module has been imported, all its functions are available. Modules are imported just for the current kernel. You can only import from packages which are already **installed** in your computer. 

Mind that, since Python is an open source project, packages are contributed by various agents, such as university professors, freelance programmers, or industry behemoths like Google. Any package has different versions and it can have dependencies on other packages.

## Python distributions

A **Python distribution** is a software bundle, which contains a Python interpreter and the standard library. Python distributions also have package managers for installing, uninstalling or updating packages. All distributions have a **package manager** called `pip`, and some distributions have a specific package manager.

You can open a Pyhton kernel directly in a **shell** applications associated to your operating system. This means **Terminal** in Mac computers and **Prompt** in Windows computers. But, for this approach to work, the shell has to find the Python files. THis is automatic when the folder where the Python distribution is in the **path** of that shell. In the contrary, you have to know where to find it. 

If you are just starting with Python, you will prefer a friendlier approach. Python distributions provide various interfaces to the Python interpreter. All include a **command line interface** (CLI), which may be a shell-like application or an **integrated development environment** (IDE). A Python IDE provides a Python-aware code editor integrated with the ability to run code from that editor. Details about the top popular Python distribution follow.

## The Anaconda distribution

In the data science community, **Anaconda** (`anaconda.com`) is the favorite distribution. The current Anaconda distribution comes with Python 3.10. Anaconda provides all the packages used in this course, so no extra installation is needed. Anyway, Anaconda has a specific package manager, called `conda`. You may need `conda` for more advanced work, because it reviews the packages that are already installed in our computer, keeping track of the dependencies, and solving version conflicts between packages. On the downside, `conda` is much slower than `pip`.

Downloading and installing Anaconda leaves you with the **Anaconda Navigator**, which opens in the browser and allows you to choose among different interfaces to the Python interpreter. First, we have **Jupyter Qt Console**, which is a shell-like app with some extra features. Jupyter (Julia/Python/R) is a new name for an older project called **IPython** (Interactive Python). IPython's contribution was the IPython shell, which added some features to the mere Python language. Qt Console is the result of adding a **graphical user interface** (GUI), with drop-down menus, mouse-clicking, etc, to the IPython shell, by means of a toolkit called Qt.

Part of the popularity of the IPython shell was due to the **magic commands**, which were extra commands written as `%cmd`. For instance, `%cd` allows you to change the **working directory**. These commands are not part of Python. Though some textbooks and tutorials are still very keen on magic commands, they areappear very briefly in this coourse. To get more information about them, enter `%quickref` in the console. Although, in practice, you can omit the percentage sign (so `%cd` works exactly the same as `cd`), it is always safer to keep using it to distinguish the magic commands, which are NOT Python, from the Python code.

Jupyter provides an alternative approach, based on the **notebook** concept. In a notebook, you can combine input, output and ordinary text. In the notebook arena, **Jupyter Notebook** is the leading choice. Notebooks are multilingual, that is, they can be used, not only with Python, but also with other languages like R. Most data scientists prefer the console for developing their code, but use notebooks for diffusion, specially for posting their work on platforms like GitHub.

Besides the Jupyter tools, Anaconda also provides a Python IDE called **Spyder**, where you can manage together a console and a text editor for your code. If you have previous experience with IDE's, for instance from working with R in RStudio, you may prefer Spyder to Qt Console.

Once Anaconda is installed, you can bypass the navigator by calling your preferred interface from a shell. To start Qt Console, enter `jupyter qtconsole`. To get access to the notebooks in the default browser, enter `jupyter notebook`. To start Spyder, enter `spyder`.

*Note*. Use *Anaconda Prompt* in Windows, instead of the standard Windows prompt, which will not find the Anaconda apps unless you change the path.

## The main packages

This course does not look at Python as a programming language, but from a very specific perspective, assuming a data science context. From this perspective, the main Python packages are:

* **NumPy** adds support for large vectors and matrices, called there **arrays**.

* **Matplotlib**, based on NumPy, provides a plotting toolkit.

* **Pandas** is a popular library for data management, used in all the examples of this course. Pandas is built on top of NumPy and Matplotlib.

## Google Colab

**Google Colab**, also known as Colaboratory, allows you to write and executing Python code in a browser, with some advantages: (a) it does not require any installation nor configurations, (b) it gives you access to GPU's (meaning more computing power) for free, and (c) it allows you an easy way to share content. In Colab, you can work with notebooks just as you do with the Anaconda notebooks.

You may be interested in using Colab, since you can access it from any deviced connected to Internet, *e.g*. an IPAD. The only thing you need to start working on Colab is a Google account, meaning a `gmail.com` address and its password. Colab work happens in **Google Drive** (`www.google.com/drive`). In your debout in Colab, you have to install the Colaboratory app in your drive. To do this, click on the *Settings* button, select *Settings >> Manage apps* button and click on *Connect more apps*. 
