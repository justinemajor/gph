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
print(moy)

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

syst = ['ystème en vitesse sans frottement ni inertie', 'ystème en vitesse avec inertie supplémentaire', 'ystème en vitesse avec frottement proportionnel à la vitesse', 'ystème en position']
num = ['5_1b', '5_2a', '5_3a', '5_4b']
for index in range(2, 6):
    result = results[index]
    fig2, ax1 = mpl.subplots(1)
    # ax1.set_title("Réponse d'un s"+syst[index-2])
    ax1.set_xlabel('Temps [s]')
    if index == 5:
        ax1.plot(result[0], result[1], 'r-', label='$V_a$(t)')
        ax1.plot(result[0], result[2], 'b-', label="$V_{\u03B8}$(t)")
        ax1.set_ylabel('Potentiel [V]')
    else:
        ax1.plot(result[0][100:] - 1, result[1][100:], 'r-', label='$V_a$(t)')
        ax1.plot(result[0][100:] - 1, result[2][100:], 'b-', label="$V_{wf}$(t)")
        ax1.set_ylabel('Potentiel [V]')
    ax1.legend()
    fig2.savefig(f'{num[index-2]}')

# Show figures
mpl.tight_layout()
# mpl.show()
