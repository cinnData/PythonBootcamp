# Cheatsheet - NumPy

## Subsetting 1D arrays

* `arr[n]`: returns the term of index `n`. Since Python starts counting at zero, this would be the entry in place `n-1`.

* `arr[lst]`: for a list of indexes `lst`, returns a subarray containing the terms whose index is in the `lst`. A range can be used instead of a list.

* `arr[n:m]`: the same as `arr[range(n, m)]`. It returns a subarray containing the terms of `arr` whose indexes go from `n` to `m-1`. If `n` is missing, it is assumed to be equal to `0`. If `m` is missing, it is assumed to be equal to `len(arr)`.

* `arr[b]`: for a 1D boolean mask `bm`, with the same length as `arr`, returns a subarray containing the terms for which `bm` takes value `True`.

## Subsetting 2D arrays

* `arr[n,m]`:returns the term at row `n` and column `m`.

* `arr[r1:r2, c1:c2]`: returns the subarray resulting from selecting the row indexes from `r1` to `r2-1` and the column indexes from `c1` to `c2-1`.

* `arr[lst, c1:c2]`: for a list of indexes `lst`, returns the subarray resulting from selecting the row indexes from `lst` and the column indexes from `c1` to `c2-1`. A range can also be used here.

* `arr[bm, c1:c2]`: for a 1D boolean mask `bm`, with the same length as the number of rows of `arr`, returns the subarray resulting from selecting the row indexes for which `bm` takes value `True` and the column indexes from `c1` to `c2-1`.

* `arr[r1:r2, lst]`: similar to `arr[lst, c1:c2]`.

* `arr[bm, c1:c2]`: similar to `arr[bm, c1:c2]`.

## NumPy attributes

* `arr.dtype`: returns the data type of `arr`. If the elements of `arr` are literals, it will be `int64`, `float64`, `<Ul` (`l` being the maximum length) or `bool`. More complex data can have data type `object`.

* `arr.ndim`: returns the number of dimensions, 1 for a 1D array and 2 for 2D array.

* `arr.shape`: returns the shape of the array, as a tuple. For a 1D array with `l` terms, it is `(l,)`, and, for a 2D array with `r` rows and `c` columns, `(r,c)`.

## NumPy methods and functions

* `np.abs(arr)`: replaces the terms of a numeric array by their absolute values. The same as `abs(arr)`.

* `np.arange(n, m, s)`: returns a 1D array containing the integers from `n` to `m-1`, making steps of `s`. So, `np.arange(2, 10, 3)` contains `2`, `5` and `8`. If `s` is negative (and `n`is higher than `m`), steps are made backwards, from `n` to `m+1`. The same as `np.array(range(n, m, s))`.

* `np.argmax(arr)`: returns the index of the maximum term of an array. With argument `axis=0`, returns a 1D array containing the index of the maximum of every column of `arr`. With argument `axis=1`, the index of the maximum of every row.

* `np.argmin(arr)`: returns the index of the minimum term of an array `arr`. With argument `axis=0`, returns a 1D array containing the index of the minimum of every column of `arr`. With argument `axis1`, the index of the minimum of every row.

* `np.array(lst)`: for a list `lst` whose elements are literals of the same data type, returns a 1D array containing the same elements as `lst`. For a list whose elements are lists of the same length, containing literals of the same data type, returns a 2D array.

* `np.argsort(arr)`: takes a 1D array `arr` and returns a 1D array containing the index that every term will take if `arr` were sorted in ascending order.

* `arr.astype(dt)`: converts an array to data type `dt`.

* `np.corrcoef([arr1, arr2, ...])`: returns the correlation matrix of a list of numeric 1D arrays of the same length. For two arrays, the square brackets can be omitted. It can also take a 2D array, returning the correlations of the row vectors (not that of the columns).

