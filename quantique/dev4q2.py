import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
pts = 625
x_range = 25
y_range = 25

# Initialization
x,y = np.linspace(-x_range,x_range,pts), np.linspace(-y_range,y_range, pts)
x,y = np.meshgrid(x,y)
z = 5
r = np.sqrt(x**2+y**2+z**2)
phi = np.arctan(y/x)
theta = np.arctan(np.sqrt(x**2+y**2)/z)

# Component of P
comp = (16*np.pi)**-1*r**2*np.exp(-r)*np.cos(theta)**2  # *np.sin(phi)**2

# Plot 
fig, ax = plt.subplots(figsize=(10,9))
ax.quiver(x, y, comp)
ax.tick_params(top=False, bottom=False, left=False, right=False)
plt.xticks([])
plt.yticks([])
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.savefig('z5fond.pdf')
plt.show()