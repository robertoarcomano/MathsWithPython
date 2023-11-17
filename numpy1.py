import numpy as np
import scipy as sp

print("vector1 = np.array([1, 2, 3])")
vector1 = np.array(
    [1, 2, 3]
)
print("vector1.itemsize:", vector1.itemsize)
print("vector1.dtype:", vector1.dtype)
print("vector1.ndim:", vector1.ndim)
print("vector1.size:", vector1.size)
print("vector1.shape:", vector1.shape)
print("vector1.max():", vector1.max())
print("vector1.min():", vector1.min())
print("vector1.mean():", vector1.mean())
print("vector1.sum():", vector1.sum())
print("np.dot(vector1, vector1):", np.dot(vector1, vector1))
print()

print("matrix1 = np.array([(1, 2, 3),(4, 5, 6),(7, 8, 9))])")
matrix1 = np.array(
    [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    ]
)

print("matrix1:\n", matrix1)
print("matrix1[0,1]:", matrix1[0,1])
print("matrix1[:,1]:", matrix1[:,1])
print("matrix1.ndim:", matrix1.ndim)
print("matrix1.size:", matrix1.size)
print("matrix1.shape:", matrix1.shape)
print("matrix1.ravel():", matrix1.ravel())
print("matrix1.sum():", matrix1.sum())
print("matrix1.sum(axis=0):", matrix1.sum(axis=0))
print("matrix1.sum(axis=1):", matrix1.sum(axis=1))
print("np.sqrt(matrix1):\n", np.sqrt(matrix1))
print("np.std(matrix1):\n", np.std(matrix1))
print("np.exp(matrix1):\n", np.exp(matrix1))
print("np.log(matrix1):\n", np.log(matrix1))
print("np.linalg.eig(matrix1):\n", np.linalg.eig(matrix1))
print()

print("matrix2 = np.array([(1, 2, 3),(4, 5, 6))])")
matrix2 = np.array(
    [
        (1, 2, 3),
        (4, 5, 6)
    ]
)

print("matrix2:\n", matrix2)
print("matrix2.ndim:", matrix2.ndim)
print("matrix2.size:", matrix2.size)
print("matrix2.shape:", matrix2.shape)
print()

print("matrix1+matrix1:\n", matrix1+matrix1)
print("matrix1*2:\n", matrix1*2)
print("matrix1*matrix1:\n", matrix1*matrix1)
print("np.matmul(matrix1,matrix1):\n", np.matmul(matrix1, matrix1))
print("np.dot(matrix1,matrix1):\n", np.dot(matrix1, matrix1))
print()

print("matrix3 = matrix2.reshape(3,2)")
matrix3 = matrix2.reshape(3,2)
print("matrix3:\n", matrix3)
print()

print("np.linspace(0,50,10):", np.linspace(5,50,10))
