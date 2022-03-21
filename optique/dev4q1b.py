import matplotlib.pyplot as mpl
import numpy as np


r1 = .5 # ou .5
delta = np.linspace(0, 10*np.pi, 100000)

def phi(delta, r=r1):
	num = (1-r**2)*np.sin(delta)
	denom = 2*r+(1+r**2)*np.cos(delta)
	return np.arctan(num/denom)

mpl.plot(delta, phi(delta))
mpl.tick_params(direction='in')
mpl.xlabel(f"Déphasage d'un aller-retour dans la cavité pour r={r1} [rad]")
mpl.ylabel("Phase de r [rad]")
mpl.savefig(f"r{r1}phase.pdf")
mpl.show()
