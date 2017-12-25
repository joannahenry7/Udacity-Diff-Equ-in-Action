# Udacity Problem (from Problem Set 4)
# PROBLEM 1
#
# There are two species of fish. We want to harvest the species 1, but we have a bycatch of species 2.
# Model logistic growth for both species with the constants and the initial values given below.
# Include harvesting at the harvest_rate given below.
# A fixed fraction p = 0...1 of this harvest will consist of species 2.
# Implement this using the Forward Euler Method.
# Using pencil and paper, determine the threshold value of p for fish 2 not to go extinct.
# Set the variable p to this threshold value when you submit the solution.

import numpy
import matplotlib.pyplot

def bycatch():
    maximum_growth_rate_1 = 0.5 # 1 / year
    carrying_capacity_1 = 2.0e6 # tons
    maximum_growth_rate_2 = 0.3 # 1 / year
    carrying_capacity_2 = 1.0e6 # tons
    harvest_rate = 0.8 * 2.5e5 # rate of catching both kinds of fish, tons / year

    p = 0.375 # fraction of bycatch, i.e. fish 2

    end_time = 100. # years
    h = 0.1 # years
    num_steps = int(end_time / h)
    times = h * numpy.array(range(num_steps + 1))

    fish_1 = numpy.zeros(num_steps + 1) # tons
    fish_1[0] = 1.3e6
    fish_2 = numpy.zeros(num_steps + 1) # tons
    fish_2[0] = 7.5e5

    for step in range(num_steps):
        fish_1_harvest = (1. - p) * harvest_rate
        fish_1_growth = maximum_growth_rate_1 * (1. - fish_1[step] / carrying_capacity_1) * fish_1[step] - fish_1_harvest
        fish_2_harvest = p * harvest_rate
        fish_2_growth = maximum_growth_rate_2 * (1. - fish_2[step] / carrying_capacity_2) * fish_2[step] - fish_2_harvest

        fish_1[step + 1] = fish_1[step] + h * fish_1_growth
        fish_2[step + 1] = fish_2[step] + h * fish_2_growth

        if fish_1[step + 1] < 0. or fish_2[step + 1] < 0.:
            break

    return times, fish_1, fish_2

times, fish_1, fish_2 = bycatch()

def plot_fish():
    fish_1_plot = matplotlib.pyplot.plot(times, fish_1, label='Fish 1')
    fish_2_plot = matplotlib.pyplot.plot(times, fish_2, label='Fish 2')
    matplotlib.pyplot.legend(('Fish 1', 'Fish 2'), loc='upper right')

    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Time in years')
    axes.set_ylabel('Amount of fish in tons')
    matplotlib.pyplot.xlim(xmin=0.)
    matplotlib.pyplot.ylim(ymin=0.)
    matplotlib.pyplot.show()

plot_fish()
