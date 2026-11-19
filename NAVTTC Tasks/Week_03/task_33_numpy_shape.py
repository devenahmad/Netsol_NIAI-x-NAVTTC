# Task 33 - numpy array shape
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
c = np.zeros((2, 3, 4))

print("a shape:", a.shape)
print("b shape:", b.shape)
print("c shape:", c.shape)

print("rows:", b.shape[0], "cols:", b.shape[1])
print("size (total items):", b.size)
print("ndim:", b.ndim)

x = np.array([1, 2, 3, 4], ndmin=5)
print(x)
print("ndim of x:", x.ndim)
print("shape of x:", x.shape)

print(len(b))