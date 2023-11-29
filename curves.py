import numpy as np
import matplotlib.pyplot as plot

x = np.linspace(-5, 5, 1000)
fns = np.array([
    ["exp", lambda t: np.exp(t)],
    ["log", lambda t: np.log(t)],
    ["linear", lambda t: t],
    ["quadratic", lambda t: t ** 2],
    ["cubic", lambda t: t ** 3],
    ["inverse", lambda t: 1/t],
])
for fn in fns:
    plot.plot(x, fn[1](x), label=fn[0])
plot.xlabel("x")
plot.figlegend()
plot.show()
