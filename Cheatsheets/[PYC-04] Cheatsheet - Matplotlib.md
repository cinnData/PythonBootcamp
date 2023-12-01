# [PYC-04] Cheatsheet - Matplotlib

## Main plot types

* `plt.bar(x, height)`: draws a bar plot, for which the horizontal coordinates are taken from `x` and the height of the bars from `height`. Both arguments are numeric vector-like objects. It takes two positional arguments plus a collection of keyword arguments with graphical specifications (`width`, `color`, etc).

* `plt.hist(x)`: draws a histogram of a numeric vector-like object `x`. It takes one positional argument plus a collection of keyword arguments with statistical (`bins`, `density`, etc) or graphical specifications (`rwidth`, `color`, etc).

* `plt.plot(x, y)`: plots `y` versus `x` as lines and/or markers. Both arguments are numeric vector-like objects. If only one is provided, it is taken as `y` and the index is used as `x`. It takes one or two positional arguments plus a collection of keyword arguments with graphical specifications (`linestyle`, `color`, etc).

* `plt.scatter(x, y)`: plots `y` versus `x` as markers. Both arguments are numeric vector-like objects. The default marker is a circular dot. It takes two positional arguments plus a collection of keyword arguments with graphical specifications (`marker`, `color`, etc).

## Line style arguments

The line style is specified by the parameter `linestyle` (in short, `ls`). The default is `linestyle='solid'`. Possible values are:

* Solid line: `'solid'` (`-`).

* Dashed line: `'dashed`' (`--`).

* Dash-dot line: `'dashdot'` (`-.`).

* Dotted line: `'dotted'` (`:`).

## Color arguments

The color is specified by the parameter `color` (in short, `c`). The default is `color='blue'`. Possible values are:

* Blue: `'blue'` (`'b'`).

* Green: `'green'` (`'g'`).

* Red: `'red'` (`'r'`).

* Cyan: `'cyan'` (`'c'`).

* Magenta: `'magenta'` (`'m'`).

* Yellow: `'yellow'` (`'y'`).

* Black: `'black'` (`'b'`).

* White: `'white'` (`'w'`).

## Marker style arguments

The marker style for line and scatter plots is specified by the parameter `marker`. The default of `plt.plot()` is `marker=None`. Possible values are:

* Point: `'.'`.

* Circle: `'o'`.

* Square: `'s'`.

* Star: `'*'`.

* Plus: `'+'`.

* X: `'x'`.

* Diamond: `'D'`.

## Additional pyplot functions

* `plt.figure()`: allows to change some default specifications, such as `figsize`. The default is `figsize=(6,4)`. The numbers are inches.

* `plt.title()`: adds a title on top of the figure.

* `plt.xlabel()`: adds a label to the horizontal axis.

* `plt.ylabel()`: adds a label to the vertical axis.

* `plt.legend()`: adds a legend for each plot.

* `plt.annotate()`: annotates individual observations.

* `plt.savefig()`: saves the figure to a file. The extension of the file name (*e.g*. `.pdf`) determines the file format.
