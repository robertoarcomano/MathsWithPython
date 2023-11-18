import numpy as np
import matplotlib.pyplot as plot
from matplotlib import style
import seaborn as sb

database = sb.load_dataset("diamonds")
tips = sb.load_dataset("tips")
flights = sb.load_dataset("flights")
sb.displot(database['carat'])
#
# n = 10
# levels = np.random.rand(n)*100
# ylevels = np.intc(np.random.rand(n)*10000)
# print(np.intc(ylevels))
# final = np.array(1)
# for i in range(n):
#     final = np.append(final, np.linspace(levels[i],levels[i],ylevels[i]))
#
#
#
# sb.displot(final)
#
sb.jointplot(x="tip", y="total_bill", data=tips)
sb.catplot(x="month", y="passengers", data=flights, kind="box")


graph1 = sb.FacetGrid(tips, col="sex", hue="smoker")
graph1.map(plot.scatter, "total_bill", "tip")

plot.show()