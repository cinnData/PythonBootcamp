## [PY-05] Control statements ##

# If statements #
grade = 9
if grade >= 5:
    print('Congratulations!')
if grade >= 5:
    print('PASS')
else:
	print('FAIL')
if grade >= 8:
    print('A')
elif grade >= 5:
    print('B')
else:
    print('C')
if grade >= 8:
    print('Good!')
elif grade >= 5:
    print('Keep working!')

# While loops #
x = 1
while x**2 <= 1000:
    x = x + 1
x
x = 1
while x > 0:
    x = x + 1
x

# For loops #
for i in range(3):
    print('Hello world!')
squares = []
for i in range(1, 5):
    squares = squares + [i**2]
squares

# List comprehensions #
squares = [i**2 for i in range(1, 5)]
squares
my_squares = [i**2 for i in range(1, 21) if i % 3 != 0]
my_squares
