# Udacity quiz (from Lesson 7)
# QUIZ
#
# Compute the total energy of the chain, where the
# 2D positions of the nodes are given by the elements
# of the array x, then return it in the variable
# energy.

import sys
import math
import numpy
import matplotlib.pyplot

total_length = 2. # m
total_mass = 1. # kg
spring_constant = 50.0 # N / m
num_points = 20
g = 9.81 # m / s2
initial_energy=sys.float_info.max
numpy.random.seed(42)

rest_length = total_length / (num_points - 1) # m
mass_per_point = total_mass / num_points # kg


def perturb_chain(x):
    x = numpy.copy(x)
    index_to_change = numpy.random.random_integers(1, num_points - 2) # not the first, not the last
    x[index_to_change] += 0.1 * (numpy.random.rand(2) - numpy.array([0.5, 0.5]))
    return x

def chain_energy(x):
    energy = 0.
    for i in range(num_points):
        energy += mass_per_point * g * x[i, 1]
    for i in range(num_points - 1):
        length = numpy.linalg.norm(x[i] - x[i + 1])
        energy += 0.5 * spring_constant * (length - rest_length) ** 2
    return energy

def plot_evolution():
    x = total_length * numpy.random.rand(num_points, 2)
    x[0, 0] = 0.
    x[0, 1] = 0.
    x[-1, 0] = 1.3
    x[-1, 1] = 0.4
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Position x in m')
    axes.set_ylabel('Position y in m')
    energy = initial_energy
    for i in range(14001):
        perturbed_chain = perturb_chain(x)
        perturbed_energy = chain_energy(perturbed_chain)
        if perturbed_energy < energy:
            energy = perturbed_energy
            x = perturbed_chain
        if i % 2000 == 0:
            matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.show()

plot_evolution()
