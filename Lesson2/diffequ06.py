# Udacity quiz from Differential Equations in Action
# from Problem Set 1
# Using Forward Euler Method, plot the trajectory of a spacecraft with
# given initial position and velocity

import numpy
import matplotlib.pyplot


h = 0.1 # s
earth_mass = 5.97e24 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

def acceleration(spaceship_position):
    d_ES = numpy.linalg.norm(spaceship_position)
    a = gravitational_constant * earth_mass / d_ES**3 * -spaceship_position
    return a

def ship_trajectory():
    num_steps = 130000
    x = numpy.zeros([num_steps + 1, 2]) # m
    v = numpy.zeros([num_steps + 1, 2]) # m/s

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3

    for i in range(num_steps):
        a = acceleration(x[i])
        x[i + 1] = x[i] + h * v[i]
        v[i + 1] = v[i] + h * a

    return x, v

x, v = ship_trajectory()

def plot_me():
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.scatter(0, 0)
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()

plot_me()
