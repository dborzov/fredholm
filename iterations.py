from equation import *
from scipy.integrate import quad


def better(p):
    psi=interpolate(psi_range, solution, kind='cubic')
    x=quad(lambda x: K_Green(x,p) *psi(x) ,0.,L) + right_side(p)

def
