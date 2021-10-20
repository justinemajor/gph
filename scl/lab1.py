import numpy as np
import scipy.io
from scipy.optimize import curve_fit
import re
import matplotlib.pyplot as mpl
import glob


results = 18*[0]
freqs = 18*[0]
ampl_u = 0.5
ampl_y = []
phase = []

for file in glob.glob("*.mat"):
    mat = scipy.io.loadmat(file)
    match = re.match(r"w(\d+)_(\d+)_(\d).mat", file)
    if match:
        result = mat.get('w' + match[2] + match[3]).transpose()
        result = np.vstack((result[0], result[2:]))
        freq = float(match[2]) + float(match[3]) / 10
        results[int(match[1])] = result
        freqs[int(match[1])] = freq


def sinus(t, a, w, phi, b):
    return a * np.sin(w*t + phi) + b


setup = np.arange(0, 18, 1).reshape(6, 3)
fig1, setup = mpl.subplots(6, 3)

index = 0
for i, trio in enumerate(setup):
    for j, ax in enumerate(trio):
        result = results[index]
        popt_y, _ = curve_fit(sinus, result[0][50:], result[2][50:], p0=[5, freqs[index], 0, 1])
        ampl_y.append(popt_y[0])
        phase.append(popt_y[2])
        ax.plot(result[0], result[1], 'r-')
        ax.plot(result[0], result[2], 'b-', label=f'w={freqs[index]}')
        ax.plot(result[0], sinus(result[0], *popt_y), 'g-')
        ax.legend()
        index += 1


for i, amp in enumerate(ampl_y):
    if amp < 0:
        phase[i] = phase[i] - np.pi
        ampl_y[i] = -amp

Re = []
Im = []

for i, phi in enumerate(phase):
    x = ampl_y[i]/ampl_u * np.exp(phi*1j)
    Re.append(np.real(x))
    Im.append(np.imag(x))

fig4, ax4 = mpl.subplots()
ax4.axhline(y=0, color='k')
ax4.axvline(x=0, color='k')
ax4.plot(Re, Im, label='Nyquist')
ax4.minorticks_on()
ax4.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax4.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax4.legend()


ampl_y = np.array(ampl_y)
rapport = 20*np.log10(ampl_y/ampl_u)
phase = (np.array(phase))*180/2/np.pi

fig2, ax1 = mpl.subplots()
ax1.axhline(y=0, color='k')
ax1.semilogx(freqs, phase, '-', label='Bode freq')
ax1.semilogx(freqs, rapport, label='Bode rapport')
ax1.minorticks_on()
ax1.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax1.legend()

fig3, ax3 = mpl.subplots()
ax3.axhline(y=0, color='k')
ax3.axvline(x=0, color='k')
ax3.plot(phase, rapport, label='Black')
ax3.minorticks_on()
ax3.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax3.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax3.legend()

mpl.show()
