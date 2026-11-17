# Task 48 - correlation with pandas
import numpy as np
import pandas as pd

np.random.seed(0)
n = 100
hours = np.random.uniform(0, 10, n)

df = pd.DataFrame({
    "study_hours": hours,
    "marks": hours * 8 + np.random.normal(0, 8, n) + 10,
    "tv_hours": 10 - hours + np.random.normal(0, 2, n),
    "random_stuff": np.random.normal(0, 1, n),
})

print(df.corr().round(2))

print("\nstudy vs marks:", round(df["study_hours"].corr(df["marks"]), 2))
print("study vs tv:", round(df["study_hours"].corr(df["tv_hours"]), 2))
print("study vs random:", round(df["study_hours"].corr(df["random_stuff"]), 2))

print("\nrule of thumb:")
print("  close to +1 -> move together")
print("  close to -1 -> move opposite")
print("  close to 0  -> no straight line link")

print("\nlinks with marks")
print(df.corr()["marks"].drop("marks").sort_values(ascending=False).round(2))