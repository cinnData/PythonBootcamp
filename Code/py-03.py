## [PY-03] Defining functions in Python ##

# A first example #
def f(x):
	y = 1/(1 - x**2)
	return y
f(2)
f(1)
f('Mary')
def f(x): return 1/(1 - x**2)

# More about functions #
def hello():
	print('Hello, world!!')
hello()
def g(x, y): 
	z = (x- y)/(x**2 + y**2)
	return z
g(2, 1)
g(x=2, y=1)
g(y=1, x=2)
g(1, 2)
g(2, y=1)
g(x=2, 1)
def root(x, n=2):
	y = x**(1/n)
	return y

# Functions and methods #
len('Bruce Sprinsgteen')
'Bruce Sprinsgteen'.replace(old='Bruce', new='The Boss')
'Bruce Sprinsgteen'.lower()
round(number=1/3, ndigits=2)