* `np.cumsum(arr)`: returns a 1D array containing the cumulative sums of the terms of `arr`. For a 2D array, the cumulative sums are calculated row following row. With argument `axis=0`, returns a 2D array containing the column cumulative sums. With argument `axis1`, the row cumulative sums. The same as `arr.cumsum()`.

* `np.delete(arr, lst)`: for a 1D array, deletes the terms whose indexes are in the list `lst`. It returns the complement of `arr[lst]`. For a 2D array, an axis can be specified. With `axis=0`, it deletes rows and, with `axis=1`, columns . `lst` can be replaced by a single index, or by a range.

* `np.diagonal(arr)`: returns the diagonal of a square 2D array, as a 1D array. The same as `arr.diagonal()`.

* `np.int64(arr)`: converts a `str`, `float` or `bool` array to data type `int64`. The same as `arr.astype('int')`.

* `np.float64(arr)`: converts a `str`, `int` or `bool` array to data type `float64`. The same as `arr.astype('float')`.

* `len(arr)`: for a 1D array, returns the number of terms of `arr`. For a 2D array, the number of rows.

* `np.linspace(a, b, n)`: returns a 1D array with `n` equally spaced terms, starting by `a` and ending by `b`.

* `np.max(arr)`: returns the maximum of the terms of `arr`. With argument `axis=0`, returns a 1D array containing the column maxima. With `axis=1`, the row maxima. The same as `arr.max()`.

* `np.mean(arr)`: returns the mean of the terms of `arr`. With argument `axis=0`, returns a 1D array containing the column means. With `axis=1`, the row means. The same as `arr.mean()`.

* `np.min(arr)`: returns the minimum of the terms of `arr`. With argument `axis=0`, returns a 1D array containing the column minima. With `axis=1`, the row minima. The same as `arr.min()`.

* `np.round(arr, d)`: rounds the terms of a numeric array to a specified number of digits. The same as `arr.round(d)`.

* `np.reshape(arr, sh)`: converts `arr` to shape `sh`. The number of terms of the reshaped array must be equal to that of the original array. The same as `arr.reshape(sh)`.

* `np.sort(arr)`: sorts a 1D array in ascending order. To reverse this, add `[::-1]`. For higher dimensional arrays, look at the manual.

* `arr.sort()`: sorts a 1D array in ascending order, without returning the new version. The original array is not retained. Not the same as `np.sort(arr)`.

* `np.sum(arr)`: returns the sum of the terms of `arr`. With argument `axis=0`, returns a 1D array containing the column totals. With `axis=1`, the row totals. The same as `arr.sum()`.

* `np.vectorize(fname)`: vectorizes the function `fname`, so it can take NumPy arrays as arguments.

* `np.transpose(arr)`: transposes a 2D array. The same as `arr.transpose()` and `arr.T`.

* `np.unique(arr)`: returns a 1D array containing the unique terms of `arr`, in ascending order. With the additional argument `returns_counts=True`, returns a second array containing the number of occurrences of every unique value.

## Joining NumPy arrays

* `np.concatenate([arr1, arr2, ...], axis=n)`: joins a sequence of arrays along an existing axis. The default is `axis=0`. For instance, if `arr1` and `arr2` are two matrices of the same number of columns, `np.concatenate([arr1, arr2])` returns a matrix with the same number of columns, with `arr1` on top of `arr2`. If they are two matrices of the same number of rows, `np.concatenate([arr1, arr2], axis=1)` returns a matrix with the same of rows with `arr1` on the left of `arr2`.

* `np.stack([arr1, arr2, ...], axis=n)`: joins a sequence of arrays of the same dimensions along a new axis. The axis parameter specifies the index of the new axis in the dimensions of the result. The default is `axis=0`. For instance, if `arr1` and `arr2` are two vectors of the same length, `np.stack([arr1, arr2])` puts them as the rows of a matrix, while `np.stack([arr1, arr2], axis=1)` puts them as the columns of a matrix. Note that stack increases the dimension, while concatenate leaves the dimension unchanged.
