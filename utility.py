import numpy as np

arr = np.array([1,2,3,4,3,5,6,34,2,6,3,23,6,234,2])
for i, v in enumerate(arr):
    print(i, v)
print("argmax:", np.argmax(arr))

