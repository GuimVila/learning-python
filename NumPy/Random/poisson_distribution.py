# Poisson Distribution is a Discrete Distribution.

# It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

# It has two parameters:

# lam - rate or known number of occurrences e.g. 2 for above problem.

# size - The shape of the returned array.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

from numpy import random

x = random.poisson(lam=2, size=10)

print(x)

sns.histplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()