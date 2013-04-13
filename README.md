===========
Fredholm.py
===========

Fredholm python package allows you to solve integral equations numerically. 

See [dborzov.github.io/fredholm](http://dborzov.github.io/fredholm/) for more details.

Fredholm's integral equation of the first order can be written in the following way::
```
    int K(y,x) phi(x) dx = f(y)
```
To use it, define the Fredholm's integral kernel of the equation and the nonhomogenious term::
```
    #!/usr/bin/env python

    import Fredholm
    Fredholm.Kernel = lambda x,y: 1/(x**2 + y**2)
    Fredholm.f = lambda x: 1.
    Fredholm.range.low, Fredholm.range.high = 0. , 100.
    Fredholm.solve()
    print Fredholm.solution(2.) 
```

Fredholm.solution yeilds the NumPy interpolation function that is defined in the defined range.

Features
=========
Here are some reasons to know and love Fredholm:

1. The adaptive integration mesh

2. Can take care of principal value integrals
