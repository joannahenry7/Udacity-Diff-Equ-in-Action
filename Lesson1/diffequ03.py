# acceleration quiz from Udacity course Differential Equations in Action
#
# acceleration function returns the acceleration vector of the spacecraft.

import numpy

earth_mass = 5.97e24 # kg
moon_mass = 7.35e22 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

# The origin, or (0,0), is at the center of the earth
# moon_position and spaceship_position are both numpy arrays, and the
# returned value should also be a numpy array.
# numpy.linalg.norm function computes length of a vector

def acceleration(moon_position, spaceship_position):
    d_ES = numpy.linalg.norm(spaceship_position)
    d_MS = numpy.linalg.norm(moon_position - spaceship_position)
    a_E = gravitational_constant * earth_mass / d_ES**2 * (-spaceship_position / d_ES)
    a_M = gravitational_constant * moon_mass / d_MS**2 * ((moon_position - spaceship_position) / d_MS)
    a = a_E + a_M
    return a

moon_position = numpy.array([20, 30])
spaceship_position = numpy.array([5, -15])
print acceleration(moon_position, spaceship_position)
