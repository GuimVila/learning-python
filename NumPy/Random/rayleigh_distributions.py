# Rayleigh distribution is used in signal processing.

# It has two parameters:

# scale - (standard deviation) decides how flat the distribution will be default 1.0).

# size - The shape of the returned array.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.rayleigh(scale=2, size=(2, 3))
print(x)

sns.kdeplot(random.rayleigh(size=1000))
plt.show()