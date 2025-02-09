import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)
# bell curve graph
# "numpy.random.normal create value the most value is 5.0
# and smallest is 1.0"
plt.hist(x, 100)
plt.show()