import numpy as np
import scipy.fft as fft
import scipy.integrate as integrate
import scipy.special as special
import scipy.linalg as linalg
import math


print("special.exp10(5):", special.exp10(5))
print("special.sindg(90):", special.sindg(90))
print("math.exp(0):", math.exp(0))
print("integrate.quad(lambda x: math.exp(x), 0, 10):", integrate.quad(lambda x: math.exp(x), 0, 10))
print("fft.fft(np.array([1,2,3,4,5,6,7,8,9,10])):", fft.fft(np.array([1,2,3,4,5,6,7,8,9,10])))
print("linalg.solve(np.array([[1, 0],[0, 1]]),np.array([1, 3])):",
linalg.solve(
    np.array([
        [1, 0],
        [0, 1]
    ]),
    np.array(
        [1, 3]
    )
))
print("linalg.inv(np.array([[1, 0],[0, 1]])):\n",
linalg.inv(np.array([
    [1, 0],
    [0, 1]
])))
