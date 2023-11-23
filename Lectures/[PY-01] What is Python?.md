# [PY-01] What is Python? 

## What is Python?

**Python** is a programming language, born in 1991. The latest stable version (when this is being written) is Python 3.11. As a programming language, Python can be used by a programmer to write a program that performs a task. Since this course is data-oriented, let us mention a few examples in that line:

* A **web scraping** program that captures data on the current prices published in an e-commerce web site, storing them in a database.

* A **machine learning** program that trains an algorithm that assigns credit scores to borrowers in a lending platform.

* A **pricing algorithm** that estimates the market price of a real estate asset.

These programs are later executed many times without being modified. But you can use Python in other ways. For instance, to examine the variation of the stock price of a specific company, or the structure of the vacation rental market in a specific region. Either for developing a program, which always involves a bit of trial and error, or in a data analysis, we use a basic tool, the **Python interactive interpreter**. We can have several instances of the interpreter, called **kernels**, running independently in our computer. To deal with the Python interpreter, Pythonistas use an app that provides an as interface to the Python interpreter, chosen among the many available choices (see below). 

## Python modules and packages

Many additional resources have been added to Python in the form of **modules**. A module is just a text file containing Python code. Modules are grouped in **libraries**. The **Python Standard Library**, distributed with Python, contains **built-in modules** providing standardized solutions for many problems that occur in everyday programming. For instance, the module `math` provides mathematical functions, while the module `datetime` provides functions for manipulating dates and times.

Other libraries are typically called **packages**, because their elements are packed according to some specific rules which allow you to install and call them together. Python can be extended by more than 300,000 packages. Some big packages like scikit-learn (a machine learning toolkit) have **subpackages**.

Since the basic Python toolkit (without any module) is quite limited, you will need to **import** additional resources for practically everything. Once a module has been imported, all its functions are available. Alternatively, you can import a single function from a module. Resources are imported just for the current kernel. You can only import from packages which are already **installed** in your computer. 

Almost everything in the Python world is open-source. In particular, Python packages are contributed by various agents, such as university professors, freelance programmers, or industry behemoths like Google. This leads to a dynamic ecosystem, where you may find overlapping, dependencies and multiple versions. 

## Python distributions

A **Python distribution** is a software bundle, containing, at least, a Python interpreter and the corresponding version of the standard library. It also includes a collection of packages and one or more package managers for installing, uninstalling or updating packages. All distributions have a **package manager** called `pip`, and some distributions have a specific package manager.

One option for working with Python is to start a Python kernel directly in a **shell** application associated to the operating system of your computer. Shell apps are typically called **Terminal** in Mac/Linux computers and **Prompt** in Windows computers. For this approach to work, the shell app has to find the Python files. This is automatic when the folder where the Python distribution is in the **path** of that shell. In the contrary, you have to know where to find it. 

If you are just starting with Python, you will prefer a friendlier approach. Python distributions provide various interfaces to the Python interpreter. All include a **command line interface** (CLI), which may be a shell-like application or an **integrated development environment** (IDE). A Python IDE provides a Python-aware code editor integrated with the ability to run code from that editor. Details about one of the top popular Python distributions follow.

## The Anaconda distribution

In the data science community, **Anaconda** (`anaconda.com`) is the favorite distribution. The current Anaconda distribution comes with Python 3.10. Anaconda provides all the packages used in this course, so no extra installation is needed. Anyway, Anaconda has a specific package manager, called `conda`. You may need `conda` for more advanced work, because it reviews the packages that are already installed in our computer, keeping track of the dependencies, and solving version conflicts between packages. On the downside, `conda` is much slower than `pip`.

After downloading and installing Anaconda, you can start your Python experience with the **Anaconda Navigator**, which opens in the browser and allows you to choose among different interfaces to the Python interpreter. First, you have **Jupyter Qt Console**, which is a shell-like app with some extra features. Jupyter (Julia/Python/R) is a new name for an older project called **IPython** (Interactive Python). IPython's contribution was the IPython shell, which added some features to the mere Python language. Qt Console is the result of adding a **graphical user interface** (GUI), with drop-down menus, mouse-clicking, etc, to the IPython shell, by means of a toolkit called Qt.

Part of the popularity of the IPython shell was due to the **magic commands**, which were extra commands written as `%cmd`. For instance, `%cd` allows you to change the **working directory**. These commands *are not part of Python*. Though some textbooks and tutorials are still very keen on magic commands, these commands appear very briefly in this course. To get more information about them, enter `%quickref` in the console. Although, in practice, you can omit the percentage sign (so `%cd` works exactly the same as `cd`), it is always safer to keep using it to distinguish the magic commands from the Python code.

Jupyter provides an alternative approach, based on the **notebook** concept. A notebook is kind of document where you can combine input, output and ordinary text. A notebook is stored in a file with extension `ipynb` (IPython notebook). In the notebook arena, **Jupyter Notebook** is the leading choice. Notebooks are multilingual, that is, they can be used, not only with Python, but also with other languages like R. Most data scientists prefer the console for developing their code, but use notebooks for diffusion, specially for posting their work on platforms like **GitHub**.

Besides the Jupyter apps, Anaconda also provides a Python IDE called **Spyder**, where you can manage together a console and a text editor for your code. If you have previous experience with IDE's, for instance from working with R in RStudio, you may prefer Spyder to Qt Console.

Once Anaconda is installed, you can bypass the navigator by calling your preferred interface from a shell. To start Qt Console, enter `jupyter qtconsole`. To get access to the notebooks in the default browser (*e.g*. Google Chrome), enter `jupyter notebook`. To start Spyder, enter `spyder`.

*Note*. Use *Anaconda Prompt* in Windows, instead of the standard Windows prompt, whose path does not contain the Anaconda apps.

## The main packages

This course does not look at Python as a programming language, but from a very specific perspective, assuming a data science context. From this perspective, the main Python packages are:

* **NumPy** adds support for large vectors and matrices, called there **arrays**.

* **Matplotlib**, based on NumPy, provides a plotting toolkit.

* **Pandas** is a popular library for data management, used in the examples of this course. Pandas is built on top of NumPy and Matplotlib.

## Colab notebooks

**Google Colaboratory** is a Google app which allows you to write and executing Python code in a browser, with some advantages: (a) it does not require installation nor configuration, (b) it gives you access to GPU's (meaning more computing power) for free, and (c) it allows you an easy way to share content. In Google Colaboratory, you work with documents called **Colab notebooks**. Though they are not exactly the same, Colab notebooks are pretty similar to Jupyter notebooks, and they stored in Google Drive as files with extension `ipynb`. 

You may be interested in using Colab, since you can access it from any deviced connected to Internet, such as an IPAD. The only thing you need to start working with Colab notebooks is a Google account, meaning a `gmail.com` address and its password. Colab work happens in **Google Drive** (enter through `https://www.google.com/drive`). In your debout, you have to install the Google Colaboratory app in your drive. To do this, click on the *Settings* button, select *Settings >> Manage apps* button and click on *Connect more apps*. `ipynb` files can be uploaded to and downloaded from Google Drive.
