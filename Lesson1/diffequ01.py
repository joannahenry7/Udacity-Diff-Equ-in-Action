import math, numpy, matplotlib.pyplot


# simple plot of sin and cos to try out matplotlib
def sin_cos():
    num_points = 50

    x = numpy.zeros(num_points)
    sin_x = numpy.zeros(num_points)
    cos_x = numpy.zeros(num_points)

    for i in range(num_points):
        x[i] = (2 * math.pi / (num_points - 1)) * i
        sin_x[i] = math.sin(x[i])
        cos_x[i] = math.cos(x[i])
    return x, sin_x, cos_x

x, sin_x, cos_x = sin_cos()


def plot_me():
    matplotlib.pyplot.plot(x, sin_x)
    matplotlib.pyplot.plot(x, cos_x)
    matplotlib.pyplot.show()
plot_me()
