# Task 43 - pandas series (one column of data)
import pandas as pd

a = pd.Series([1, 7, 2])
print(a)
print(a[0])

b = pd.Series([10, 20, 30], index=["x", "y", "z"])
print(b)
print(b["y"])

calories = {"day1": 420, "day2": 380, "day3": 390}
c = pd.Series(calories)
print(c)

print(pd.Series(calories, index=["day1", "day2"]))

print(c * 2)
print(c.mean(), c.max(), c.min(), c.sum())

print(c[c > 385])

c.name = "calories"
print(c)

print(c.describe())
