# Polynomial Regression => if data not fit for
# linear regression just use this

# is like linear regression just draw line through data points

import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

#specify how line will display (start_position, end_position, count_point)
my_line = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(my_line, mymodel(my_line))
plt.show()

# R-Squared => use for predict range 0 - 1
# (0 = no relationship) (1 = 100% related)

from sklearn.metrics import r2_score

print("relationship_value : ",r2_score(y, mymodel(x)))

# Predict Future Values => this example predict speed car at time 17:00
speed = mymodel(17)
print("Speed_car_at_17:00 : ", speed)