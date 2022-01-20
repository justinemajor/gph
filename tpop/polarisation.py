import numpy as np
import scipy.io
from scipy.optimize import curve_fit
import re
import matplotlib.pyplot as mpl
import glob


degreeSign = u"\N{DEGREE SIGN}"


def malus(theta):
    return np.cos(theta)**2

x = np.linspace(0, np.pi, 1000)

figMalus, mal = mpl.subplots(1)
mal.plot(np.degrees(x), malus(x))
mal.set_ylabel("Transmission $I/I_0$")
mal.set_xlabel("Angle relatif [$^{o}$]")
figMalus.savefig("malus")


def brewster(n2):
    return np.degrees(np.arctan(n2))

x = np.linspace(1.33, 1.7, 1000)

angle = brewster(1.495)

figBrewster, brew = mpl.subplots(1)
brew.plot(x, brewster(x))
brew.set_xlabel("Indice du milieu")
brew.set_ylabel(f"Angle de Brewster [{degreeSign}]")
brew.plot(1.495, angle, 'o')
brew.annotate(f"Angle attendu avec le plexiglass : {angle:.2f}{degreeSign}", (1.495, angle-.3))
figBrewster.savefig("brewster")


n1 = 1
# n2 = 1.495

def cosTheta2(theta1, n2):
    return np.sqrt(1-(n1/n2*np.sin(theta1))**2)

def rs(theta1, n2):
    return ((n1*np.cos(theta1)-n2*cosTheta2(theta1, n2))/(n1*np.cos(theta1)+n2*cosTheta2(theta1, n2)))**2

def rp(theta1, n2):
    return ((n1*cosTheta2(theta1, n2)-n2*np.cos(theta1))/(n1*cosTheta2(theta1, n2)+n2*np.cos(theta1)))**2

x = np.linspace(0, np.pi/2, 1000)

coefRef, ref = mpl.subplots(1)
ref.plot(np.degrees(x), rs(x, 1.495), label="TE")
ref.plot(np.degrees(x), rp(x, 1.495), label="TM")
ref.set_xlabel(f"Angle d'incidence [{degreeSign}]")
ref.set_ylabel("Intensité relative de l'onde réfléchie")
ref.plot(angle, 0, 'ko', label=f"Angle de Brewster à {angle:.2f}{degreeSign}")
ref.axhline(y=0, color='k')
ref.axvline(x=0, color='k')
ref.grid()

"""Results"""
deg = np.arange(10, 85, 5)
deg = np.radians(deg)
tm = np.array([20.1, 19, 17.4, 15.4, 13, 10.3, 7.2, 4.1, 1.8, 0.05, 2.2, 10.6, 29.8, 71.8, 152.6])
tm /= 500
te = np.array([4.1, 5.1, 5.7, 7.2, 5.2, 7.9, 10.3, 14.6, 20.9, 31.4, 87.9, 121.8, 163, 184, 227])
te /= 500

popt, pcov = curve_fit(rp, deg, tm, p0=[2])
popt2, pcov2 = curve_fit(rs, deg, te, p0=[2])

ref.plot(np.degrees(deg), tm, label="TM expérimental")
ref.plot(np.degrees(deg), rp(deg, *popt), label=f"curvefit TM, n={popt[0]:.3f}")
ref.plot(np.degrees(deg), te, label="TE expérimental")
ref.plot(np.degrees(deg), rs(deg, *popt), label=f"curvefit TE, n={popt2[0]:.3f}")
ref.legend()
coefRef.savefig("coefficientReflexion")


mpl.show()