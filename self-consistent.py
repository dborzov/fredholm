from numpy import log, pi
from scipy.optimize import brentq

def f(x, d=3.):
    return x - 2. *  pi/log(d**2 *x)

print brentq(lambda x:f(x,d=3.),1.01,10., xtol=1e-3)