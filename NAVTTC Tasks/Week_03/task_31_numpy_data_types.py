# Task 31 - numpy data types
import numpy as np

print(np.array([1, 2, 3]).dtype)
print(np.array([1.5, 2.5]).dtype)
print(np.array(["a", "b"]).dtype)
print(np.array([True, False]).dtype)

a = np.array([1, 2, 3], dtype="int8")
print(a.dtype, a.itemsize, "byte per item")

b = np.array([1, 2, 3], dtype="float64")
print(b.dtype, b.itemsize, "bytes per item")

f = np.array([1.1, 2.7, 3.9])
i = f.astype(int)
print(i)

x = np.array([1, 0, 2])
print(x.astype(bool))

s = np.array(["1", "2", "3"])
print(s.astype(int) + 1)

big = np.array([100, 120], dtype="int8")
print(big + 20)

print(np.issubdtype(f.dtype, np.floating))