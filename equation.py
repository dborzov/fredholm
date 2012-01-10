from pylab import arange


from numpy.matlib import zeros
import numpy, math
import numpy.linalg as lina

def K(q,p, Ee, dimensions='3D'):
        ratio=1./numpy.sqrt((p**2 + q**2 + p*q + Ee)*(p**2 + q**2 - p*q + Ee))
        return ratio*4.*q/math.log(0.75*q**2+ Ee)

def dlta(x,y):
    aus=0.
    if x==y:
        aus=1.
    return aus

class equation(object):
    def __init__(self,Ee, dimensions='3D', L=10. , d=0.05):
        self.L=L
        self.d=d
        self.dimensions=dimensions
        nn=int(self.L/self.d)
        self.x=map(lambda a:{'ps':float(a)*self.d + self.d/2.,'in':a}, range(0,nn))
        self.Ee=Ee
        self.b=map(self.ff,self.x)

        self.Abba=zeros((len(self.x),len(self.x)),float)
        for p,q in ([a,b] for a in self.x for b in self.x):
                self.Abba[p['in'],q['in']]=dlta(p['in'],q['in']) - self.d*K( q['ps'],p['ps'],Ee, dimensions)

    def ff(self, p):
        a=-sum([self.d*K(q['ps'],p['ps'],self.Ee, self.dimensions)/(q['ps']**2 + self.Ee) for q in self.x])
        return a

    def solve(self):
        self.solution=lina.solve(self.Abba, self.b)
        return self.solution

    def lowlimit(self):
        return self.solution[0]

print 'Whoah, someone run the equation file!'


