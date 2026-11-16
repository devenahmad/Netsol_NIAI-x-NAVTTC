# Task 34 - numpy reshape
import numpy as np

a = np.arange(1, 13)
print(a)

# 1d -> 2d
print(a.reshape(4, 3))
print(a.reshape(2, 6))

# 1d -> 3d
print(a.reshape(2, 3, 2))

print(a.reshape(3, -1))
print(a.reshape(-1, 2).shape)

# flatten back to 1d
m = a.reshape(3, 4)
print(m.flatten())
print(m.reshape(-1))
print(m.ravel())

print(m.T)
print(m.T.shape)

try:
    a.reshape(5, 3)
except ValueError as e:
    print("error:", e)

v = np.array([1, 2, 3])
print(v.shape, "->", v[:, np.newaxis].shape)
print(v.reshape(-1, 1))