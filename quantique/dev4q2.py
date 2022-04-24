import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
pts = 625
x_range = 10
y_range = 10
colors_in_quiver = 20
headwidth=5.0
minlength=3
pivot='tail'

# Initialization
y,z = np.linspace(-x_range,x_range,pts), np.linspace(-y_range,y_range, pts)
y,z = np.meshgrid(y,z)
x = 0
r = np.sqrt(x**2+y**2+z**2)
phi = np.arctan(y/x)
theta = np.arctan(np.sqrt(x**2+y**2)/z)

# Component of P
comp = (16*np.pi)**-1*r**2*np.exp(-r)*np.sin(theta)**2  # *np.sin(phi)**2

# Plot 
fig, ax = plt.subplots(figsize=(10,9))
ax.quiver(y, z, comp)
ax.tick_params(top=False, bottom=False, left=False, right=False)
plt.xticks([])
plt.yticks([])
ax.set_xlabel('Y')
ax.set_ylabel('Z')

plt.savefig('x0-.pdf')
plt.show()