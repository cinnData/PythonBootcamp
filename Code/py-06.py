## [PY-06] NumPy and Matplotlib ##

# NumPy arrays #
import numpy as np
arr1 = np.array(range(10))
arr1
np.array([2, 'a', True])
np.array([2, True])
np.array([2, 3.2])
arr2 = np.array([[0, 7, 2, 3], [3, 9, -5, 1]])
arr2
arr1.shape
arr2.shape
arr1[2]
arr2[1, 2]

# NumPy functions #
np.sqrt(arr1)
def f(t): return 1/(1 + np.exp(t))
f(arr2)

# Subsetting arrays #
arr1[:3]
arr2[:1, 1:]
arr1 > 3
arr2 > 2
arr1[arr1 > 3]
arr2[arr2[:, 0] > 0, :]

# Plotting with Matplotlib #
import matplotlib.pyplot as plt
t = np.linspace(0, 2, 100)
plt.figure(figsize=(6,6))
plt.title('Figure. Three curves')
plt.plot(t, t, label='linear', color='black')
plt.plot(t, t**2, label='quadratic', color='black', linestyle='dashed')
plt.plot(t, t**3, label='cubic', color='black', linestyle='dotted')
plt.legend();
