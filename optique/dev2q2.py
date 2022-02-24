import numpy as np


nti2 = 1.333**2
angi = np.radians(60)
sine = np.sin(angi)
cosine = np.cos(angi)


ro = (cosine-(nti2-sine**2)**.5)/(cosine+(nti2-sine**2)**.5)
re = (nti2*cosine-(nti2-sine**2)**.5)/(nti2*cosine+(nti2-sine**2)**.5)

# print(ro, re)

ro **= 2
re **= 2

d = (ro-re)/(ro+re)
print(d*100)
