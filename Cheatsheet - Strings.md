# Cheatsheet - Strings

## Slicing

* `str[n]`: extracts the character of the string `str` whose index is `n`. Since Python starts counting at zero, this would be the character in placed `n+1`.

* `str[-n]`: extracts the character of `str` whose index is equal to the length of `str` minus `n`. So, `str[-1]` extracts the last character, `str[-2]` the penultimate character, etc.

* `str[n:m]`: extracts the substring formed by the characters of `str` whose indexes go from `n` to `m-1`. If `n` is missing, it is assumed to be `0`. If `m` is missing, it is assumed to be equal to the length of `str`.

* `str[n:m:s]`: extracts the substring formed by the characters of `str` from index `n` to index `m-1`, making steps of `s`. So, `str[2:10:3]` contains the characters with indexes `2`, `5` and `8`. If `s` is negative, steps are made backwards. So `str[::-1]` returns `str` reversed.

## String methods

* `str.capitalize()`: returns a copy of `str` with its first character capitalized and the rest lowercased.

* `str.count(substr)`: returns the number of times the substring `substr` occurs in a string `str`, without overlapping.

* `str.endswith(suffix)`: returns a Boolean indicating whether the last characters of `str` coincide with the string `suffix`.

* `str.find(substr)`: returns the index of the first character of the first occurrence of a substring in a string. If the substring does not occur, it returns `-1`.

* `str.join(strlist)`: returns the string resulting from pasting the elements of the list of strings `strlist` with the glue `str`. So, `' '.join(['Joe', 'Biden'])` returns `'Joe Biden'`.

* `str.lower()`: returns a copy of `str` with all the cased characters converted to lowercase.

* `str.replace(old, new)`: returns a copy of `str` with all occurrences of `old` replaced by `new`.

* `str.split(sep)`: returns the list of substrings of `str` resulting from a split based on the separator specified. The default is `sep=''`.

* `str.startswith(prefix)`: returns a Boolean indicating whether the first characters of `str` coincide with the string `prefix`.

* `str.strip(chars)`: returns a copy of `str` with the leading and trailing characters removed. The `chars` argument is a string specifying the set of characters to be removed. The default is `chars=' '`.

* `str.upper()`: returns a copy of `str` with all the cased characters converted to uppercase.

* `substr in str`: returns a Boolean indicating whether `substr` is contained in the `str`.
