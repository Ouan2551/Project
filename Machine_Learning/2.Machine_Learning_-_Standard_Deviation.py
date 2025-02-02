# standard deviation => number that describes how 
# spread out the value are

# low standard deviation => value is near than avg
# high standard deviation => value is over than avg

import numpy
speed = [86,87,88,86,87,85,86]

# find standard deviation
print(numpy.std(speed))

# variance => number show value spread out

# step how to find variance
# 1) find mean value
# 2) value in list - mean equal for find difference
# 3) difference power by 2 
# 4) and then plus all difference power by 2
# and divide it by 2 you will get value variance

print(numpy.var(speed))