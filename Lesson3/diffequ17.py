# Udacity quiz (from Leson 3)
# Implement Backward Euler, then set the step size h to 5
# (Backward Euler is better for stiff equations than Forward Euler)

import math
import numpy
import matplotlib.pyplot


h = 5. # days
transmission_coeff = 5e-9 # 1 / day person
latency_time = 1. # days
infectious_time = 5. # days

end_time = 60. # days
num_steps = int(end_time / h)

times = h * numpy.array(range(num_steps + 1))

def backward_euler():

    s = numpy.zeros(num_steps + 1)
    e = numpy.zeros(num_steps + 1)
    i = numpy.zeros(num_steps + 1)
    r = numpy.zeros(num_steps + 1)

    s[0] = 1e8 - 1e6 - 1e5
    e[0] = 0.
    i[0] = 1e5
    r[0] = 1e6

    for step in range(num_steps):
        p = ((1.0 + h / infectious_time) / (h * transmission_coeff) + i[step]) / (h / latency_time) - (s[step] + e[step]) / (1.0 + h / latency_time)
        q = -((1.0 + h / infectious_time) / (h * transmission_coeff) * e[step] + (s[step] + e[step]) * i[step]) / ((1.0 + h / latency_time) * (h / latency_time))
        e[step + 1] = -0.5 * p + math.sqrt(0.25 * p * p - q)
        i[step + 1] = (i[step] + h / latency_time * e[step + 1]) / (1. + h / infectious_time)
        s[step + 1] = s[step] / (1. + h * transmission_coeff * i[step + 1])
        r[step + 1] = r[step] + h / infectious_time * i[step + 1]

    return s, e, i, r

s, e, i, r = backward_euler()

def plot_me():
    s_plot = matplotlib.pyplot.plot(times, s, label='S')
    e_plot = matplotlib.pyplot.plot(times, e, label='E')
    i_plot = matplotlib.pyplot.plot(times, i, label='I')
    r_plot = matplotlib.pyplot.plot(times, r, label='R')
    matplotlib.pyplot.legend(('S', 'E', 'I', 'R'), loc='upper right')

    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Time in days')
    axes.set_ylabel('Numberr of persons')
    matplotlib.pyplot.xlim(xmin=0.)
    matplotlib.pyplot.ylim(ymin=0.)
    matplotlib.pyplot.show()

plot_me()
