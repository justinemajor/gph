import numpy as np
import matplotlib.pyplot as plt


noir = [67, 67, 65, 67, 67, 66, 66, 66, 66, 65, 67, 67, 66, 65, 66, 67, 68, 68, 67, 69, 68, 66, 64, 65, 67, 68, 68, 68, 67, 66, 65]
bleu = [67, 67, 66, 66, 65, 65, 66, 69, 69, 72, 70, 66, 66, 69, 70, 68, 66, 66, 67, 67, 67, 68, 69, 70, 72, 72, 72, 69, 69, 71, 69]
orange = [69, 66, 65, 67, 67, 66, 67, 68, 69, 69, 69, 70, 70, 70, 69, 68, 67, 70, 70, 69, 68, 68, 68, 67, 66, 67, 67, 68, 69, 70, 71]

temps = np.arange(0, 310, 10)

plt.plot(temps, noir, 'k:')
plt.plot(temps, bleu, 'b:')
plt.plot(temps, orange, 'r:')
plt.show()

"""moyNoir = np.round(np.mean(noir), 2)
moyBleu = np.round(np.mean(bleu), 2)
moyOrange = np.round(np.mean(orange), 2)

print(moyNoir, moyBleu, moyOrange)

stdNoir = np.round(np.std(noir), 2)
stdBleu = np.round(np.std(bleu), 2)
stdOrange = np.round(np.std(orange), 2)

print(stdNoir, stdBleu, stdOrange)"""