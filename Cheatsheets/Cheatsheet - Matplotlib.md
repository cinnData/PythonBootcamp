# Cheatsheet - Matplotlib

## Main plot types

* `plt.hist`: histogram.

* `plt.plot`: line chart.

* `plt.scatter`: scatter plot.

## Line style

Specified by the argument `linestyle` (in short, `ls`). The default is `linestyle='solid'`.

* Solid line: `'solid'` (`-`).

* Dashed line: `'dashed`' (`--`).

* Dash-dot line: `'dashdot'` (`-.`).

* Dotted line: `'dotted'` (`:`).

## Color

Specified by the argument `color` (in short, `c`). The default is `color='blue'`.

* Blue: `'blue'` (`'b'`).

* Green: `'green'` (`'g'`).

* Red: `'red'` (`'r'`).

* Cyan: `'cyan'` (`'c'`).

* Magenta: `'magenta'` (`'m'`).

* Yellow: `'yellow'` (`'y'`).

* Black: `'black'` (`'b'`).

* White: `'white'` (`'w'`).

## Marker style

Specified by the argument `marker`. The default of `plt.plot` is `marker=None`.

* Point: `'.'`.

* Circle: `'o'`.

* Square: `'s'`.

* Star: `'*'`.

* Plus: `'+'`.

* X: `'x'`.

* Diamond: `'D'`.

## Additional pyplot features

* `plt.figure`: allows to change some default specifications, such as `figsize`.

* `plt.title`: adds title on top.

* `plt.xlabel`: adds label to the horizontal axis.

* `plt.ylabel`: adds label to the vertical axis.

* `plt.legend`: adds a legend for each plot.

* `plt.annotate`: annotates individual observations.

* `plt.savefig`: saves the figure to a file. The extension of the file name (*e.g*. `.pdf`) determines the file format.
