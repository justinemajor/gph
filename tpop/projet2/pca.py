import pandas as pd
import os
import re
import fnmatch
from sklearn.decomposition import PCA, FastICA
import numpy as np
import matplotlib.pyplot as plt
import glob
from projet2 import Transfo


transfo = Transfo()

bank = glob.glob("calibration/visible/*")
print(bank)
files = []
colors = []
freq = []

for file in bank:
	groups = re.match(r"calibration/visible/([a-zA-Z0-9 ]*)_\w+_(\w+).txt", file)
	year = groups[1]
	color = groups[2]
	files.append(year)
	colors.append(color)
	data = transfo.read(file)
	data = transfo.transform(data['x'], data['y'])
	data = transfo.cleanData(data['f'], data['A'])
	data['A'] = transfo.lpf(data['A'], 'lpf')
	transfo.collectData(data['A'])
	freq = data['f']

bank = transfo.dataBank
transfo.clear()


mini = min([len(i) for i in bank])
matrix = [i[:mini] for i in bank]
freq = freq[:mini]



# Principal components analysis and creation of the coefficient matrix
# ica = FastICA(n_components=9)
# fitted = ica.fit_transform(matrix)
ica = PCA(0.99)  # or n_components=5
principalCoefficients = ica.fit_transform(np.real(matrix))
principalComponents = np.array(ica.components_)
inverse = np.linalg.pinv(principalComponents)
moy = np.array(ica.mean_)
m = moy@inverse
coefs = principalCoefficients + m
# print(sum(pca.explained_variance_ratio_))
# coefs = fitted


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
principalDf = pd.DataFrame(data=gen, columns=['Solution'] + [i for i in range(len(ica.components_))])
pd.set_option('display.max_columns', None)
principalDf.head()
print(principalDf)

for ind, i in enumerate(gen):
	plt.figure()
	plt.plot(range(len(ica.components_)), [abs(float(j)) for j in i[1:]])
	plt.savefig(f'pcaCoefs/ir_{i[0]}_{ind}.pdf')
	plt.clf()
	plt.close()

plt.figure()
plt.tick_params(direction='in')
for ind, i in enumerate(matrix):
	plt.plot(freq, i, label=f'{files[ind]}', color=colors[ind])

handles, labels = plt.gca().get_legend_handles_labels()
# sort both labels and handles by labels
labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
plt.legend(handles, labels)

plt.xlabel("Longueur d'onde [nm]")
plt.ylabel('Intensité relative [u.a.]')
plt.savefig('visible_tot.pdf')
plt.show()
