# Random number does NOT mean a different number every time. Random means something that can not be predicted logically.
# If there is a program to generate random number it can be predicted, thus it is not truly random.
# Random numbers generated through a generation algorithm are called pseudo random.

# In order to generate a truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc.

# In this tutorial we will be using pseudo random numbers.

from numpy import random

x = random.randint(100) # Generates a random integer from 0 to 100. 
print(x)

# The random module's rand() method returns a random float between 0 and 1.

y = random.rand()
print(y)

z = random.randint(100, size=(5)) # Generate a 1-D array containing 5 random integers from 0 to 100:
print(z)

fi = random.randint(100, size=(3, 5))
print(fi)

fa = random.rand(5)
print(fa)


fo = random.rand(3, 5)
print(fo)

# The choice() method allows you to generate a random value based on an array of values.
# The choice() method takes an array as a parameter and randomly returns one of the values.

myChoice = random.choice([3, 5, 7, 9])
print(myChoice)

# The choice() method also allows you to return an array of values.
# Add a size parameter to specify the shape of the array.

myRandomChoice = random.choice([3, 5, 7, 9], size=(3, 5))
print(myRandomChoice)
