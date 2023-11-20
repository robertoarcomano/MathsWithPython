import numpy as np
import matplotlib.pyplot as plot
import matplotlib.style as style


def p(x):
    return 1 - 14 * x + 16 * x ** 2


style.use("bmh")
dots = np.array([
    [0., 1.],
    [0.5, -2.],
    [1., 3.]
])
plot.scatter(dots[:, 0], dots[:, 1])
x = np.linspace(0, 1, 100)
plot.plot(x, p(x))
plot.show()
