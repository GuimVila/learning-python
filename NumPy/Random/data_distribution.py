# Data Distribution is a list of all possible values, and how often each value occurs.
# Such lists are important when working with statistics and data science.

# Random Distribution 

# A random distribution is a set of random numbers that follow a certain probability density function.
# Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)

# The sum of all probability numbers should be 1.

y = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(y)

z = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5, 2))

print(z)