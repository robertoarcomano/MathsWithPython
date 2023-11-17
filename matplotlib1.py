import numpy as np
import matplotlib.pyplot as plot
from matplotlib import style

style.use("bmh")
print(style.available)
x=np.array(np.linspace(0,100,100))
y=x*x
plot.plot(x,y)
plot.title("Quadratic function")
plot.xlabel("Time")
plot.ylabel("x square")
plot.show()
