from numpy.matlib import zeros
import numpy.linalg as lina

def getenergy(V):
    M=100
    Abba=zeros((M+1,M+1),float)
    for i in range (0,M+1):
        for j in range (0,M+1):
            aus=0
            if i==j:
                aus=1
            Abba[i,j]=aus*(i/float(M))**2 + V/float(M)

    spectrum,wavefunctions=lina.eig(Abba)
    return min(spectrum)





