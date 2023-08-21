## [PY-05] Control statements ##

# If statements #
if 3 < 5: print('Minor')
if 3 == 5: print('Equal')
else: print('Not equal')
import math
if math.sqrt(1) < 1: print('Minor')
elif math.sqrt(1) == 1: print('Equal')
else: print('Major')

# While loops #
x = 1
while x**2 <= 1000: x = x + 1
x
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
