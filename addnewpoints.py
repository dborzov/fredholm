# -*- coding: utf-8 -*-

import equation
from pylab import *
import pickle

dimensions='2D'
L=20.
to=18.15
stepus=0.01
fromus=1.1
pointnumber=100.


xlog = arange(math.log(fromus), math.log(to), math.log(to/fromus)/pointnumber)
x=[math.exp(each) for each in xlog]
#array_of_computations=pickle.load(open( "computedpoints.pickle", "rb" ))
array_of_computations=[]

for i in range(0,len(x)):
    dot=equation.equation(x[i], dimensions, L)
    dot.solve()
    array_of_computations.append(dot)
    print ('['+str(i)+'/'+str(round(pointnumber))+'] Computing the '+str(round(x[i],2))+ ' point:  ')

pickle.dump(array_of_computations,open( "computedpoints.pickle", "wb" ))