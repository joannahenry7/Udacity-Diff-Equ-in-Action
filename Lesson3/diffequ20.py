# Udacity problem (from Problem Set 3)
# PROBLEM 3
#
# Modify the prevent_malaria function below to
# implement the Forward Euler Method.
#
# At 100 days, mosquito nets are
# introduced that reduce the probability of
# bites by bite_reduction_by_net.
#
# Be sure to include this reduction
# in your model.
#
# Please note that the mosquito population remains
# constant because its birth rate is equal to
# its mortality rate.

import numpy
import matplotlib.pyplot

h = 0.1 # days
end_time = 400. # days
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))

total_humans = 1e8
total_mosquitoes = 1e10

def prevent_malaria():
    bites_per_day_and_mosquito = 0.1 # humans / (day * mosquito)
    transmission_probability_mosquito_to_human = 0.3 # probability
    transmission_probability_human_to_mosquito = 0.5 # probability
    human_recovery_time = 70.0 # days
    mosquito_lifetime = 10.0 # days
    bite_reduction_by_net = 0.9 # probability

    infected_humans = numpy.zeros(num_steps + 1)
    infected_mosquitoes = numpy.zeros(num_steps + 1)

    infected_humans[0] = 0.
    infected_mosquitoes[0] = 1e6


    # differential equations were determined by:
    # increase of infected humans = bites per day * chance of mosquito being infected * chance of human being susceptible * chance of transmission
    # increase of infected mosqu = bites per day * chance of mosqu being susceptible * chance of human being infected * chance of transmission
    # decrease of infected humans = 1 / recovery time * number of infected humans
    # decrease of infected mosqu = 1 / mosqu lifetime * number of infected mosqu
    #
    # final terms for increase of infected humans/mosquitoes:
    # humans: bites_per_day_and_mosquito * infected_mosquitoes[step] * (total_humans - infected_humans[step]) / total_humans * transmission_probability_mosquito_to_human
    # mosqu: bites_per_day_and_mosquito * (total_mosquitoes - infected_mosquitoes[step]) * infected_humans[step] / total_humans * transmission_probability_human_to_mosquito
    # below are the constants from these equations (transmission coefficients)
    human_transm_coeff = bites_per_day_and_mosquito / total_humans * transmission_probability_mosquito_to_human
    mosqu_transm_coeff = bites_per_day_and_mosquito / total_humans * transmission_probability_human_to_mosquito
    use_nets = False

    for step in range(num_steps):
        if step * h >= 100. and not use_nets:
            human_transm_coeff *= (1 - bite_reduction_by_net)
            mosqu_transm_coeff *= (1 - bite_reduction_by_net)
            use_nets = True

        s_humans = total_humans - infected_humans[step] # susceptible humans
        s_mosqu = total_mosquitoes - infected_mosquitoes[step] # susceptible mosquites

        # differential equations for infected humans and infected mosquitoes respectively
        ih_dot = human_transm_coeff * infected_mosquitoes[step] * s_humans - 1. / human_recovery_time * infected_humans[step]
        im_dot = mosqu_transm_coeff * infected_humans[step] * s_mosqu - 1. / mosquito_lifetime * infected_mosquitoes[step]

        # Forward Euler's method
        infected_humans[step + 1] = infected_humans[step] + h * ih_dot
        infected_mosquitoes[step + 1] = infected_mosquitoes[step] + h * im_dot

    return infected_humans, infected_mosquitoes

infected_humans, infected_mosquitoes = prevent_malaria()

def plot_me():
    humans_plot = matplotlib.pyplot.plot(times, infected_humans / total_humans, label='Humans')
    mosquitoes_plot = matplotlib.pyplot.plot(times, infected_mosquitoes / total_mosquitoes, label='Mosquitoes')
    matplotlib.pyplot.legend(('Humans', 'Mosquitoes'), loc='upper right')

    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Time in days')
    axes.set_ylabel('Fraction infected')
    matplotlib.pyplot.xlim(xmin=0.)
    matplotlib.pyplot.ylim(ymin=0.)
    matplotlib.pyplot.show()

plot_me()
