## [PY-07] NumPy and Matplotlib ##

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
def f(t):
    return 1/(1 + np.exp(t))
f(arr2)

# Subsetting arrays #
arr1[:3]
arr2[:1, 1:]
arr1 > 3
arr2 > 2
arr1[arr1 > 3]

# An example #
height = [1.65, 1.73, 1.51, 1.63, 1.69, 1.7, 1.81, 1.66, 1.58, 1.66,
    1.62, 1.81, 1.75, 1.65, 1.65]
weight = [61.6, 59.5, 46.5, 75.3, 47.6, 80.2, 67.5, 64.1, 69.5, 57.0,
    68.6, 69.3, 53.2, 66.1, 50.6]
gender = ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'F', 'F', 'M', 'F', 'M',
    'F', 'M', 'M']
height = np.array(height)
weight = np.array(weight)
gender = np.array(gender)
bmi = weight/height**2
bmi
bmi.mean().round(1)
bmi[gender == 'F'].mean().round(1)
bmi[gender == 'M'].mean().round(1)

# Plotting with Matplotlib #
import matplotlib.pyplot as plt
t = np.linspace(0, 2, 100)
plt.figure(figsize=(5,5))
plt.title('Figure 1. Three curves')
plt.plot(t, t, label='linear', color='black')
plt.plot(t, t**2, label='quadratic', color='black', linestyle='dashed')
plt.plot(t, t**3, label='cubic', color='black', linestyle='dotted')
plt.legend();
