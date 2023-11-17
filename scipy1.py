import numpy as np
import scipy.fft as fft
import scipy.integrate as integrate
import scipy.special as special
import scipy.linalg as linalg
import math

print("special.exp10(5):", special.exp10(5))
print()

print("special.sindg(90):", special.sindg(90))
print()

print("math.exp(1):", math.exp(1))
print()

print("integrate.quad(lambda x: math.exp(x), 0, 10):", integrate.quad(lambda x: math.exp(x), 0, 10))
print("integrate.quad(lambda x: np.exp(-x), 0, np.inf):", integrate.quad(lambda x: np.exp(-x), 0, np.inf))
print()

print("fft.fft(np.array([1,2,3,4,5,6,7,8,9,10])):", fft.fft(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
print()

print("linalg.solve(np.array([[1, 0],[0, 1]]),np.array([1, 3])):",
      linalg.solve(
          np.array([
              [1, 0],
              [0, 1]
          ]),
          np.array(
              [1, 3]
          )
      )
      )
print()

print("linalg.inv(np.array([[1, 0],[0, 1]])):\n",
      linalg.inv(np.array([
          [1, 0],
          [0, 1]
      ]))
      )
print()

print("linalg.eig([ [1, 0], [0, 4] ]):\n", linalg.eig([[1, 0], [0, 4]]))
