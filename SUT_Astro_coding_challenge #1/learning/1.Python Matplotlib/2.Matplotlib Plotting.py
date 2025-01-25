import numpy as np
import matplotlib.pyplot as plt

# custom for use '.' for plot
x = np.array([2,50])
y = np.array([10,30])

# multiple plot
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

# plot with no x axis graph will default x axis
# from 0 to n when n = count of array
ypoints2 = np.array([3, 8, 1, 10, 5, 7])

# plot without line
plt.plot(x, y, '.')

# multiple points
plt.plot(xpoints, ypoints, '.')

# plot with no x axis
plt.plot(ypoints2)

plt.show()