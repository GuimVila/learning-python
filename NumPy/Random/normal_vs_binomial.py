from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.kdeplot(random.normal(loc=50, scale=5, size=1000), label='normal')
sns.kdeplot(random.binomial(n=100, p=0.5, size=1000), label='binomial')

# Afegir la llegenda per mostrar els labels
plt.legend()
plt.show()