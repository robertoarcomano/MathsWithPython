import numpy as np
import matplotlib.pyplot as plot

data = np.array([
    [0, 0],
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 5],
    [5, 6]
])
x = data[:, 0]
y = data[:, 1]
print(x)
e_x = np.mean(x)
e_y = np.mean(y)
var_x = np.var(x)
var_y = np.var(y)
e_xy = np.mean(x * y)
print("E[x]:", e_x)
print("E[y]:", e_y)
print("Var[x]:", var_x)
print("Var[y]:", var_y)
print("E[xy]:", e_xy)
print("E[xy]-E[x]E[y]:", e_xy - e_x * e_y)
covar1 = np.mean((x - e_x) * (y - e_y))
covar2 = e_xy - e_x * e_y
covar3 = np.cov(x, y, bias=True)
b = covar1 / var_x
a = e_y - b * e_x
correlation = (covar1 / (var_x * var_y))
correlation = np.sum((b * x + a - e_y)**2) / np.sum((y - e_y)**2)
print("Covar1(x,y)(E[(x-E[x])(y-E[y])):", covar1)
print("Covar2(x,y)(E[xy]-E[x]E[y]):", covar2)
print("Covar3(x,y)(numpy):\n", covar3)
print("Eigen values of covar(x,y):\n", np.linalg.eig(covar3))
print(a, b)
print("Correlation coefficient:\n", correlation)

xx = np.linspace(-10, 10, 100)
yy = b * xx + a
plot.plot(xx, yy)
plot.scatter(x, y)
plot.show()
