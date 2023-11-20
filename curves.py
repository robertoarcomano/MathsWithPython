import numpy as np
import matplotlib.pyplot as plot

x = np.linspace(0, 5, 100)
y1 = np.exp(x)
y2 = x
y3 = x ** 2
y4 = x ** 3
plot.plot(x, y1, label="exp")
plot.plot(x, y2, label="linear")
plot.plot(x, y3, label="quadratric")
plot.plot(x, y4, label="cubic")
plot.xlabel("x")
plot.figlegend()
plot.show()
