import pandas as pd
import os
import re
import fnmatch
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
import glob
from projet2 import Transfo


transfo = Transfo()

bank = glob.glob("calibration/visible/*")
files = []

for file in bank:
	year = re.match(r"calibration/visible/(\d+)_[a-z0-9._]+", file)[1]
	files.append(year)
	data = transfo.read(file)
	data = transfo.transform(data['x'], data['y'])
	data = transfo.cleanData(data['f'], data['A'])
	transfo.collectData(data['A'])

bank = transfo.dataBank
transfo.clear()


mini = min([len(i) for i in bank])
matrix = [i[:mini] for i in bank]


# Principal components analysis and creation of the coefficient matrix
pca = PCA(0.99)  # or n_components=5
principalCoefficients = pca.fit_transform(matrix)
principalComponents = np.array(pca.components_)
inverse = np.linalg.pinv(principalComponents)
moy = np.array(pca.mean_)
m = moy@inverse
coefs = principalCoefficients + m
print(sum(pca.explained_variance_ratio_))


# Compute the concentration of every PC in every raw spectrum data
prop = []
for i in range(len(coefs)):
    tot = sum(coefs[i])
    totr = []
    for it in range(len(coefs[i])):
        totr.append(round(coefs[i][it]/tot*100, 0))
    prop.append(totr)

prop = np.array(prop)
names = np.array([files])
gen = np.hstack((names.transpose(), prop))


# Create the table of concentrations and show
principalDf = pd.DataFrame(data=gen, columns=['Solution'] + [i for i in range(len(pca.components_))])
pd.set_option('display.max_columns', None)
principalDf.head()
print(principalDf)

for i in gen:
	plt.figure()
	plt.plot(range(10), [float(j) for j in i[1:]])
	plt.savefig(f'pcaCoefs/{i[0]}.pdf')
	plt.clf()
	plt.close()
