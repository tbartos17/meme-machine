import matplotlib.pyplot as plt
import numpy
import math

data1 = [-20,-20,-20,-15,-15,-15,-10,-10,-10,-5,-5,-5,0,0,0,5,5,5,10,10,10,15,15,15,20,20,20]
data2 = [6.52,6.86,3.03,3.29,2.40,3.02,1.86,4.16,3.50,1.32,1.37,1.19,0,0,0,2.50,1.52,1.32,2.64,2.97,1.98,2.59,2.64,2.70,2.24,3.42,2.63]

dataleft = [-20,-20,-20,-15,-15,-15,-10,-10,-10,-5,-5,-5,0,0,0]
dataleft2 = [6.52,6.86,3.03,3.29,2.40,3.02,1.86,4.16,3.50,1.32,1.37,1.19,0,0,0]

dataright = [0,0,0,5,5,5,10,10,10,15,15,15,20,20,20]
dataright2 = [0,0,0,2.50,1.52,1.32,2.64,2.97,1.98,2.59,2.64,2.70,2.24,3.42,2.63]

def function(x):
    test = x
    x = []
    for value in test:
        if value != 0:
            x.append(value**(-1))
        else:
            x.append(value)
    return x

dataleft2 = function(dataleft2)

##plt.plot(numpy.unique(dataright), numpy.poly1d(numpy.polyfit(dataright, dataright2, 1))(numpy.unique(dataright)))
##plt.plot(dataright, dataright2, "ro")
##plt.xlabel('Change in Volume (mL)')
##plt.ylabel('Time (s)')
##plt.show()

plt.plot(numpy.unique(dataleft), numpy.poly1d(numpy.polyfit(dataleft, dataleft2, 1))(numpy.unique(dataleft)))
plt.plot(dataleft, dataleft2, "ro")
plt.xlabel('Change in Volume (mL)')
plt.ylabel('Time (s)')
plt.show()

