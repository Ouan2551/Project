# regression => straight line pass all of dot data
# how it work => use relationship between data point
# and draw linear regression

# in machine learning just use it for predict the output value in future
import matplotlib.pyplot as plt
from scipy import stats # use this library to draw regression line

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Linear Regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# R for Relationship => know how relationship between
# value x-axis and y-axis if don't know you can't predict
# r value range from -1 to 1 (0 = no relationship)

slope, intercept, r, p, std_err = stats.linregress(x, y)
print("Relationship_value : ", r)

# Predict Future Values => predict speed of 10 years old car
speed = myfunc(10)
print("speed : ", speed)