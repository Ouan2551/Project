# how to get big data sets
# => create big data for testing use module numpy
# come with number to random data set, any size

import numpy
x = numpy.random.uniform(0.0, 5.0, 250) # (lowest, highest, count)
print(x)

# histogram => use for visualize data set
import matplotlib.pyplot as plt1
# after "as" is just name whatever you want to use
plt1.hist(x, 5)
plt1.show