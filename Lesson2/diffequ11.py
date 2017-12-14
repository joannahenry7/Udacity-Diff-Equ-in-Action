# Udacity quiz (from Lesson 2)
# Implement the Symplectic Euler Method

import numpy
import matplotlib.pyplot


h = 5.0 # s
earth_mass = 5.97e24 # kg
spacecraft_mass = 30000. # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position # earth located at origin
    d_ES = numpy.linalg.norm(vector_to_earth) # distance from earth to spaceship
    return gravitational_constant * earth_mass / d_ES**3 * vector_to_earth

def symplectic_euler():
    num_steps = 20000
    x = numpy.zeros([num_steps + 1, 2]) # m
    v = numpy.zeros([num_steps + 1, 2]) # m / s
    energy = numpy.zeros(num_steps + 1) # J = kg m2 / s2

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3

    # implement symplectic method
    for step in range(num_steps):
        x[step + 1] = x[step] + h * v[step]
        v[step + 1] = v[step] + h * acceleration(x[step + 1])

    for step in range(num_steps + 1):
        velocity = numpy.linalg.norm(v[step])
        distance = numpy.linalg.norm(x[step])
        kinetic_energy = 0.5 * spacecraft_mass * velocity**2
        potential_energy = - gravitational_constant * earth_mass * spacecraft_mass / distance
        energy[step] = kinetic_energy + potential_energy

    return x, energy

x, energy = symplectic_euler()

def plot_me():
    axes_positions = matplotlib.pyplot.subplot(211)
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.scatter(0, 0)
    matplotlib.pyplot.axis('equal')
    axes_positions.set_xlabel('Longitudinal position in m')
    axes_positions.set_ylabel('Lateral position in m')
    axes_energy = matplotlib.pyplot.subplot(212)
    matplotlib.pyplot.plot(energy)
    axes_energy.set_xlabel('Step number')
    axes_energy.set_ylabel('Energy in J') # 1 Joule = 1 N m = 1 kg m2 / s2
    matplotlib.pyplot.show()

plot_me()
