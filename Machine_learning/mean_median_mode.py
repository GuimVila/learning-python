import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed) # The mean value is the average value
y = numpy.median(speed) # The median value is the value in the middle, after you have sorted all the values:
z = stats.mode(speed) # The Mode value is the value that appears the most number of times:

print(x)
print(y)
print(z)
speed.sort()
print(speed)


