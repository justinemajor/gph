import numpy as np
import matplotlib.pyplot as plt
import glob
import re


plt.figure()
grab = glob.glob("tests/hpfilter_700nm_detvisible.txt")[0]
print(grab)
file = open(grab, 'r')
results = list(file)
file.close()
results = results[0:]
x, y = [], []
for ind, i in enumerate(results):
	trio = i.replace("\n", '').split('\t')
	x.append(float(trio[1]))
	y.append(float(trio[2]))

transfo = np.fft.fft(y)
# transfo = np.append(transfo, transfo[0])
freq = np.fft.fftfreq(len(x), d=(x[-1]-x[0])/len(x)*10**-6)

pic = np.argmax(np.imag(transfo))
pic = freq[pic]
# pic = pic*2*np.pi
print(pic)
pic = pic**-1
print(pic)

plt.subplot(311)
plt.plot(x, y)
plt.subplot(312)
plt.plot(freq, np.real(transfo))
plt.subplot(313)
plt.plot(freq, np.imag(transfo))
# plt.show()
