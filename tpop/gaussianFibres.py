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
y1 /= max(y1)
x1 -= x1[np.argmax(y1)]

x = []
y = []

for index, i in enumerate(y1):
    if 1: #i != min(y1):
        x.append(x1[index])
        y.append(i)

x = np.array(x)
y = np.array(y)

def gauss(x, a, b, x0, sigma, d):
    return a * np.exp(b * (x - x0)**2 / (2 * sigma**2)) + d


n = len(x)
mean = sum(x * y) / n
sigma = (sum(y * (x - mean) ** 2) / n) ** .5

popt, pcov = curve_fit(gauss, x, y, p0=[2, 2, mean, sigma, 1])

fig1, xy = mpl.subplots(1)
xy.plot(x, y)
xy.plot(x, gauss(x, *popt))
xy.tick_params(axis="y", direction="in")
xy.tick_params(axis="x", direction="in")
mpl.show()
