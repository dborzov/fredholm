# -*- coding: utf-8 -*-

import pylab, pickle

plotrange=[1.,1.3]
dimensions='2D'
L=16.

array=pickle.load(open( "computedpoints.pickle", "rb" ))

x=[]; y=[]
for each in array:
    x.append(each.Ee)
    y.append(each.limitvalue)
    print('x-point '+str(each.Ee)+' added ' +str(each.limitvalue))

pylab.semilogx(x,y,'bo')
pylab.xlabel('-E, energy parameter')
pylab.ylabel('G3')

"""
pylab.ylim([-1.,1.])
"""
try:
    pylab.xlim(plotrange)
    tick_number=10
    pylab.xticks([1.+float(i)*(plotrange[1]-plotrange[0])/float(tick_number) for i in xrange(0,tick_number)],[round(1.+float(i)*(plotrange[1]-plotrange[0])/float(tick_number),2) for i in xrange(0,tick_number)])
except:
    print('The range is undefined, taking the default one')

pylab.title('G_3, the beauteful')
pylab.savefig('plotus.pdf')