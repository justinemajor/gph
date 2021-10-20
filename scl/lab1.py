import numpy as np
import scipy.io
from scipy.optimize import curve_fit
import re
import matplotlib.pyplot as mpl
import glob


# Useful instances
results = 18*[0]
freqs = 18*[0]
ampl_u = 0.5
ampl_y = []
phase = []

# Reading the files
for file in glob.glob("*.mat"):
    mat = scipy.io.loadmat(file)
    match = re.match(r"w(\d+)_(\d+)_(\d).mat", file)
    if match:
        result = mat.get('w' + match[2] + match[3]).transpose()
        result = np.vstack((result[0], result[2:]))
        freq = float(match[2]) + float(match[3]) / 10
        results[int(match[1])] = result
        freqs[int(match[1])] = freq

# Sinus function for curvefitting
def sinus(t, a, w, phi, b):
    return a * np.sin(w*t + phi) + b

# Setting up signal graphs
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

# Making sure every sinus has a positive gain
for i, amp in enumerate(ampl_y):
    if amp < 0:
        phase[i] = phase[i] - np.pi
        ampl_y[i] = -amp

# Nyquist graph
Re = []
Im = []

for i, phi in enumerate(phase):
    x = ampl_y[i]/ampl_u * np.exp(phi*1j)
    Re.append(np.real(x))
    Im.append(np.imag(x))

fig4, ax4 = mpl.subplots()
ax4.axhline(y=0, color='k')
ax4.axvline(x=0, color='k')
ax4.plot(Re, Im)
ax4.minorticks_on()
ax4.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax4.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax4.set_title('Lieu de Nyquist')
ax4.set_xlabel('Re')
ax4.set_ylabel('Im')
fig4.savefig('Nyquist')

# Setting important variables: gain and phase
ampl_y = np.array(ampl_y)
gain = 20 * np.log10(ampl_y / ampl_u)
phase = (np.array(phase))*180/2/np.pi

# Bode diagrams (Phase & gain)
fig2, (ax1, ax2) = mpl.subplots(2, 1)
ax1.axhline(y=0, color='k')
ax1.semilogx(freqs, phase)
ax1.minorticks_on()
ax1.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax1.set_title('Diagrammes de Bode')
ax1.set_xlabel('\u03C9 [rad/s]')
ax1.set_ylabel('Phase [\u00B0]')

ax2.axhline(y=0, color='k')
ax2.semilogx(freqs, gain)
ax2.minorticks_on()
ax2.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax2.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax2.set_xlabel('\u03C9 [rad/s]')
ax2.set_ylabel("Gain [dB]")
fig2.savefig('Bode')

# Black graph
fig3, ax3 = mpl.subplots()
ax3.axhline(y=0, color='k')
ax3.axvline(x=0, color='k')
ax3.plot(phase, gain)
ax3.minorticks_on()
ax3.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax3.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax3.set_title('Lieu de Black')
ax3.set_xlabel('Phase [\u00B0]')
ax3.set_ylabel("Gain [dB]")
fig3.savefig('Black')

# show
mpl.tight_layout()
mpl.show()
