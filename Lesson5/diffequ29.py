# Udacity quiz (from Lesson 5)
# 1. Initialize v and w so that the simulation
#    starts at a car speed of 120 km/h and with
#    no wheel slip.
#
# 2. Implement the Forward Euler Method for the
#    simulation.

import math
import numpy
import matplotlib.pyplot

h = 0.01 # s
mass_quarter_car = 250. # kg
mass_effective_wheel = 20. # kg
g = 9.81 # m / s2

end_time = 5. # s
num_steps = int(end_time / h)

w = numpy.zeros(num_steps + 1) # m / s
v = numpy.zeros(num_steps + 1) # m / s
x = numpy.zeros(num_steps + 1) # m
times = h * numpy.array(range(num_steps + 1))

def plot_me():
    axes_x = matplotlib.pyplot.subplot(411)
    axes_v = matplotlib.pyplot.subplot(412)
    axes_w = matplotlib.pyplot.subplot(413)
    axes_s = matplotlib.pyplot.subplot(414)

    def friction_coeff(slip):
        return 1.1 * (1. - math.exp(-20 * slip)) - 0.4 * slip

    def wheel_slip():
        b_values = numpy.arange(70., 190.1, 30.) # m / s2
        for b in b_values:
            x[0] = 0.
            v[0] = 120. * 1000 / 3600
            w[0] = 120. * 1000 / 3600

            for step in range(num_steps):
                if v[step] < 0.01: # Did we already come to a complete stop?
                    break
                s = max(0., 1. - w[step] / v[step]) # clamp the value at zero to reduce numerical instability

                x[step + 1] = x[step] + h * v[step]
                friction_force = friction_coeff(s) * mass_quarter_car * g
                v[step + 1] = v[step] + h * (-friction_force / mass_quarter_car)
                w[step + 1] = w[step] + h * (friction_force / mass_effective_wheel - b)

                w[step + 1] = max(0., w[step + 1]) # clamp the value at zero so the brake cannot decelerate the wheel so far as to spin in the wrong direction

            axes_x.plot(times[:step], x[:step])
            axes_v.plot(times[:step], v[:step])
            axes_w.plot(times[:step], w[:step])
            axes_s.plot(times[:step], 1. - w[:step] / v[:step])
            p = int((0.35 + 0.4 * (b - b_values[0]) / (b_values[-1] - b_values[0])) * num_steps)
            axes_x.annotate(b, (times[p], x[p]),
                                    xytext=(-30, -30), textcoords='offset points',
                                    arrowprops=dict(arrowstyle='-', connectionstyle='arc3, rad = 0.2', shrinkB=0.))
        return x, v, w

    axes_x.set_ylabel('Position\nin m', multialignment='center')
    axes_v.set_ylabel('Car velocity\nin m/s', multialignment='center')
    axes_w.set_ylabel('Wheel velocity\nin m/s', multialignment='center')
    axes_s.set_ylabel('Wheel\nslip', multialignment='center')
    axes_s.set_xlabel('Time in s')
    axes_s.set_ylim(0., 1.)

    return wheel_slip()

x, v, w = plot_me()
matplotlib.pyplot.show()
