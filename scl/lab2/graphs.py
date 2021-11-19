import numpy as np
import scipy.io
from scipy.optimize import curve_fit
import re
import matplotlib.pyplot as mpl
import glob


# Useful instances
t = []
u = []
y_exp = {}
y_th = {}
doIt = 1

# Reading the files (with regular expressions!! :))
for file in glob.glob("*.txt"):
    match = re.match(r"5_(\d)([a-z]+).txt", file)
    fich = open(file, 'r')
    mat = list(fich)
    fich.close()
    for i in mat:
        elem_str = i.replace("\n", "")
        elem = elem_str.split(",")
        if doIt:
            t.append(float(elem[0]))
            u.append(float(elem[1]))
        if match[2] == "exp":
            y_exp[int(match[1])] = y_exp.get(int(match[1]), []) + [float(elem[3])]
        else:
            y_th[int(match[1])] = y_th.get(int(match[1]), []) + [float(elem[3])]
    doIt = 0

fig, ax = mpl.subplots(1)
ax.plot(t, u, label="$V_{wf}$ expérimental")
ax.plot(t, y_exp[1], label="$V_{wf}$ obtenu avec IdentSyst")
ax.plot(t, y_th[1], label="$V_{wf}$ théorique")
ax.legend()
ax.set_ylabel('Potentiel [V]')
ax.set_xlabel('Temps [s]')
fig.savefig(f"5_1d")

# mpl.show()
