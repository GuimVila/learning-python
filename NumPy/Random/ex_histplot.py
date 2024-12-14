# Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
# Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.
# Distplot is deprecated 

import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot([0, 1, 2, 3, 4, 5], kde=True)

plt.show()