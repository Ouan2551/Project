import numpy

#Standard Deviation => describes how spread out the values are
    #A low standard deviation => most of the numbers
                    #are close to the mean (average) value
    #A high standard deviation => values are spread out
                    #over a wider range


speed1 = [86,87,88,86,87,85,86]
x = numpy.std(speed1)
print(x)

speed2 = [32,111,138,28,59,77,97]
y = numpy.std(speed2)
print(y)