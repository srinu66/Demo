
import numpy
import torch
import matplotlib.pyplot as plt
from scipy import stats


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)
print('Median Speed '+ str(x))

x = numpy.mean(speed)
print('Mean Speed '+ str(x))

x = numpy.max(speed)
print('Max Speed '+ str(x))

x = numpy.min(speed)
print('Min Speed '+ str(x))

x = numpy.sort(speed)
print(x)

x = numpy.std(speed)
print("Standard Deviation "+ str(x))


ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 32)
print("Percentile "+ str(x))

x = numpy.random.uniform(0,10,20)
print(x)

plt.hist(x,100)
plt.show()

x = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x,100)
plt.show()

x = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(x,100)
plt.show()

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x,y)
plt.show()

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x+ intercept

speed = myfunc(10)

print("Speed of 10 year old car " + str(speed))
