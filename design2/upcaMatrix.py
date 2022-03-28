import numpy as np
import cv2
import glob
import matplotlib.pyplot as mpl
import copy
from pyzbar.pyzbar import decode


# the surface pixel shows the reflexivity
# the third axis contains, in order, the information for the direction of the normal, the size of each pixel and their position


"""upca = glob.glob("codeEx*")[0]

im = cv2.imread(upca)
im = im[:,:,0:3]
im = np.mean(im, axis=2)
im = im[100:300,:]

info = np.zeros(im.shape)
im = np.stack((im, *[info]*3), axis=2)
b = {"position":(), "size":(), "normal":()}"""

code = "14563857312"
if len(code) != 11:
	raise Exception("The code has to be of length 11.")
b = [1, 0, 1]
m = [0, 1, 0, 1, 0]
e = [1, 0, 1]
white = [0]*10
l1 = [0, 0, 1, 1, 0, 0, 1]
l2 = [0, 0, 1, 0, 0, 1, 1]
l3 = [0, 1, 1, 1, 1, 0, 1]
l4 = [0, 1, 0, 0, 0, 1, 1]
l5 = [0, 1, 1, 0, 0, 0, 1]
l6 = [0, 1, 0, 1, 1, 1, 1]
l7 = [0, 1, 1, 1, 0, 1, 1]
l8 = [0, 1, 1, 0, 1, 1, 1]
l9 = [0, 0, 0, 1, 0, 1, 1]
l0 = [0, 0, 0, 1, 1, 0, 1]
l = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9]
r1 = [1, 1, 0, 0, 1, 1, 0]
r2 = [1, 1, 0, 1, 1, 0, 0]
r3 = [1, 0, 0, 0, 0, 1, 0]
r4 = [1, 0, 1, 1, 1, 0, 0]
r5 = [1, 0, 0, 1, 1, 1, 0]
r6 = [1, 0, 1, 0, 0, 0, 0]
r7 = [1, 0, 0, 0, 1, 0, 0]
r8 = [1, 0, 0, 1, 0, 0, 0]
r9 = [1, 1, 1, 0, 1, 0, 0]
r0 = [1, 1, 1, 0, 0, 1, 0]
r = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9]
impairs = int(code[0])+int(code[2])+int(code[4])+int(code[6])+int(code[8])+int(code[10])
pairs = int(code[1])+int(code[3])+int(code[5])+int(code[7])+int(code[9])
ver = (10-((impairs)*3+pairs)%10)%10
rVer = r[ver]

im = white+b
for ind, i in enumerate(code):
	if ind <= 5:
		im += l[int(i)]
	elif ind == 6:
		im += m + r[int(i)]
	else:
		im += r[int(i)]
im += rVer + e + white


for i, val in enumerate(im):
	if val == 1:
		im[i] = 0
	else:
		im[i] = 255


im = np.array(im)

reverse = []
for i in im[::-1]:
	reverse.append(i)
reverse = np.array(reverse)

im = np.stack(([im]*10), axis=0)
reverse = np.stack(([reverse]*10), axis=0)


down = decode(reverse)
print(down)

up = decode(im)
print(up)


"""print(im[0,:,0].shape)
add = np.zeros((1,))
print(add.shape)
line = np.append(im[0,:,0], add)
print(line.shape)

nb = []
prec = 0
for i in line:
	if i != prec:
		if prec:
			nb.append(elem)
		elem = 1
	elif i == prec:
		elem += 1
	prec = i
print(min(nb))
print(np.array(nb)%5)
"""


mpl.imshow(im)
mpl.show()
