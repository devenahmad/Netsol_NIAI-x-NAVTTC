# Task 37 - splitting numpy arrays
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

parts = np.array_split(a, 3)
print(parts)
print(parts[0], parts[1], parts[2])

print(np.array_split(a, 4))

print(np.split(a, 2))

# 2d
m = np.arange(1, 13).reshape(4, 3)
print(m)
for p in np.array_split(m, 2):
    print(p)
    print("--")

for p in np.array_split(m, 3, axis=1):
    print(p)
    print("--")

print(np.hsplit(m, 3))
print(np.vsplit(m, 2))

print(np.split(a, [2, 4]))

print(np.delete(a, 0))