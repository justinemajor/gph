import numpy as np
import matplotlib.pyplot as plt
import glob
import re
from projet2 import Transfo


transfo = Transfo()

bank = glob.glob("calibration/ir/*")

for file in bank:
	data = transfo.read(file)
	data = transfo.transform(data['x'], data['y'])
	transfo.graph(data['f'], data['A'])

bank = glob.glob("calibration/visible/*")

for file in bank:
	data = transfo.read(file)
	data = transfo.transform(data['x'], data['y'])
	transfo.graph(data['f'], data['A'])

transfo.clear()
