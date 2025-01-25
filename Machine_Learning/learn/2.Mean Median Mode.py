import numpy #use in Mean and Median
from scipy import stats
#Mean => average value
#Median => mid point value
#Mode => most common value

#e.g.
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#Mean
x = numpy.mean(speed)
print("x (mean) : ", x)

#Median
y = numpy.median(speed)
print("y (median) : ", y)

#Mode
z = stats.mode(speed)
print("z (mode) : ", z)