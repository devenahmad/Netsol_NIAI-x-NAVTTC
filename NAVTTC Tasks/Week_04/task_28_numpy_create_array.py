# Task 28 - creating numpy arrays
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a, type(a))

# 2d & 3d
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c)
print("dims:", a.ndim, b.ndim, c.ndim)

print(np.zeros(4))
print(np.ones((2, 3)))
print(np.full((2, 2), 7))
print(np.eye(3))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))

print(np.random.rand(3))
print(np.random.randint(1, 100, 5))
print(np.random.randn(2, 2))

f = np.array([1, 2, 3], dtype=float)
print(f, f.dtype)