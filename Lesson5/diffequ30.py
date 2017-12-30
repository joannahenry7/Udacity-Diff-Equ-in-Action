# Udacity quiz (from Lesson 5)
# Implement the driver pumping the brakes in the
# wheel_slip function below. The driver should
# slam on the brake from t = 0.0 s to t = 0.7 s,
# let go, then slam the brakes on again from
# t = 1.0 s to t = 1.7 s, and so on.

import math
import numpy
import matplotlib.pyplot

h = 0.01 # s
mass_quarter_car = 250. # kg
mass_effective_wheel = 20. # kg
g = 9.81 # m / s2

end_time = 5. # s
num_steps = int(end_time / h)

w = numpy.zeros(num_steps + 1) # 1 / s
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
        b_values = [130., 200.] # m / s2
        for b in b_values:
            is_pumping = (b > 170.)
            x[0] = 0.
            v[0] = 120. * 1000. / 3600. # 120 km / h
            w[0] = v[0]

            for step in range(num_steps):
                if v[step] < 0.01:
                    break

                s = max(0., 1. - w[step] / v[step])
                force = friction_coeff(s) * mass_quarter_car * g
                v[step + 1] = v[step] - h * force / mass_quarter_car
                x[step + 1] = x[step] + h * v[step]

                on_off_factor = 1.0
                if is_pumping:
                    if (h * step) % 1. >= 0.7:
                        on_off_factor = 0.
                w[step + 1] = w[step] + h * (force / mass_effective_wheel - b * on_off_factor)
                w[step + 1] = max(0., w[step + 1])

            axes_x.plot(times[:step], x[:step])
            axes_v.plot(times[:step], v[:step])
            axes_w.plot(times[:step], w[:step])
            axes_s.plot(times[:step], 1. - w[:step] / v[:step])
            p = int((0.4 + 0.4 * (b - b_values[0]) / (b_values[-1] - b_values[0])) * num_steps)
            axes_x.annotate(is_pumping, (times[p], x[p]),
                                   xytext=(-30, -30), textcoords='offset points',
                                   arrowprops=dict(arrowstyle='-', connectionstyle='arc3, rad=0.2', shrinkB = 0.))

        return x, v, w

    axes_x.set_ylabel('Position\nin m', multialignment='center')
    axes_v.set_ylabel('Car velocity\nin m', multialignment='center')
    axes_w.set_ylabel('Wheel velocity\nin m', multialignment='center')
    axes_s.set_ylabel('Wheel\n slip', multialignment='center')
    axes_s.set_xlabel('Time in s')
    axes_s.set_ylim(0., 1.)

    return wheel_slip()

plot_me()
matplotlib.pyplot.show()
