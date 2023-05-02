## [PY-04] Functions and control statements ##

# Functions #
def f(x):
    y = 1/(1 - x**2)
    return y
f(2)
f(1)
f('Mary')
def g(x, y): return x*y/(x**2 + y**2)
g(1, 1)

# If statements #
if 3 < 5: print('Minor')
if 3 == 5: print('Equal')
else: print('Not equal')
if math.sqrt(1) < 1: print('Minor')
elif math.sqrt(1) == 1: print('Equal')
else: print('Major')

# While loops #
x = 1
while x**2 <= 1000: x = x + 1
x
x = 1
while x > 0: x = x + 1
x

# For loops #
for i in range(3): print('Hello world!')
squares = []
for i in range(1, 5):
    squares = squares + [i**2]
squares

# List comprehensions #
[i**2 for i in range(1, 5)]
[i**2 for i in range(1, 21) if i % 3 != 0]
