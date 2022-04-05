import matplotlib.pyplot as mpl
import numpy as np


def sinc(beta):
	return np.sin(beta)/beta

def new(beta):
	return np.cos(beta)/2*(1/(beta+np.pi/2)-1/(beta-np.pi/2))


kb2 = 100
theta = np.linspace(-np.pi/2,np.pi/2,10000)
beta = kb2*np.sin(theta)


mpl.plot(beta, sinc(beta), 'y', label="fonction sinc")
mpl.plot(beta, new(beta), 'b', label="fonction d'apodisation")
mpl.tick_params(direction='in')
mpl.xlabel("Valeur de \u03B2 pour une plage d'angle \u03B8 de -\u03C0/2 a \u03C0/2")
mpl.ylabel("F(\u03B2)")
mpl.legend()
mpl.savefig(f"apodisationKb2_{kb2}.pdf")
mpl.show()
