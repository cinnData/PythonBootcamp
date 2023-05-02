## [PY-03] Data containers ##

# Lists #
mylist = ['Messi', 'Cristiano', 'Neymar', 'Haaland']
len(mylist)
len([])
newlist = mylist + [2, 3]
newlist
len(newlist)

# Extracting items from a list #
mylist[0]
mylist[-1]
mylist[0:2]
mylist[2:]
mylist[:3]
mylist[0::2]
mylist[::-1]

# Membership operators #
yourlist = [4, 7] 
2 in yourlist
2 not in yourlist

# Ranges #
myrange = range(0, 10, 2)
list(myrange)
list(range(5, 12))
list(range(10))

# Other data container types #
mytuple = ('Messi', 'Cristiano', 'Neymar', 'Coutinho')
mytuple[-2:]
mydict = {'name': 'Joan', 'gender': 'F', 'age': 32}
mydict.keys()
mydict.values()
mydict['name']
