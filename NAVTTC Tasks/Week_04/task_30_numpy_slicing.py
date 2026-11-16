# Task 30 - numpy slicing
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7])

print(a[1:5])
print(a[4:])
print(a[:4])
print(a[-3:-1])
print(a[::2])
print(a[::-1])

# 2d
m = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15]])

print(m[1, 1:4])
print(m[0:2, 2])
print(m[0:2, 1:4])
print(m[:, ::2])
print(m[::2, :])

# slices share memory with the original
part = m[0, :3]
part[0] = 999
print(m[0])