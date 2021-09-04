# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 13:40:29 2021

@author: Dell

"""
#Linear regression
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import sklearn.linear_model as lm
import numpy
from sklearn.metrics import r2_score

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#scipy method for line of regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

#function for our line of regression
def myfunc(x):
  return slope * x + intercept
#map the x values to the new y values
mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

#poly regression

#basic data set
x = [1,2,3,4,6,7,8,9,10,12,13,14,15,16,18,19,21,23]
y = [101,94,83,45,60,66,60,65,71,71,75,76,78,79,90,99,99,120]

#NumPy has a method that lets us make a polynomial model
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
#specify how the line will display
myline = numpy.linspace(1, 22, 100)
#plot our scatterplot and line of regression
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
#print r-squared which is the relstionship value
print(r2_score(y, mymodel(x)))


#scaling data

 
df=pd.read_csv("https://www.w3schools.com/python/cars2.csv")
from sklearn.preprocessing import StandardScaler

scale=StandardScaler()
x=df[['Volume','Weight']]
scaledx=scale.fit_transform(x)
print(scaledx)