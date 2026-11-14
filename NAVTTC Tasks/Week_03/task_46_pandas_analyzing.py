# Task 46 - analyzing data with pandas
import numpy as np
import pandas as pd

np.random.seed(1)
n = 20
df = pd.DataFrame({
    "age": np.random.randint(18, 60, n),
    "salary": np.random.randint(30000, 120000, n),
    "dept": np.random.choice(["it", "hr", "sales"], n),
    "rating": np.random.choice([1, 2, 3, 4, 5], n),
})

print(df.head())
print("\nlast 3 rows")
print(df.tail(3))

print("\nshape:", df.shape)
print("\ninfo")
df.info()

print("\ndescribe")
print(df.describe())

print("\ncolumn types")
print(df.dtypes)

print("\nunique departments:", df["dept"].unique())
print("\ncount per department")
print(df["dept"].value_counts())

print("\naverage salary by dept")
print(df.groupby("dept")["salary"].mean().round(0))

print("\nhighest paid")
print(df.sort_values("salary", ascending=False).head(3))

print("\nnull values per column")
print(df.isnull().sum())