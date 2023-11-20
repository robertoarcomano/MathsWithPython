import numpy as np
import matplotlib.pyplot as plot

n = 20
delta = n / 2
x = np.linspace(1, n, n)
print(x)
y = np.random.rand(n)*delta - delta/2 + x

func1 = np.polyfit(x, y, 1)
print(x, func1)
plot.plot(x, y, '.')
plot.plot(x, np.polyval(func1, x), 'r-')
plot.show()
