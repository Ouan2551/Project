# Multiple Regression => predict value using variable more than 2
import numpy
import matplotlib as plt1

# main library used
import pandas # used for read csv file

data = pandas.read_csv("D:\Important files Nannaphat\coding\Project\Machine_Learning\data.csv")
print(data)

# warning if have multiple use '[]' two time
X = data[['Weight', 'Volume']]
Y = data['CO2']
print(X)
print(Y)

from sklearn import linear_model
regr = linear_model.LinearRegression()
# use linearregression() to create linear regression object
regr.fit(X, Y) # use method fit()

# predict weight = 2300, volume = 1300
predictedCO2 = regr.predict([[2300, 1300]])
print("PredictCO2 (first) : ", predictedCO2)

# Coefficient => value that describes relationship with unknown variable
# Example: if x is a variable, then 2x is x two times
# x is the unknown variable, and the number 2 is the coefficient

print("Coefficient : ", regr.coef_)

# These values tell us that if the weight increase by 1kg
# the CO2 emission increases by 0.00755095g
# And if the engine size (Volume) increases by 1cm3
# the CO2 emission increases by 0.00780526g
predictedCO2 = regr.predict([[3300, 1300]])
print("PredictCO2 (second) : ", predictedCO2)