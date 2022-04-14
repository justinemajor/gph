import numpy as np
import matplotlib.pyplot as plt
import glob
import re


class Transfo:
	def __init__(self):
		self.fileName = ''

	def setFileName(self, fileName:str):
		self.fileName = fileName.strip("calibration").strip('.txt')
		return self.fileName

	def clear(self):
		self.fileName = ''

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
			x.append(float(trio[1]))
			y.append(float(trio[2]))
		x = np.array(x)
		y = np.array(y)
		x = 2*x
		return {'x':x, 'y':y}

	def transform(self, x, y) -> dict:
		transfo = abs(np.fft.fft(y))
		freq = np.fft.fftfreq(len(x), d=(x[-1]-x[0])/len(x)*10**-7)
		return {'f':freq, 'A':transfo}

	def principalPeak(self, f, A) -> float:
		pic = np.argmax(A[int(len(f)/2)+1:])
		pic = abs(f[int(len(freq)/2)+1:][pic])
		pic = pic**-1
		return pic

	def graph(self, f, A, fileName=''):
		if not fileName: fileName = self.fileName
		plt.figure()
		plt.plot(abs(f[int(len(f)/2)+1:]**-1), A[int(len(f)/2)+1:])
		plt.savefig(f'dataBank/{fileName}.pdf')
		plt.clf()
		plt.close()
