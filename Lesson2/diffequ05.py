# Udacity quiz from Differential Equations in Action
# from Problem Set 1
# Using Forward Euler Method, model ballistic trajectory of several particles
# each starting at (0,0) given initial speed in the direction specified by angle

import math
import numpy
import matplotlib.pyplot


h = 0.1 # s
g = 9.81 # m/s/s
acceleration = numpy.array([0., -g])
initial_speed = 20. # m/s

def trajectory():
    angles = numpy.linspace(20., 70., 6)

    num_steps = 30
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2])

    for angle in angles:
        rad = angle * math.pi / 180.
        v[0, 0] = initial_speed * math.cos(rad)
        v[0, 1] = initial_speed * math.sin(rad)

        for i in range(num_steps):
            n = i + 1
            x[n] = x[i] + h * v[i]
            v[n] = v[i] + h * acceleration

        matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Horizontal position in m')
    axes.set_ylabel('Vertical position in m')
    matplotlib.pyplot.show()
    return x, v

trajectory()
