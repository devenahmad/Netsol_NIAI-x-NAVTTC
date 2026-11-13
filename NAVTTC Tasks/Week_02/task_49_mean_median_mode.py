# Task 49 - mean, median and mode
import numpy as np
from statistics import mode, multimode

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

mean = np.mean(speed)
median = np.median(speed)
most_common = mode(speed)

print("speeds:", speed)
print("mean   :", round(mean, 2), "(the average)")
print("median :", median, "(the middle one when sorted)")
print("mode   :", most_common, "(shows up most)")

print("\nmultimode of [1,1,2,2,3]:", multimode([1, 1, 2, 2, 3]))

# why median matters -> one huge outlier
salaries = [40, 42, 45, 47, 50, 1000]
print("\nsalaries:", salaries)
print("mean   :", np.mean(salaries))
print("median :", np.median(salaries))
print("the mean got dragged up by the outlier, the median didn't")

# scipy way if you have it (if not works, install it with "pip install scipy" or "pip install --upgrade scipy")
try:
    from scipy import stats
    print("\nscipy mode:", stats.mode(speed, keepdims=False).mode)
except ImportError:
    print("\nscipy is not installed, so the scipy mode was skipped.")
    print("Install it with: pip install scipy")