import matplotlib.pyplot as mpl
import numpy as np


r1 = .5 # ou .5
delta = np.linspace(0, 10*np.pi, 100000)

def phi(delta, r=r1):
	num = (1-r**2)*np.sin(delta)
	denom = 2*r+(1+r**2)*np.cos(delta)
	return np.arctan(num/denom)

def sinc(beta):
	return np.sin(beta)/beta

def new(beta):
	return np.cos(beta)/2*(1/(beta+np.pi/2)-1/(beta-np.pi/2))


kb2 = 100
theta = np.linspace(-np.pi/2,np.pi/2,10000)
beta = kb2*np.sin(theta)



"""mpl.plot(delta, phi(delta))
mpl.tick_params(direction='in')
mpl.xlabel(f"Déphasage d'un aller-retour dans la cavité pour r={r1} [rad]")
mpl.ylabel("Phase de r [rad]")
mpl.savefig(f"r{r1}phase.pdf")
mpl.show()"""

# dev 5 q3
mpl.plot(beta, sinc(beta), 'y', label="fonction sinc")
mpl.plot(beta, new(beta), 'b', label="fonction d'apodisation")
mpl.tick_params(direction='in')
mpl.xlabel("Valeur de \u03B2 pour une plage d'angle \u03B8 de -\u03C0/2 à \u03C0/2")
mpl.ylabel("F(\u03B2)")
mpl.legend()
mpl.savefig(f"apodisationKb2_{kb2}.pdf")
mpl.show()
