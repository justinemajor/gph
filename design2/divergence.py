import numpy as np


diameter = np.array([21.355, 26.402, 30.799])
rayon = diameter/2
distance = np.array([38, 38+7.5, 38+2*7.5])

angle = []

for ind, i in enumerate(rayon):
    ang = np.arctan(i/distance[ind])
    ang = np.degrees(ang)
    ang *= 2
    angle.append(ang)

angle = np.array(angle)
moy = np.mean(angle)
