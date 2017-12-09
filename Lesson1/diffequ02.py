# Eulerian Free Fall quiz from Udacity course Differential Equations in Action
# uses Euler's method to plot position and velocity of free falling object
# at time t
# beginning at position x = 0 and velocity v = 0 with acceleration g = -9.81 m/s/s
# (acceleration, velocity and position are all negative because object is
# falling downward)
# position = (initial position) + velocity * time
# velocity = (initial velocity) + acceleration * time

import numpy
import matplotlib.pyplot

def forward_euler():
    h = 0.1 # step size, in seconds
    g = -9.81 # m/s/s

    num_steps = 50

    # use 51 points so initial point can be 0 and we plot 50 additional points
    t = numpy.zeros(num_steps + 1)
    x = numpy.zeros(num_steps + 1)
    v = numpy.zeros(num_steps + 1)

    for step in range(num_steps):
        t[step + 1] = t[step] + h
        x[step + 1] = x[step] + h * v[step]
        v[step + 1] = v[step] + h * g
    return t, x, v

t, x, v = forward_euler()

def plot_me():
    axes_height = matplotlib.pyplot.subplot(211)
    matplotlib.pyplot.plot(t, x)
    axes_velocity = matplotlib.pyplot.subplot(212)
    matplotlib.pyplot.plot(t, v)
    axes_height.set_ylabel('Height in m')
    axes_velocity.set_ylabel('Velocity in m/s')
    axes_velocity.set_xlabel('Time in s')
    matplotlib.pyplot.show()

plot_me()
