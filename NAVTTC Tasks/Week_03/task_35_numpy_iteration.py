# Task 35 - looping over numpy arrays
import numpy as np

a = np.array([1, 2, 3])
for x in a:
    print(x)

# 2d
m = np.array([[1, 2, 3], [4, 5, 6]])
for row in m:
    print(row)

for row in m:
    for x in row:
        print(x, end=" ")
print()

# nditer does it in one loop
for x in np.nditer(m):
    print(x, end=" ")
print()

# 3d
t = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(t):
    print(x, end=" ")
print()

# ndenumerate gives index too
for idx, x in np.ndenumerate(m):
    print(idx, x)

# change dtype while looping
for x in np.nditer(a, flags=["buffered"], op_dtypes=["S"]):
    print(x)

for x in np.nditer(m[:, ::2]):
    print(x, end=" ")
print()