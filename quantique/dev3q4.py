import matplotlib.pyplot as plt
import numpy as np


def f(x):
	return np.abs(x)**3/3+np.abs(x)**2+np.abs(x)


x = np.linspace(-100, 100, 10000)

plt.plot(x, f(x))
plt.plot([-100,100], [0, 0], 'k:')
plt.show()