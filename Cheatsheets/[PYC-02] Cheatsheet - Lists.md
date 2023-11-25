# [PYC-02] Cheatsheet - Lists

## Extracting items from a list

* `lst[n]`: extracts the item of the list `lst` whose index is `n`. Since Python starts counting at zero, this would be the item in place `n+1`.

* `lst[-n]`: extracts the item with index `len(lst) - n`. So, `lst[-1]` returns the last item, `lst[-2]` the penultimate item, etc.

* `lst[n:m]`: extracts a sublist containing the items whose indexes go from `n` to `m-1`. If `n` is missing, it is assumed to be equal to `0`. If `m` is missing, it is assumed to be equal to `len(lst)`.

* `lst[n:m:s]`: extracts a sublist containing the items from index `n` to index `m-1`, making steps of `s`. So, `lst[2:10:3]` contains the items with indexes `2`, `5` and `8`. If `s` is negative, steps are made backwards. In particular, `lst[::-1]` returns the list reversed.

## List functions 

* `len()`: returns the number of items of a list. It takes one positional argument.

* `max()`: returns the largest items of a list whose items have a common type. It takes one positional argument.

* `min()`: returns the largest items of a list whose items have a common type. It takes one positional argument.

* `sorted()`: sorts a list of items of a common type, in ascending order. With the argument `reverse=True`, the list is sorted downwards. Besides `reverse`, it has another parameter with less interest.

* `sum()`: returns the sum of the items of a numeric list. It takes one positional argument.

## List methods

* `.append(x)`: adds `x` at the end of a list, *in place* (without returning the new version). The new version of `mylist` after applying this method is the same as `mylist + [x]`. It takes one positional argument.

* `.count(x)`: returns the number of times `x` appears in a list. It takes one positional argument.

* `.extend(x)`: adds the contents of the list `lst` at the end of a list, *in place* (without returning the new version). If `x` is a list, the new version of `mylist` after applying this method is the same as `mylist + x`. It takes one positional argument.

* `.index(x)`: returns the index of the first item of a list whose value is equal to `x`. It takes at least one positional argument.

* `.insert(n, x)`: inserts `x` in a list with index `n`, *in place* (without returning the new version). It takes two positional arguments.

* `.pop(n)`: returns the item of a list with index `n`, removing it. It takes one positional argument. If it is missing, it is assumed to be equal to `-1`.

* `.remove(x)`: removes the first occurrence of `x` from a list, *in place* (without returning the new version). It raises a `ValueError` if there is no occurrence. It takes one positional argument. 

* `.reverse()`: reverses the order of in a list whose items have a common type, *in place* (without returning the new version). The new version of `mylist` after applying this method is the same as `mylist[::-1]`, the same as `sorted(mylist, reverse=True)`. It takes zero arguments.

* `.sort()`: sorts the items of a list whose items have a common type, *in place* (without returning the new version). With the argument `reverse=True`, the list is sorted downwards. Besides `reverse`, it has another parameter with less interest. The new version of `mylist` after applying this method is the same as `sorted(mylist)`.

## List comprehensions

* `[expr for i in lst]`: returns a list whose items result from evaluating the expression `expr` on the items of the list `lst`.

* `[expr for i in lst if cond]`: returns a list whose items result from evaluating the expression `expr` on the items of `lst` that satisfy the condition `cond`.

* `[expr for i1 in lst1 for i2 in lst2]`: returns a list whose items result from evaluating the expression `expr` on all the pairs `(i, j)` in which `i1` is taken from `lst1` and `i2` is taken from `lst2`. This is called a **nested loop**.

* `[expr for i in lst for j in i]`: applies to a list of lists. It returns a list whose items result from evaluating the expression `expr` on the items of every item `i` of `lst`. This is a particular case of nested loop (see the preceding bullet).
 
