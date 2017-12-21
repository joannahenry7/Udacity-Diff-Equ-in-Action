# Udacity quiz (from Lesson 4)
# Modify the harvest function below to
# demonstrate ramping up the rate at
# which fish are harvested.

import numpy
import matplotlib.pyplot

maximum_growth_rate = 0.5 # 1 / year
carrying_capacity = 2e6 # tons
maximum_harvest_rate = 0.8 * 2.5e5 # tons / year
ramp_start = 4. # years
ramp_end = 6. # years

end_time = 10. # years
h = 0.1 # years
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))

def harvest():
    fish = numpy.zeros(num_steps + 1) # tons
    fish[0] = 2e5

    is_extinct = False
    for step in range(num_steps):
        current_time = step * h
        if current_time >= ramp_end:
            harvest_rate = maximum_harvest_rate
        elif current_time >= ramp_start:
            harvest_rate = current_time * maximum_harvest_rate / 2. - 4e5
        else:
            harvest_rate = 0.

        if is_extinct:
            fish_next_step = 0.
        else:
            fish_next_step = fish[step] + h * (maximum_growth_rate * (1. - fish[step] / carrying_capacity) * fish[step] - harvest_rate)
            if fish_next_step <= 0.:
                is_extinct = True
                fish_next_step = 0.
        fish[step + 1] = fish_next_step

    return fish
fish = harvest()

def plot_me():
    matplotlib.pyplot.plot(times, fish)
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Time in years')
    axes.set_ylabel('Amount of fish in tons')
    matplotlib.pyplot.show()

plot_me()
