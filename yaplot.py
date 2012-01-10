import equation
from pylab import *

dimensions='2D'
L=16.
to=1.15
stepus=0.01
fromus=1.1
pointnumber=40.


xlog = arange(math.log(fromus), math.log(to), math.log(to/fromus)/pointnumber)
x=[math.exp(each) for each in xlog]
y=zeros((len(xlog)),float)

for i in range(0,len(x)):
    dot=equation.equation(x[i], dimensions, L)
    dot.solve()
    y[i]=dot.lowlimit()*x[i]
    print ('['+str(i)+'/'+str(round(pointnumber))+'] Computing the '+str(round(x[i],2))+ ' point:  '+ str(round(y[i],2)))


last=y[0]; bnds=[fromus-stepus];
for i in range(1,len(y)):
    if abs(y[i]-last)>5. and (last>0.) and (y[i]<0.):
        bnds.append(round((x[i]+x[i-1])/2.,6))
        print('is it a pole or do my eyes decieve me? ', x[i])
    last=y[i]
bnds.append(to)


semilogx(x,y,'o')
if len(bnds)!=0:
    stem(bnds,[50. for whatever in bnds])
xlabel('-E, energy parameter')
ylabel('G3')
ylim([-1000.,1000.])
xlim([fromus-stepus,to])
xticks(arange(fromus,to,10*stepus),[round(each,2) for each in arange(fromus,to,10*stepus)])
title('bound state positions '+str(bnds[1:len(bnds)-1]))
savefig('number1.pdf')
