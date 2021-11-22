import numpy as np
import scipy.io
from scipy.optimize import curve_fit
import re
import matplotlib.pyplot as mpl
import glob


# Useful instances
t = {}
u = {}
y_exp = {}
y_th = {}

# Reading the files (with regular expressions!! :))
for file in glob.glob("*.txt"):
    match = re.match(r"5_(\d)([a-z]+).txt", file)
    fich = open(file, 'r')
    mat = list(fich)
    fich.close()
    for i in mat:
        elem_str = i.replace("\n", "")
        elem = elem_str.split(",")
        t[int(match[1])] = t.get(int(match[1]), []) + [float(elem[0])]
        u[int(match[1])] = u.get(int(match[1]), []) + [float(elem[1])]
        if match[2] == "exp":
            y_exp[int(match[1])] = y_exp.get(int(match[1]), []) + [float(elem[3])]
        else:
            y_th[int(match[1])] = y_th.get(int(match[1]), []) + [float(elem[3])]

for key, val in t.items():
    t[key] = t[key][:int(len(val)/2)]
    u[key] = u[key][:int(len(val)/2)]

fig, ax = mpl.subplots(1)
ax.plot(t[1], u[1], label="$V_{wf}$ expérimental")
ax.plot(t[1], y_exp[1], label="$V_{wf}$ obtenu avec IdentSyst")
ax.plot(t[1], y_th[1], label="$V_{wf}$ théorique")
ax.legend()
ax.set_ylabel('Potentiel [V]')
ax.set_xlabel('Temps [s]')
fig.savefig(f"5_1d")

fig2, ax2 = mpl.subplots(1)
ax2.plot(t[4], u[4], label="$V_{\u03B8}$ expérimental")
ax2.plot(t[4], y_exp[4], label="$V_{\u03B8}$ obtenu avec IdentSyst")
ax2.plot(t[4], y_th[4], label="$V_{\u03B8}$ théorique")
ax2.legend()
ax2.set_ylabel('Potentiel [V]')
ax2.set_xlabel('Temps [s]')
fig2.savefig(f"5_4d")

# mpl.show()
