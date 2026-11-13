# Task 50 - standard deviation and variance
import numpy as np

speed1 = [86, 87, 88, 86, 87, 85, 86]
speed2 = [32, 111, 138, 28, 59, 77, 97]

for name, s in (("speed1", speed1), ("speed2", speed2)):
    print(name, s)
    print("  mean     :", round(np.mean(s), 2))
    print("  variance :", round(np.var(s), 2))
    print("  std dev  :", round(np.std(s), 2))
    print()

print("speed1 is tightly packed, speed2 is all over the place")

v = np.var(speed2)
print("sqrt of variance:", round(v ** 0.5, 2), "= std:", round(np.std(speed2), 2))

data = speed2
m = sum(data) / len(data)
manual_var = sum((x - m) ** 2 for x in data) / len(data)
print("by hand variance:", round(manual_var, 2))

print("sample std:", round(np.std(speed2, ddof=1), 2))

std = np.std(speed2)
mean = np.mean(speed2)
inside = [x for x in speed2 if abs(x - mean) <= std]
print("within one std:", inside)