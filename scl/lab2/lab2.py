import numpy as np
import scipy.io
from scipy.optimize import curve_fit
import re
import matplotlib.pyplot as mpl
import glob


# Useful instances
results = {}
ampl_u = []
ampl_y = []

# Reading the files (with regular expressions!! :))
for file in glob.glob("*.mat"):
    mat = scipy.io.loadmat(file)
    match = re.match(r"(\d+)_([A-Za-z]+).mat", file)
    if match:
        result = mat.get(match[2]).transpose()
        result = np.vstack((result[0], result[2:]))
        index = int(match[1])
        results[index] = result

# Setting up signal graphs
setup = np.arange(0, 6, 1).reshape(3, 2)
fig1, setup = mpl.subplots(3, 2)

yes = 1
indDeb = 0
for ind, el in enumerate(results[2][0]):
    if el >= 4 and yes:
        indDeb = ind
        yes = 0

moy = np.mean(results[2][2][indDeb+100:])
# print(moy)

"""index = 1
for i, pair in enumerate(setup):
    for j, ax in enumerate(pair):
        if index == 6:
            pass
        else:
            result = results[index]
            ax.plot(result[0], result[1], 'r-')
            ax.plot(result[0], result[2], 'b-', label=f'{index}')
            ax.legend()
            index += 1"""

syst = ['mesuré en 4.1', 'en vitesse sans frottement ni inertie', 'en vitesse avec inertie supplémentaire']
syst += ['en vitesse avec frottement proportionnel à la vitesse', 'en position']
num = ['5_5mod', '5_1b', '5_2a', '5_3a', '5_4b']
for index in range(1, 6):
    result = results[index]
    fig2, ax1 = mpl.subplots(1)
    # ax1.set_title("Réponse d'un système "+syst[index-2])
    ax1.set_xlabel('Temps [s]')
    # ax1.axhline(y=0, linestyle=':', color='k')
    if index == 5:
        ax1.plot(result[0], result[1], 'r-', label='$V_a$(t)')
        ax1.plot(result[0], result[2], 'b-', label="$V_{\u03B8}$(t)")
        ax1.set_ylabel('Potentiel [V]')
    else:
        ax1.plot(result[0][100:] - 1, result[1][100:], 'r-', label='$V_a$(t)')
        ax1.plot(result[0][100:] - 1, result[2][100:], 'b-', label="$V_{wf}$(t)")
        ax1.set_ylabel('Potentiel [V]')
    # ax1.minorticks_on()
    # ax1.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    # ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    ax1.legend()
    fig2.savefig(f'{num[index-1]}')

resultX = results[1][1][501:]
resultY = results[1][2][501:]
y = []
x = []
for i in range(int(len(resultX)/1000)):
    y.append(np.mean(resultY[i*1000+600:(i+1)*1000-1]))
    x.append(resultX[i*1000+1])

y += [y[-1]]*2
x += [4, 5]

fig3, ax3 = mpl.subplots(1)
ax3.plot(x, y, "o-")
ax3.set_xlabel("$V_a$ [V]")
ax3.set_ylabel("$V_{wf}$ [V]")
ax3.minorticks_on()
ax3.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax3.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
mpl.savefig("5_5a")

# print(results[5][1][50])
# print(results[5][1][1250])

# Show figures
mpl.tight_layout()
# mpl.show()
