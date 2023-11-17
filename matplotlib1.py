import numpy as np
import matplotlib.pyplot as plot
from matplotlib import style

# style.use("bmh")
print(style.available)
x=np.array(np.linspace(0,100,100))
y=x*x
plot.plot(x,y)
plot.title("Quadratic function")
plot.xlabel("Time")
plot.ylabel("x square")

x1=[0, 100]
y1=[0, 10000]
plot.plot(x1,y1)


x2=[0, 62, 102]
y2=[0, 3604, 10004]

x3=[0, 42, 82]
y3=[0, 4000, 8000]

plot.bar(x2, y2, width=5)
plot.bar(x3, y3, width=5)

plot.show()

