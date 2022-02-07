import numpy as np
from scipy.optimize import curve_fit
import re
import scipy as sp
import matplotlib.pyplot as mpl
import glob


filePath = glob.glob("*.csv")[0]
file = open(filePath, 'r')
results = list(file)
file.close()
x1, y1 = [], []
results = results[1:]
for i in results:
    result = i.replace('\n', '').split(',')
    x1.append(float(result[0]))
    y1.append(float(result[1]))

x1 = np.array(x1)
y1 = np.array(y1)
y1 -= np.min(y1)
y1 /= max(y1)
x1 -= x1[np.argmax(y1)]

x = []
y = []

for index, i in enumerate(y1):
    if 1:  # i != min(y1):
        x.append(x1[index])
        y.append(i)

x = np.array(x)
y = np.array(y)


def gauss(x, a, b, x0, sigma, d):
    return a * np.exp(b * (x - x0)**2 / (2 * sigma**2)) + d


n = len(x)
mean = sum(x * y) / n
sigma = (sum(y * (x - mean) ** 2) / n) ** .5

popt, pcov = curve_fit(gauss, x, y, p0=[1, 1, mean, sigma, 0])

maxi = np.max(gauss(x, *popt))
mid = maxi/2


def invGauss(y, a, b, x0, sigma, d):
    return (np.log((y-d)/a)*(2 * sigma**2)/b)**.5+x0


mid1 = invGauss(mid, *popt)
mid2 = -mid1
mhw = mid1-mid2
print(mhw)

fig1, xy = mpl.subplots(1)
xy.plot(x, y, '.', mfc="dimgray", mec="dimgray", label="mesures expérimentales")
xy.plot(x, gauss(x, *popt), 'k', label="courbe gaussienne « fittée »")
xy.arrow(0, mid-.125, 0, 0.1, color="silver", length_includes_head=True, width=.0005, head_length=.025)
xy.plot([mid2, mid1], [mid]*2, color="silver", label="diamètre du faisceau laser")
xy.annotate(f"{mhw:.3f} m", [-0.003, 0.3])
xy.tick_params(axis="y", direction="in")
xy.tick_params(axis="x", direction="in")
xy.set_xlabel("Longueur [m]")
xy.set_ylabel("Intensité lumineuse relative [-]")
xy.legend()
fig1.savefig("gaussian.pdf")
# mpl.show()
