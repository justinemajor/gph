import numpy as np
import matplotlib.pyplot as plt
import glob
import re


class Transfo:
	def __init__(self):
		self.fileName = ''
		self.dataBank = []

	def setFileName(self, fileName:str):
		self.fileName = fileName.strip("calibration").strip('.txt').strip('tests')
		return self.fileName

	def clear(self):
		self.fileName = ''
		self.dataBank = []

	def read(self, fileName:str) -> dict:
		grab = glob.glob(fileName)[0]
		self.setFileName(grab)
		file = open(grab, 'r')
		results = list(file)
		file.close()
		results = results[0:]
		x, y = [], []
		for ind, i in enumerate(results):
			trio = i.replace("\n", '').split('\t')
			# for ind, i in enumerate(trio[:-1]):
				# exp = re.match(r"(\s*-*[0-9.]+)E\+*(\-*\d+)", i)
				# trio[ind] = float(exp[1])*10**int(exp[2])
			x.append(float(trio[1])*10**-7)
			y.append(float(trio[2])*10**-3)
		x = np.array(x)
		y = np.array(y)
		x = 2*x
		return {'x':x, 'y':y}

	def transform(self, x, y) -> dict:
		transfo = abs(np.fft.fft(y))
		freq = np.fft.fftfreq(len(x), d=(x[-1]-x[0])/(len(x)-1))
		return {'f':freq, 'A':transfo}

	def cleanData(self, f, A):
		restrictF = []
		restrictA = []
		for ind, i in enumerate(f):
			if i != 0:
				i = i**-1*10**9
			if 0 < i <= 1600:
				restrictF.append(i)
				restrictA.append(A[ind])
		return {'f':restrictF, 'A':restrictA}

	def principalPeak(self, f, A) -> float:
		pic = np.argmax(A)
		pic = f[pic]
		return pic

	def graph(self, f, A, fileName=''):
		if not fileName: fileName = self.fileName
		plt.figure()
		plt.tick_params(direction='in')
		plt.plot(f, A)
		plt.xlabel("Longueur d'onde [nm]")
		plt.ylabel('Intensité relative [u.a.]')
		plt.savefig(f'dataBank/{fileName}.pdf')
		# plt.show()
		plt.clf()
		plt.close()

	def collectData(self, A):
		self.dataBank.append(A)

	def lpf(self, A, filt):
		"""Fourier transformation"""
		fft = np.fft.fft(A)

		"""Apply a "symmetrical" filter, either high-pass or low-pass"""
		# Better when keeping the first point, because of a vertical translation/alignment
		nCut = 400
		tot = len(fft)
		ff = filt  # frequency filter, which has a value of either "lpf" or "hpf"

		if tot % 2 == 1:
		    lmi = int((tot-1)/2)  # lowerMiddleIndex
		    umi = lmi + 1  # upperMiddleIndex
		else:
		    lmi = int(tot/2)
		    umi = lmi

		"""For high-pass filter (HPF)"""
		if ff == "hpf":
		    fft[1:1+nCut] = np.zeros(nCut)
		    fft[-nCut:] = np.zeros(nCut)  # symmetrical!

		"""For low-pass filter (LPF)"""
		if ff == "lpf":
		    lowerLimit = lmi-nCut+1
		    upperLimit = umi+nCut
		    fft[lowerLimit:upperLimit] = np.zeros(len(fft[lowerLimit:upperLimit]))

		if ff not in ["lpf", "hpf"]:
		    raise ValueError("The value given to the frequency filter is not an option. Please choose between 'lpf' and 'hpf'.")

		"""Reconstruct the spectrum with the filtered fft"""
		dft = np.fft.ifft(fft)
		return dft










