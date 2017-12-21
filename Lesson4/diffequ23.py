# Udacity quiz (from Lesson 4)
# Complete the forward_euler() function for the
# differential equation and set the variable
# end_time to where the solution completely
# explodes! Give two decimal places of precision.

import numpy
import matplotlib.pyplot

end_time = 0.64 #
h = 0.0001
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))

x = numpy.zeros(num_steps + 1)
x[0] = 3.

def forward_euler():
    for step in range(num_steps):
        x[step + 1] = x[step] + h * (x[step]**2 + 1) / 2

    return x
x = forward_euler()

def plot_me():
    matplotlib.pyplot.plot(times, x)
    matplotlib.pyplot.show()

plot_me()
