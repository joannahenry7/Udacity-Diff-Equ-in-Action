# Udacity problem (from Problem Set 6)
# PROBLEM 1
#
# Model heat conduction in a wire that we will pretend is made up of 100 segments.
# Show how the change in temperature of a given segment depends on the temperature
# of the segments to either side of it by filling in the array coefficients.  This
# is a matrix that can be multiplied by a vector containing every segment's
# temperature after one time step to yield a vector containing all of the initial
# temperatures.  Use numpy.linalg.solve(coefficients, temperatures_old) to compute
# the values of temperatures_new.  Then implement the implicit finite difference
# method to show how the temperature of each segment changes with time.

import numpy
import matplotlib.pyplot

ambient_temperature = 300. # K
flame_temperature = 1000. # K
thermal_diffusivity = 10. * 0.001 ** 2 # m2 / s
dx = 0.001 # m
size = 100 # grid units
positions = dx * numpy.arange(size) # m

h = 0.5 # s
end_time = 10.0 # s
num_steps = int(end_time / h)

def heat_conduction_implicit():
    temperatures_old = ambient_temperature * numpy.ones(size) # K
    for i in range(4 * size / 10, 5 * size / 10):
        temperatures_old[i] = flame_temperature
    temperatures_new = numpy.copy(temperatures_old) # K

    c = h * thermal_diffusivity / dx ** 2
    coefficients = numpy.zeros([size, size])

    for i in range(size):
        if i == 0:
            coefficients[i, i] = 1 + c
            coefficients[i, i + 1] = -c
        elif i == 99:
            coefficients[i, i] = 1 + c
            coefficients[i, i - 1] = -c
        else:
            coefficients[i, i] = 1 + 2 * c
            coefficients[i, i - 1] = -c
            coefficients[i, i + 1] = -c

    for step in range(num_steps):
        temperatures_new = numpy.linalg.solve(coefficients, temperatures_old)
        temperatures_new, temperatures_old = temperatures_old, temperatures_new

    return temperatures_old

temperatures = heat_conduction_implicit()

def heat_plot():
    matplotlib.pyplot.plot(positions, temperatures)
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Position in m')
    axes.set_ylabel('Temperature in K')
    matplotlib.pyplot.show()

heat_plot()
