from numpy import log, pi, arange, exp
from scipy.optimize import brentq
import matplotlib.pyplot as plot
from matplotlib import rc
import equation

def diagram_sum(x, d):
    return 4.*pi/log(d**2 *2.*x)

def diagram_sum_3body(x, d):
    point=equation.equation(3.*x,'2D',20.,0.1,d)
    point.solve()
    g3=point.g3
    del point
    return 4.*pi/log(d**2 *2.*x) + g3


drange=arange(0.6,5.,0.05)
xx=[d for d in drange]
ee=[1/d**2 for d in drange]
yy=[brentq(lambda mu:mu - diagram_sum(mu,d),(0.5+0.01)/(d**2),0.5/d**2 *exp(8 * pi * d**2), xtol=1e-3) for d in drange]

drange=arange(0.6,5.6,1.0)
zx=[d for d in drange]
ze=[1/d**2 for d in drange]
zz=[brentq(lambda mu:mu - diagram_sum_3body(mu,d),(1+0.01)/(2.*d**2),0.5/d**2 *exp(8 * pi * d**2), xtol=1e-2) for d in drange]

drange=arange(0.7,1.5,0.1)
wx=[d for d in drange]
we=[1/d**2 for d in drange]
wz=[brentq(lambda mu:mu - diagram_sum_3body(mu,d),(1+0.01)/(2.*d**2),0.5/d**2 *exp(8 * pi * d**2), xtol=1e-2) for d in drange]

drange=arange(0.6,0.7,0.025)
fx=[d for d in drange]
fe=[1/d**2 for d in drange]
fz=[brentq(lambda mu:mu - diagram_sum_3body(mu,d),(1+0.01)/(2.*d**2),0.5/d**2 *exp(8 * pi * d**2), xtol=1e-2) for d in drange]


plot.plot(xx,yy)
plot.plot(zx,zz,'o')
plot.plot(wx,wz,'o')
plot.plot(fx,fz,'o')
plot.xlabel('d, bound state size parameter')
plot.ylabel(r'$\mu$, self-consistent potential')
plot.savefig('results/potential_self-consistent.pdf')
plot.close()

plot.plot(ee,yy)
plot.plot(ze,zz,'o')
plot.plot(we,wz,'o')
plot.plot(fe,fz,'o')
rc('text', usetex=True)
plot.xlabel(r'$\frac{1}{d^2}$, bound state energy')
plot.ylabel(r'$\mu$, self-consistent potential')
plot.savefig('results/potential_energy_parameter.pdf')

