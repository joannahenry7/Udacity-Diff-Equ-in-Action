# Udacity problem (from Problem Set 5)
# PROBLEM 2
#
# Implement the control algorithm for the hydraulic brake (see Section 14 and 15 of Unit 5).
# When the wheel slip gets larger than high_slip, start to decrease the pressure;
# when the wheel slip gets smaller than low_slip, start to increase the pressure.
# Increasing/decreasing the pressure leads to a rate of change of hydraulic_speed in the
# strength b of the brake (as measured in deceleration of the velocity of the rim of the
# wheel if there was no friction force from the road.)
# The strength of the brake must always lie between 0 and max_brake.

import math
import numpy
import matplotlib.pyplot

h = 0.001 # s
mass_quarter_car = 250. # kg
mass_effective_wheel = 20. # kg
g = 9.81 # m / s2
max_brake = 250. # m / s2
hydraulic_speed = 3300. # m / s3
low_slip = 0.17
high_slip = 0.23

end_time = 5. # s
num_steps = int(end_time / h)

def friction_coeff(slip):
    return 1.1 * (1. - math.exp(-20 * slip)) - 0.4 * slip

def hydraulic():
    w = numpy.zeros(num_steps + 1) # m / s
    v = numpy.zeros(num_steps + 1) # m / s
    x = numpy.zeros(num_steps + 1) # m
    b = numpy.zeros(num_steps + 1) # m / s2
    times = h * numpy.array(range(num_steps + 1))

    axes_x = matplotlib.pyplot.subplot(511)
    axes_v = matplotlib.pyplot.subplot(512)
    axes_w = matplotlib.pyplot.subplot(513)
    axes_s = matplotlib.pyplot.subplot(514)
    axes_b = matplotlib.pyplot.subplot(515)

    x[0] = 0.
    v[0] = 120. * 1000. / 3600. # 120 km / h
    w[0] = v[0]
    b[0] = max_brake # initially the driver steps on the brake as hard as possible

    brake_change = 0.

    for step in range(num_steps):
        if v[step] < 0.01:
            break
        s = max(0., 1. - w[step] / v[step])
        force = friction_coeff(s) * mass_quarter_car * g
        v[step + 1] = v[step] - h * force / mass_quarter_car
        x[step + 1] = x[step] + h * v[step]
        w[step + 1] = w[step] + h * (force / mass_effective_wheel - b[step])
        w[step + 1] = max(0., w[step + 1])

        if s > high_slip:
            brake_change = -1.
        elif s < low_slip:
            brake_change = 1.

        b[step + 1] = b[step] + brake_change * h * hydraulic_speed
        b[step + 1] = max(0., min(b[step + 1], max_brake))

    axes_x.plot(times[:step:10], x[:step:10])
    axes_v.plot(times[:step:10], v[:step:10])
    axes_w.plot(times[:step:10], w[:step:10])
    axes_s.plot(times[:step:10], 1. - w[:step:10] / v[:step:10])
    axes_b.plot(times[:step:10], b[:step:10])
    axes_x.set_ylabel('Position\nin m', multialignment='center')
    axes_v.set_ylabel('Car velocity\n in m/s', multialignment='center')
    axes_w.set_ylabel('Wheel velocity\n in m/s', multialignment='center')
    axes_s.set_ylabel('Wheel\nslip', multialignment='center')
    axes_s.set_ylim(0., 1.)
    axes_b.set_ylabel('Brake strength\nin m/s$^2$', multialignment='center')
    axes_b.set_ylim(0., max_brake)
    axes_b.set_xlabel('Time in s')
    matplotlib.pyplot.show()

    return w

hydraulic()
