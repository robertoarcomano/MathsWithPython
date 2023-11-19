import numpy
import scipy.integrate as integrate

import numpy1
import pylab
from numpy1 import linalg as LA

def plot_sin():
    t = numpy.arange(-numpy.pi, numpy.pi, 0.01)
    s = numpy.sin(t)
    pylab.plot(t, s)
    pylab.xlabel('t')
    pylab.ylabel('sin(t)')
    pylab.title('Sin(t) graph')
    pylab.grid(True)
    pylab.show()


def plot_points():
    t = numpy.arange(-numpy.pi, numpy.pi, 0.01)
    s = numpy.sin(t)
    x = [0, 1, 1, 2]
    y = [0, 0, 1, 1]
    pylab.plot(x, y)
    pylab.grid(True)
    pylab.show()


def plot_line():
    t = numpy.arange(-2, 3, 0.01)
    straight_line = 2*t - 1
    quadratic = t*t
    sin = numpy.sin(t)
    pylab.xlim(-2, 2)
    pylab.ylim(-1, 2)
    pylab.plot(t, straight_line)
    pylab.plot(t, quadratic)
    # pylab.plot(t, sin)
    pylab.grid(True)
    pylab.show()


def calc_eigen():
    m = [
        [2, 1],
        [-1, 4]
    ]
    eigenvalues, eigenvectors = LA.eig(m)
    print(eigenvalues)
    print(eigenvectors)


def integrate_x_square():
    # 1. Integrate y=x*x from 0 to 1.
    output = integrate.quad(lambda x: x*x, 0, 1)
    # output equals to 1/3
    print("output: ", output[0])
    t = numpy.arange(-numpy.pi, numpy.pi, 0.01)
    s = numpy.square(t)
    pylab.plot(t, s)
    pylab.xlabel('t')
    pylab.ylabel('sin(t)')
    pylab.title('Sin(t) graph')
    pylab.grid(True)
    pylab.show()


# plot_sin()
# integrate_x_square()
plot_line()
calc_eigen()
