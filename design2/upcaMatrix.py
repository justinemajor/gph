import numpy as np
import cv2
import glob
import matplotlib.pyplot as mpl
import copy


# the surface pixel shows the reflexivity
# the third axis contains, in order, the information for the direction of the normal, the size of each pixel and their position


upca = glob.glob("codeEx*")[0]

code = np.zeros((10, 10, 3))
surface = code[:,:,0]

im = cv2.imread(upca)
im = im[:,:,0:3]
im = np.mean(im, axis=2)
im = im[50:300,:]

info = np.zeros(im.shape)
im = np.stack((*[im]*3, info), axis=2)
b = {"position":(), "size":(), "normal":()}
print(im.shape)

for i, line in enumerate(im):
	for j, val in enumerate(line):
		if val[0] >= 250:
			im[i,j] = .95
		else:
			im[i,j] = .05


# mpl.imshow(im)
# mpl.show()
