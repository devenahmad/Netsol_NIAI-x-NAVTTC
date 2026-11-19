# Task 39 - sorting numpy arrays
import numpy as np

a = np.array([3, 2, 0, 1, 9, 4])
print(np.sort(a))
print(a)

a.sort()
print(a)

print(np.sort(a)[::-1])

print(np.sort(np.array(["banana", "apple", "cherry"])))
print(np.sort(np.array([True, False, True])))

# 2d
m = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(m))
print(np.sort(m, axis=0))

names = np.array(["ali", "sara", "bilal"])
marks = np.array([70, 95, 82])
order = np.argsort(marks)
print(order)
print(names[order])
print(names[order][::-1])