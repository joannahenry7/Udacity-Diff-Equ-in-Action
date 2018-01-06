# Udacity quiz (from Lesson 7)
# QUIZ
#
# Implement the Forward Euler Method below
# for the Lorenz System. Return an array
# with the absolute values of the differences
# of the x values in the variable called distance.

import numpy
import matplotlib.pyplot

def lorenz():
    h = 0.001 # s
    end_time = 50. # s
    num_steps = int(end_time / h)

    sigma = 10.
    beta = 8. / 3.
    rho = 28.

    x = numpy.zeros([num_steps + 1, 2])
    y = numpy.zeros([num_steps + 1, 2])
    z = numpy.zeros([num_steps + 1, 2])
    times = h * numpy.array(range(num_steps + 1))

    x[0, 0] = 0.
    y[0, 0] = 0.3
    z[0, 0] = 40.

    x[0, 1] = 0.
    y[0, 1] = 0.300000000000001
    z[0, 1] = 40.

    for step in range(num_steps):
        x[step + 1] = x[step] + h * sigma * (y[step] - x[step])
        y[step + 1] = y[step] + h * (x[step] * (rho - z[step]) - y[step])
        z[step + 1] = z[step] + h * (x[step] * y[step] - beta * z[step])

    distance = numpy.fabs(x[:, 0] - x[:, 1])

    return times, distance, x, y, z

times, distance, x, y, z = lorenz()

def plot_me():
    axes = matplotlib.pyplot.gca()
    numpy.ma.masked_less(distance, 1e-20)
    matplotlib.pyplot.semilogy(times, distance)
    axes.set_xlabel('t')
    axes.set_ylabel('Distance of x values')
    # Uncomment these four lines and comment the four lines abve to see the Lorenz Butterfly
    #matplotlib.pyplot.plot(x[:, 0], z[:, 0])
    #matplotlib.pyplot.plot(x[:, 1], z[:, 1])
    #axes.set_xlabel('x')
    #axes.set_ylabel('z')
    matplotlib.pyplot.show()

plot_me()
