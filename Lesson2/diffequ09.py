# Udacity quiz (from Lesson 2)
# Implement adaptive step size in the
# below function.

import math
import numpy
import matplotlib.pyplot


total_time = 12500 # s
g = 9.81 # m/s/s
earth_mass = 5.97e24 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

def acceleration(spaceship_position):
    vector_to_earth = -spaceship_position # earth located at origin
    d_ES = numpy.linalg.norm(vector_to_earth) # distance btw earth and spaceship
    return gravitational_constant * earth_mass / d_ES**3 * vector_to_earth

def orbit():
    x = numpy.zeros(2) # m
    v = numpy.zeros(2) # m/s
    x[0] = 15e6
    x[1] = 1e6
    v[0] = 2e3
    v[1] = 4e3
    matplotlib.pyplot.scatter(x[0], x[1], s = 4)

    current_time = 0. # s
    h = 100. # s
    h_new = h # s, will store the adaptive step size of the next step
    tolerance = 5e5 # m

    while current_time < total_time:
        acceleration0 = acceleration(x)
        xE = x + h * v
        vE = v + h * acceleration0
        xH = x + h * 0.5 * (v + vE)
        vH = v + h * 0.5 * (acceleration0 + acceleration(xE))
        x = xH
        v = vH

        # implement adaptive step size
        lte = numpy.linalg.norm(xE - xH) + total_time * numpy.linalg.norm(vE - vH) #local truncation error
        h_new = h * (tolerance / lte)**(0.5)

        matplotlib.pyplot.scatter(x[0], x[1], s = 1)
        current_time += h
        h = h_new
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.scatter(0., 0.)
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()
    return x, v

x, v = orbit()
