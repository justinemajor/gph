import numpy as np


x = 1
y = 1
z = 20
r = (x**2+y**2+z**2)**.5
point = np.array([x, y, z])
position = point[:2]/r


phi = np.arccos(-position[0])
alpha = (180-np.degrees(phi))/2
cosine = np.cos(phi)
sine = np.sin(phi)


theta = np.arccos(-position[1]/np.sin(phi))
beta = (180-np.degrees(theta))/2
cosine2 = np.cos(-theta)
sine2 = np.sin(-theta)


laser = np.array([[-1], [0], [0]])
mirror1 = np.array([[-cosine, sine, 0],
                    [-sine, -cosine, 0],
                    [0, 0, -1]])
mirror2 = np.array([[-1, 0, 0],
                   [0, -cosine2, sine2],
                   [0, -sine2, -cosine2]])
result = mirror2@mirror1@laser*r
result = np.round(result, 3)

print(result)  # Right position!! ;P
# print((result[0]**2+result[1]**2+result[2]**2)**.5/r)

matrix = np.array([[alpha],
                   [beta]])
matrix = np.round(matrix, 1)

print(matrix)

# alpha = round((180-np.degrees(np.arccos(-x/r)))/2, 1)
# beta = round((180-np.degrees(np.arccos(-y/(y**2+z**2)**.5)))/2, 1)
# print(alpha, beta)
# That's it!! ;P
