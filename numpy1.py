import numpy as np
import scipy as sp

vector1 = np.array(
    [1, 2, 3]
)
vector2 = np.array(
    [4, 5, 6]
)
matrix1 = np.array(
    [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    ]
)

print(vector1)
print(matrix1)
print(np.linalg.eig(matrix1))
