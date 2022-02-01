import numpy as np
from scipy.optimize import curve_fit
import re
import matplotlib.pyplot as mpl


def w1(Z):
    return 632.8*4.5/np.pi/(315**2+(.65**2)*(Z**2))**.5

a = 2.405/0.12*620/2/np.pi
V = 2*np.pi*a/630*.12
w2 = a/1000*(.65+1.619*V**(-1.5)+2.879*V**(-6))

def t(Z):
    return (2*w1(Z)*w2/(w1(Z)**2+w2**2))**2

z = np.linspace(0, 1000, 100000)
peakIndex = np.argmax(t(z))
peakPosition = z[peakIndex]
peakCoord = peakPosition/1000, np.max(t(z))


fig1, tz = mpl.subplots(1)
tz.plot(z/1000, t(z))
tz.set_xlabel("Z [m]")
tz.set_ylabel("T [-]")
tz.arrow(peakCoord[0], peakCoord[1]-.1, 0, 0.1, length_includes_head=True, head_width=.01)
tz.annotate(f"max à Z={peakPosition:.1f}mm", peakCoord)
tz.tick_params(axis="y", direction="in")
tz.tick_params(axis="x", direction="in")
fig1.savefig("fibres.pdf")
fig1.savefig("fibres.eps")
fig1.savefig("fibres")
# mpl.show()