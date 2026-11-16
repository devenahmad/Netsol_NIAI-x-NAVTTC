# Task 36 - joining numpy arrays
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate((a, b)))

# 2d
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(np.concatenate((m1, m2), axis=0))
print(np.concatenate((m1, m2), axis=1))

print(np.stack((a, b), axis=0))
print(np.stack((a, b), axis=1))
print(np.hstack((a, b)))
print(np.vstack((a, b)))
print(np.dstack((a, b)))

print(np.append(a, [7, 8]))

print(np.insert(a, 1, 99))
