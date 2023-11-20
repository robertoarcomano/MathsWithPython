import numpy as np
import matplotlib.pyplot as plot

data = np.array([
    [0, 0],
    [1, 2],
    [2, 4],
    [3, 7],
    [4, 10],
    [5, 11],
    [6, 30],
    [7, 100],
    [8, 150],
    [9, 160]
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
correlation = np.sum((b * x + a - e_y)**2) / np.sum((y - e_y)**2)
print("Covar1(x,y)(E[(x-E[x])(y-E[y])):", covar1)
print("Covar2(x,y)(E[xy]-E[x]E[y]):", covar2)
print("Covar3(x,y)(numpy):\n", covar3)
print("Eigen values of covar(x,y):\n", np.linalg.eig(covar3))
print(a, b)
print("Correlation coefficient:\n", correlation)

xx = np.linspace(min(x), max(x), 100)
yy = b * xx + a

plot.subplot(221)
plot.plot(xx, yy)
plot.scatter(x, y)
plot.xlabel("Using Least square error")

plot.subplot(222)
fn = np.polyfit(x, y, 1)
yyy = np.polyval(fn, xx)
print("fn:", fn)
print("b,a:", b, a)
plot.plot(xx, yyy)
plot.scatter(x, y)
plot.xlabel("Using numpy.polyval()")

plot.subplot(223)
fn = np.polyfit(x, y, 4)
yyy = np.polyval(fn, xx)
print("fn:", fn)
print("b,a:", b, a)
plot.plot(xx, yyy)
plot.scatter(x, y)
plot.xlabel("Using numpy.polyval(4)")

plot.subplot(224)
fn = np.polyfit(x, y, 8)
yyy = np.polyval(fn, xx)
print("fn:", fn)
print("b,a:", b, a)
plot.plot(xx, yyy)
plot.scatter(x, y)
plot.xlabel("Using numpy.polyval(8)")

plot.show()
