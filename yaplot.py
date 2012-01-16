# -*- coding: utf-8 -*-

import equation
import pylab, pickle, equation

dimensions='2D'
L=16.

array=pickle.load(open( "computedpoints.pickle", "rb" ))

x=[]; y=[]
for each in array:
    x.append(each.Ee)
    y.append(each.limitvalue)
    print('x-point '+str(each.Ee)+' added ' +str(each.limitvalue))


pylab.semilogx(x,y,'o')
pylab.xlabel('-E, energy parameter')
pylab.ylabel('G3')

"""
pylab.ylim([-1.,1.])
"""
try:
    pylab.xlim([fromus,to])
except:
    print('The range is undefined, taking the default one')

pylab.title('G_3, the beauteful')
pylab.savefig('plotus.pdf')