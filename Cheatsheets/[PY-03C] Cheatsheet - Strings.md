# [PY-03C] Cheatsheet - Strings

## Slicing

* `str[n]`: extracts the character of the string `str` whose index is `n`. Since Python starts counting at zero, this would be the character in placed `n+1`.

* `str[-n]`: extracts the character of `str` whose index is equal to the length of `str` minus `n`. So, `str[-1]` extracts the last character, `str[-2]` the penultimate character, etc.

* `str[n:m]`: extracts the substring formed by the characters of `str` whose indexes go from `n` to `m-1`. If `n` is missing, it is assumed to be `0`. If `m` is missing, it is assumed to be equal to the length of `str`.

## Membership operators

* `substr in str`: returns a Boolean value indicating whether `substr` is contained in the `str`.

* `substr not in str`: the opposite.

## String methods

* `.capitalize()`: converts the first character of a string to uppercase and the rest to lowercase. It takes zero arguments.

* `.count(sub)`: returns the number of times the substring `sub` occurs in a string, without overlapping. It takes one positional argument.

* `.endswith(suffix)`: returns a Boolean indicating whether the last characters of a string coincide with those of the string `suffix`. It takes one positional argument.

* `.find(sub)`: returns the index of the first character of the first occurrence of the string `sub` in a string. If the substring does not occur, it returns `-1`. It takes one positional argument.

* `.lower()`: converts all the characters of a string to lowercase. It takes zero arguments.

* `.replace(old, new)`: replaces every occurrence of the subtring `old` by the string `new`. It takes two positional arguments.

* `.split(sep)`: returns the list of substrings of `str` resulting from a split based on the separator specified. It has one parameter whose default is `sep=''`.

* `.startswith(prefix)`: returns a Boolean value indicating whether the first characters of a string coincide with the string `prefix`. It takes one positional argument.

* `.strip(chars)`: removes with the leading and/or trailing characters from a string when they coincide with the substring `chars`. It takes one positional argument whose default is `' '`.

* `.upper()`: converts all the characters of a string to uppercase. It takes zero arguments.
