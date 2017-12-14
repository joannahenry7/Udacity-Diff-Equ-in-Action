# Udacity quiz from Differential Equations in Action
# from Problem set 1
# Model one revolution of moon around earth, assuming orbit is circular

import math
import numpy
import matplotlib.pyplot


moon_distance = 384e6 # m

def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])

    for step in range(num_steps + 1):
        angle = step * 2 * math.pi / num_steps # radians
        x[step, 0] = moon_distance * math.cos(angle)
        x[step, 1] = moon_distance * math.sin(angle)

    return x

x = orbit()

def plot_me():
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()

plot_me()
