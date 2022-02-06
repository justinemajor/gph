import numpy as np
import matplotlib.pyplot as mpl


def profondeur(theta, n):
    return np.cos(theta)/(n**2-np.sin(theta)**2)**.5

n = 1.333
theta = np.linspace(0, np.pi/2, 1000)

fig1, xy = mpl.subplots(1)
xy.plot(np.degrees(theta), profondeur(theta, n))
xy.tick_params(axis="y", direction="in")
xy.tick_params(axis="x", direction="in")
xy.set_ylabel("Profondeur apparente du poisson [m]")
xy.set_xlabel("Angle d'observation [\N{DEGREE SIGN}]")
fig1.savefig("profondeurApparente.pdf")
mpl.show()