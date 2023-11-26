import numpy as np
import matplotlib.pyplot as plot
from matplotlib import style


def parabolic(x, y):
    return x**2 + y**2


def sigmoid_1d(x):
    return 1/1+np.exp(-x)


def sigmoid_2d(x, y):
    return sigmoid_1d(x) + sigmoid_1d(y)


def hyperbolic(x, y):
    return 1/x + 1/y


def sin_on(x, y):
    return np.sin(x)/x + np.sin(x)/y


style.use("bmh")
x = np.array(np.linspace(-10,10,30))
y = x
x, y = np.meshgrid(x, y)

fig, axs = plot.subplots(
    2, 2, figsize=(8, 12), subplot_kw={'projection': '3d'})
axs[0, 0].plot_surface(x, y, parabolic(x, y), cmap='autumn', cstride=2, rstride=2)
axs[0, 1].plot_surface(x, y, sigmoid_2d(x, y), cmap='autumn', cstride=2, rstride=2)
axs[1, 0].plot_surface(x, y, hyperbolic(x, y), cmap='autumn', cstride=2, rstride=2)
axs[1, 1].plot_surface(x, y, sin_on(x, y), cmap='autumn', cstride=2, rstride=2)
plot.show()

