## [PY-06] Programs and modules ##

# The working directory #
%pwd
%cd py_course
%pwd

# Program 1 #
print('\nHi, there!\nThis is the Python Course!')
runfile('program1.py')

# input statements #
input('\nDo you know Python? (y/n) ')
int(input('\nWhat is your age? '))

# Program 2 #
runfile('program2.py')

# Modules #
import myfuncs
myfuncs.has_zero(1, -2, 0)
from myfuncs import has_zero
has_zero(1, -2, 3)
