import numpy
# library numpy working with array
from scipy import stats

# mean => average value
# median => middle value
# mode => most common value

# list name speed
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# find mean normal way
print(sum(speed)/len(speed)) # use length array to divide
# or using function from numpy library
print(numpy.mean(speed))

# find median
print(numpy.median(speed))
# if it have two number it middle
# this function will plus two number
# after then divide by 2 will get value median

# find mode => use library scipy
print(stats.mode(speed))