# Task 32 - numpy copy vs view
import numpy as np

# copy is separate
a = np.array([1, 2, 3, 4, 5])
c = a.copy()
a[0] = 100
print("a:", a)
print("copy:", c)

# view shares data
a = np.array([1, 2, 3, 4, 5])
v = a.view()
a[0] = 100
print("a:", a)
print("view:", v)

v[1] = 555
print("a after changing view:", a)

print("copy owns data:", c.base is None)
print("view owns data:", v.base is None)
print("view's base is a:", v.base is a)

# slices are views
s = a[1:3]
s[0] = -1
print(a)

# reshape also gives a view
r = a.reshape(5, 1)
r[0, 0] = 42
print(a)