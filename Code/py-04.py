## [PY-04] Python data containers ##

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
mylist[1:3]
mylist[2:]
mylist[:3]
mylist[0::2]
mylist[::-1]

# Membership operators #
yourlist = [4, 7]
2 in yourlist
2 not in yourlist

# Strings as sequences #
mylist[2:3]
mylist[2]
'Neymar' in mylist
mylist.append('Vinicius')
mylist

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

# Mutability #
mylist[1] = 'Benzema'
mylist
mydict['job'] = 'Engineer'
mydict
mydict['name'] = 'Martha'
mydict
