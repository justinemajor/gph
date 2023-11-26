import numpy as np
import matplotlib.pyplot as plt
import glob
import re
from projet2 import Transfo


transfo = Transfo()

bank = glob.glob("calibration/ir/*")
bank = []

for file in bank:
	data = transfo.read(file)
	data = transfo.transform(data['x'], data['y'])
	data = transfo.cleanData(data['f'], data['A'])
	data['A'] = transfo.lpf(data['A'], 'lpf')
	transfo.graph(data['f'], data['A'])

bank = glob.glob("calibration/visible/*")
bank = []

for file in bank:
	data = transfo.read(file)
	data = transfo.transform(data['x'], data['y'])
	data = transfo.cleanData(data['f'], data['A'])
	data['A'] = transfo.lpf(data['A'], 'lpf')
	transfo.graph(data['f'], data['A'])

bank = glob.glob("tests/filtre_577nm_det*")
file = bank[0]
data = transfo.read(file)
data = transfo.transform(data['x'], data['y'])
data = transfo.cleanData(data['f'], data['A'])
data['A'] = transfo.lpf(data['A'], 'lpf')
transfo.graph(data['f'], data['A'])
print(transfo.principalPeak(data['f'], data['A']))

transfo.clear()
