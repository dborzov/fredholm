import equation, numpy
from scipy.integrate import quad
import matplotlib.pyplot as pyplot
from scipy.interpolate import interp1d as interpolate

def make_one_iterated():
    equation.get_some_point()
    equation.parameters_printed()
    print equation.G3,'+/-',equation.error_margin()
#    equation.rescale(3.)
#    equation.parameters_printed()
#    print equation.G3,'+/-',equation.error_margin()
    for i in range(6):
        previous_value=equation.G3
        print 'Iterate #', i
        equation.iterate()
        print equation.G3,' increment ',equation.G3-previous_value
    equation.dump_result()


for k in range(7):
    make_one_iterated()
